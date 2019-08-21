# Visual Tree
Visualization of the directory tree

❤️ This python code generates a visual version of the directory tree from the command line.

### Example
```
{Visual Tree}
C:\Users\John\Documents
      <> Projects
         <> Arizona
         <> Coca-cola
         <> Inspection
      <> Personal
         <> CV-ver1
         <> CV-ver2
         <> CoverLetter
         <> Resume-2019
      <> Empty
      <> Private
         <> 2018-summer
         <> 2019-summer
Visual directory tree for: Documents
Total count of 5 directories and 9 files
```

### Requirements
In order to run this code, you need to install Python  2.7

Also, you need to install the `walkdir` library.
```
pip install walkdir
```
Learn more about the walkdir library documentation [here](walkdir.readthedocs.io)

### How to Use
Run the following command.
```
> python main.py <PATH>
```

To use the optional arguments, refer to the following documentation.
```
> python main.py -h
usage: main.py [-h] [-depth DEPTH] [-file FILE] path

positional arguments:
  path          Root directory

optional arguments:
  -h, --help    show this help message and exit
  -depth DEPTH  Maximum depth of tree
  -file FILE    Maximum number of files displayed in one directory
```
* `-depth` indicates the maximum depth of the tree, starting from the root. The depth of the root is 0. The default value for this argument is set to 5, but you can change the value through the command line argument.
* `-file` indicates the maximum number of files displayed in one directory. The rest will not appear in the visual representation of the tree. `> ...` indicates that there are more than maximum number of files in this directory. The default value for this argument is set to 10, but you can change the value through the command line argument.
