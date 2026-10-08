"""Q5 cross-check: among 4-itemsets with support count >= 130, find the rules with highest confidence."""
import csv, itertools, collections
rows = list(csv.reader(open("hw1_2026.csv", encoding="utf-8-sig")))
H = rows[0]
T = [frozenset(H[i] for i, v in enumerate(r) if v == "TRUE") for r in rows[1:] if r]
N, MIN = len(T), 130
cnt = collections.Counter()
for k in range(1, 5):
    c = collections.Counter()
    for t in T:
        for s in itertools.combinations(sorted(t), k):
            if k == 1 or all(frozenset(x) in cnt for x in itertools.combinations(s, k - 1)):
                c[frozenset(s)] += 1
    freq = {s: n for s, n in c.items() if n >= MIN}
    cnt.update(freq)
    print(f"L({k}) = {len(freq)}")
L4 = [s for s in cnt if len(s) == 4]
rules = []
for s in L4:
    for r in range(1, 4):
        for a in itertools.combinations(sorted(s), r):
            a = frozenset(a); b = s - a
            conf = cnt[s] / cnt[a]
            rules.append((conf, conf / (cnt[b] / N), sorted(a), sorted(b), cnt[a], cnt[s]))
rules.sort(key=lambda x: -x[0])
for conf, lift, a, b, na, ns in rules[:5]:
    print(f"{a} ({na}) ==> {b} ({ns})  conf={conf:.4f} lift={lift:.2f}")
