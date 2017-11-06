def bacafile():
    with open('media/PLBBSGRC01-1082017.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]

def jumlah(content, n=1):
    length = len(content)
    for num_idx in range(0, length, n):
        yield content[num_idx:min(num_idx + n, length)]


def emit(batched):
    for n, name in enumerate([
        " "
    ]):
        yield name, batched[n]

