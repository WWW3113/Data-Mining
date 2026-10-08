"""Preprocess hw1_2026.csv for Apriori: keep only TRUE (item bought), FALSE -> missing '?'.
Outputs:
  hw1_2026_preprocessed.arff  (Weka input; each attribute is nominal {TRUE}, FALSE becomes '?')
  hw1_2026_preprocessed.csv   (same data in CSV, FALSE replaced by '?')
"""
import csv, sys

src = sys.argv[1] if len(sys.argv) > 1 else "hw1_2026.csv"
with open(src, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))
header, data = rows[0], [r for r in rows[1:] if r]
print(f"{len(data)} transactions, {len(header)} items")

def q(name):
    return "'" + name.replace("\\", "\\\\").replace("'", "\\'") + "'"

with open("hw1_2026_preprocessed.arff", "w", encoding="utf-8") as f:
    f.write("@relation hw1_2026_transactions\n\n")
    for h in header:
        f.write(f"@attribute {q(h)} {{TRUE}}\n")
    f.write("\n@data\n")
    for r in data:
        f.write(",".join("TRUE" if v.strip().upper() == "TRUE" else "?" for v in r) + "\n")

with open("hw1_2026_preprocessed.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(header)
    for r in data:
        w.writerow(["TRUE" if v.strip().upper() == "TRUE" else "?" for v in r])
