import itertools

def is_safe(report):
    diffs =[(b-a) for a, b in itertools.pairwise(report)]
    return all(1 <= i <= 3 for i in diffs) or all(-3 <= i <= -1 for i in diffs)

def is_safe_enough(report):
    if is_safe(report): return True
    for i in range(len(report)):
        to_test = report[:i]+report[i+1:]
        if is_safe(to_test): return True
    return False

def main():
    report = []
    with open('input.txt') as f:
        for line in f.readlines():
            report.append([int(level) for level in line.split()])


    print(sum(is_safe(r) for r in report))
    print(sum(is_safe_enough(r) for r in report))

if __name__ == '__main__':
    main()