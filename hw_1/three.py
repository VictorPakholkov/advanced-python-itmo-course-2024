import sys

def cli():
    args = sys.argv
    l = 0
    w = 0
    c = 0
    if len(args) > 2:
        for i in range(1, len(args)):
            l_l = 0
            w_l = 0
            c_l = 0
            with open(args[i], 'r') as f:
                lines = f.readlines()
            for line in lines:
                c += len(line)
                c_l += len(line)
                a = line.rstrip('\n')
                l_l += 1
                w_l += len(list(a.split()))
                l += 1
                w += len(list(a.split()))
            l -= 1
            l_l -= 1
            print('\t', sep='', end='')
            print(l_l, w_l, c_l, args[i], sep='\t')
        print('\t', sep='', end='')
        print(l, w, c, 'total', sep='\t')
    elif len(args) == 2:
        with open(args[1], 'r') as f:
            lines = f.readlines()
        for line in lines:
            c += len(line)
            a = line.rstrip('\n')
            l += 1
            w += len(list(a.split()))
        l -= 1
        print('\t', sep='', end='')
        print(l, w, c, args[1], sep='\t')
    else:
        lines = []
        for line in sys.stdin:
            lines.append(line)
        for line in lines:
            c += len(line)
            a = line.rstrip('\n')
            l += 1
            w += len(list(a.split()))
        l -= 1
        print('\t', sep='', end='')
        print(l, w, c, sep='\t')

if __name__ == "__main__":
    cli()