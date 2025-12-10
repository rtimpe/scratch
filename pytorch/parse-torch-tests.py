"""
Parses test reports to look for failures

1. Go to the hud page for the pr (i.e. https://hud.pytorch.org/pr/167407)
2. Figure out which step you're interested in (i.e. linux-jammy-py3.14t-clang12)
3. Click through to the appropriate github action page
4. Copy the job number (last part of the url)
5. Search for the job number on the hud page, looking for artifacts that begin with test-jsons and download the zip file
6. Repeat as necessary for sharded tests
7. Extract each zip file.  The should be merged in test/test-reports/python-pytest
8. Invoke with
   $ python parse-torch-tests.py --dir ~/Downloads/test/test-reports/python-pytest/
"""

import argparse
import json
from pathlib import Path


def parse_tests(dir: Path):
    for p in dir.glob("**/*.json"):
        with open(p) as f:
            for l in f:
                j = json.loads(l)
                if "failure" in j:
                    print(
                        f"{j['file']}: {j['invoking_file']} {j['classname']}{j['name']}"
                    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dirs", nargs="*", type=Path)
    args = parser.parse_args()

    for d in args.dirs:
        parse_tests(d)


if __name__ == "__main__":
    main()
