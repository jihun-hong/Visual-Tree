import os
import argparse

from utils import check, offset, summary
from walkdir import filtered_walk

INDENT = "   "
SYMBOL = "<> "


def main(args):

    root = args.path
    if not check(root):
        raise ValueError("Warning! Root directory isn't valid")

    max_dep = args.depth
    max_file = args.file
    assert max_dep > 0 and max_file > 0

    print("{Visual Tree}")

    dir_count = 0
    file_count = 0
    for path, _, files in sorted(filtered_walk(root, depth=max_dep)):
        level = offset(root, path)
        base = os.path.basename(path)

        if level == 1:
            print(path)
        else:
            print(INDENT * level + SYMBOL + base)
        dir_count += 1

        # display files
        level += 1
        local_count = 0
        display = True
        for file in sorted(files):
            file_count += 1
            local_count += 1
            if display:
                print(INDENT * level + SYMBOL + file)
            if local_count == max_file + 1:
                display = False
                print(INDENT * level + SYMBOL + "...")

    summary(root, dir_count, file_count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Required arguments
    parser.add_argument(dest='path', type=str, help="Root directory")
    parser.add_argument('-depth', type=int, default=5, help="Maximum depth of tree")
    parser.add_argument('-file', type=int, default=10, help="Maximum number of files displayed in one directory")

    args = parser.parse_args()
    main(args)
