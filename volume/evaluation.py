

def evaluation(inp: str) -> str:
    out = 'output: '
    for line in inp.split('\n'):
        out += line.upper()
        out += '  '
    return out
