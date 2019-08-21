import os


def check(path):
    if path.endswith("/"):
        return False
    if not os.path.isdir(path):
        return False
    if not os.path.exists(path):
        return False
    return True


def offset(reference, directory):
    return directory.count(os.path.sep) - reference.count(os.path.sep) + 1


def summary(root, dir_count, file_count):
    path_base = os.path.basename(root)

    print("Visual directory tree for: " + path_base)
    print("Total count of %s directories and %s files" % (dir_count, file_count))
