import csv
from pathlib import Path
import io
import os

def combine_csv_in_dir(dirpath, result_path):
    folder = Path(dirpath)
    for file in folder.glob("*.csv"):
        csv_file = csv.reader(Path(file).read_text(encoding="utf-8"))
        

print("Tester combine_csv_in_dir... ", end="")
# Mappen samples må ligge i samme mappe som denne filen
dirpath = os.path.join(os.path.dirname(__file__), "samples")
combine_csv_in_dir(dirpath, "combined_table.csv")
with open("combined_table.csv", "rt", encoding='utf-8') as f:
   content = f.read()
   assert("""\
uibid,karakter,kommentar
abc104,C,hei
abc105,D,"med komma, her er jeg"
abc106,E,tittit
abc101,A,Her er min kommentar
abc102,B,"Jeg er glad, men her er komma"
abc103,C,Katching
""" == content or """\
uibid,karakter,kommentar
abc101,A,Her er min kommentar
abc102,B,"Jeg er glad, men her er komma"
abc103,C,Katching
abc104,C,hei
abc105,D,"med komma, her er jeg"
abc106,E,tittit
""" == content)
print("OK")
