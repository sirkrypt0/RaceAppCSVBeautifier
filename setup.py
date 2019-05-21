# from distutils.core import setup
import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\SirKrypto\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\SirKrypto\AppData\Local\Programs\Python\Python35\tcl\tk8.6'

base = None
if sys.platform == "win32":
    base = 'Win32GUI'

executables = [
    Executable('main.py', base=base, targetName="RaceAppCSV.exe")
]

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

options = {
    'build_exe': {
        "packages": ["numpy", "tkinter"],
        "includes": ["numpy.core._methods"],
        "excludes": [],
        'include_files': [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ]
    }
}

setup(name='RaceAppCSV',
      version='1.0',
      description='RaceApp CSV Beautifier',
      options=options,
      executables=executables
      )