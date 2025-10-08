import sys
import struct
import os
import traceback

# Optional: small GUI bits for picking files / showing errors
try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
    TK_OK = True
except Exception:
    TK_OK = False

def get_exe_architecture(path):
    with open(path, "rb") as f:
        # Locate PE header via MS-DOS header
        f.seek(0x3C)
        pe_offset_data = f.read(4)
        if len(pe_offset_data) != 4:
            return "Not a valid PE file (truncated header)"
        pe_offset = struct.unpack("<I", pe_offset_data)[0]

        # Verify PE signature
        try:
            f.seek(pe_offset)
        except Exception:
            return "Not a valid PE file (bad PE offset)"
        pe_signature = f.read(4)
        if pe_signature != b"PE\0\0":
            return "Not a valid PE file (missing 'PE\\0\\0' signature)"

        # Machine field (2 bytes) identifies target CPU
        machine_bytes = f.read(2)
        if len(machine_bytes) != 2:
            return "Not a valid PE file (truncated COFF header)"
        machine = struct.unpack("<H", machine_bytes)[0]

        # Common machine values
        if machine == 0x014c:
            # Could be PE32 (x86) or IL-only .NET that runs AnyCPU.
            # We’ll try to read Optional Header 'Magic' to be clearer.
            magic = _read_optional_magic(f)
            if magic == 0x10B:
                return "32-bit (x86, PE32)"
            elif magic == 0x20B:
                # Rare combination, but handle gracefully.
                return "64-bit (PE32+), reported machine x86"
            else:
                return "32-bit (x86)"
        elif machine == 0x8664:
            return "64-bit (x64, AMD64)"
        elif machine == 0x0200:
            return "Itanium (IA-64)"
        elif machine == 0x01c0:
            return "ARM (32-bit)"
        elif machine == 0x01c4:
            return "ARMv7 (Thumb-2)"
        elif machine == 0xAA64:
            return "ARM64 (AArch64)"
        else:
            return f"Unknown architecture (machine=0x{machine:X})"

def _read_optional_magic(f):
    """
    We are currently 2 bytes into the COFF header (Machine already read).
    COFF header is 20 bytes total, so we need to skip the remaining 18 bytes
    to reach the Optional Header and read its 'Magic' (first 2 bytes).
    Magic: 0x10B => PE32, 0x20B => PE32+
    """
    # We've read 2 of the 20 COF
