# RenPy_Import_Issue
Simple RenPy project demonstrating my problem importing python modules.

# This I have tried:
* I have my repo working in both python 2.7.18 and 3.9.1 using from __future__ and from builtins.
* I have decent sized pytest suite to validate a large portion of my code with Unit Tests at least.
* I have tried using various methods to load items into a .rpy file:
  * from mymodule import SomeClass
  * from mymodule.module import SomeClass
* I can make either work but I have to wrap imports with try blocks as it looks like absolute_import is not being used by Ren'Py
* As in my test repo here I have multiple files and imports which either block on the above so I need to use try blocks or end up with the `TypeError: 'dict_keys' object does not support indexing` exception.

I'll add some branches with variations to see if that helps while I tinker with options.
