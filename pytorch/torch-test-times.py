import argparse
from pprint import pp
import json
from pathlib import Path

def parse_tests(dir: Path):
    tests = {}
    for p in dir.glob("**/*.json"):
        with open(p) as f:
            for l in f:
                j = json.loads(l)
                k = j['file'] + ' ' + j['classname'] + '.' + j['name']
                tests[k] = j['time']
    return tests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ft-dirs', nargs='*', type=Path)
    parser.add_argument('--gil-dirs', nargs='*', type=Path)
    args = parser.parse_args()

    for d in args.ft_dirs:
        ft_tests = parse_tests(d)
    for d in args.gil_dirs:
        gil_tests = parse_tests(d)

    print(f'gil only: {gil_tests.keys() - ft_tests.keys()}')
    print(f'ft only: {ft_tests.keys() - gil_tests.keys()}')
    diffs = []
    for k in gil_tests.keys() & ft_tests.keys():
        if gil_tests[k] > 5:
            diffs.append(((ft_tests[k] - gil_tests[k]) / (gil_tests[k] + .00000001), k, gil_tests[k], ft_tests[k]))

    print(f'gil tot: {sum(gil_tests.values()) / 60}')
    print(f'ft tot: {sum(ft_tests.values()) / 60}')
    pp(sorted(diffs))

if __name__ == '__main__':
    main()
