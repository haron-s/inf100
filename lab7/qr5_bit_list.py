from qr6_error_correction import generate_error_correction

def toBinary(character):
    return f'{ord(character):08b}'

def string_to_data(content_string):
    return [int(bit) for character in content_string for bit in toBinary(character)]

def get_core_bit_list(content_string):
    modus = [0, 1, 0, 0]
    data = string_to_data(content_string)
    byte_len = [int(bit) for bit in f'{(len(data)//8):08b}']
    term = [0, 0, 0, 0]
    return modus + byte_len + data + term

def pad_bit_list(core_bit_list, pad_to_bytes):
    pad_list = []

    total_len = pad_to_bytes - (len(core_bit_list) // 8)
    for i in range(total_len):
        if i % 2 == 0:
            pad_list += [1, 1, 1, 0, 1, 1, 0, 0]
        else:
            pad_list += [0, 0, 0, 1, 0, 0, 0, 1]

    core_bit_list[:] += pad_list

def string_to_bit_list(content_string, qr_layout):
    correction_bytes = {'L': 10, 'M': 16, 'Q': 22, 'H': 28}
    core_bit_list = get_core_bit_list(content_string)
    core_byte_len = len(core_bit_list) // 8

    correction_level = ""
    for correction_byte in correction_bytes:
        if correction_bytes[correction_byte] + core_byte_len <= qr_layout["byte_capacity"]:
            correction_level = correction_byte
            total_len = correction_bytes[correction_byte] + core_byte_len

    pad_to_bytes = qr_layout["byte_capacity"] - total_len
    if pad_to_bytes > 0:
        pad_bit_list(core_bit_list, pad_to_bytes)
    elif pad_to_bytes < 0:
        raise ValueError("core_byte_len too long")
    
    return (generate_error_correction(core_bit_list, correction_level), correction_level)
