import itertools

def solve(w1, w2, res):
    chars = "".join(set(w1 + w2 + res))
    firsts = {w1[0], w2[0], res[0]}
    
    for p in itertools.permutations(range(10), len(chars)):
        d = dict(zip(chars, p))
        if any(d[f] == 0 for f in firsts): continue
        
        # Helper to convert word to number
        to_num = lambda word: int("".join(str(d[c]) for c in word))
        
        if to_num(w1) + to_num(w2) == to_num(res):
            return f"{to_num(w1)} + {to_num(w2)} = {to_num(res)} (Mapping: {d})"
    return "No solution"

print(solve("SEND", "MORE", "MONEY"))