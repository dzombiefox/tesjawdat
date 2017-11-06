import json
def bacafile():
    with open('PLBBSGRC01-1082017.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


def batch(content, n=1):
    length = len(content)
    for num_idx in range(0, length, n):
        yield content[num_idx:min(num_idx+n, length)]


def emit(batched):
    for n, name in enumerate([
        "PLBBSGRC01-1082017"
    ]):
        yield name, batched[n]

content = bacafile()
batched = batch(content, 6)
res = [dict(emit(b)) for b in batched]
print(res)

with open('out.json', 'w') as f:
    f.write(json.dumps(res, indent=4))