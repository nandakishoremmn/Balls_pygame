from distutils.core import setup
import py2exe
import os

Mydata_files = []
for files in os.listdir('images/'):
    f1 = 'images/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'images', [f1]
        Mydata_files.append(f2)
for files in os.listdir('sounds/'):
    f1 = 'sounds/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'sounds', [f1]
        Mydata_files.append(f2)


setup(
    version = "1.0",
    description = "Catch It!",
    name = "Catch It!",
    windows = [{"script":"main.py"}],
    data_files = Mydata_files
    )
