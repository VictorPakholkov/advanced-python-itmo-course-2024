import sys

def cli():
    args = sys.argv
    if len(args) > 2:
        for i in range(1, len(args)):
            print("==> ", args[i], "<==", sep='')
            with open(args[i], 'r') as f:
                lines = f.readlines()
            for line in lines[-10:]:
                print(line.rstrip('\n'))
    elif len(args) == 2:
        with open(args[1], 'r') as f:
            lines = f.readlines()
        for line in lines[-10:]:
            print(line.rstrip('\n'))
    else:
        lines = []
        for line in sys.stdin:
            lines.append(line)
        for line in lines[-17:]:
             print(line.rstrip('\n'))


if __name__ == "__main__":
    cli()