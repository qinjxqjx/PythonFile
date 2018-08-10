def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        print "==" + line
        if line.strip():
            block.append(line)
        elif block:
            print '1'
            print block
            yield ''.join(block).strip()
            block = []