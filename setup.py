# Use pyinstaller to create .exe


##################################
# from distutils.core import setup
# import sys
# import os
# import py2exe
#
# os.environ['TCL_LIBRARY'] = r'C:\Users\Tobias\AppData\Local\Programs\Python\Python34\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Users\Tobias\AppData\Local\Programs\Python\Python34\tcl\tk8.6'
#
# PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
#
# setup(options={'py2exe': {'bundle_files': 1,
#                           'compressed': True,
#                           "includes": ["openpyxl", "tkinter"],
#                           "dll_excludes": [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
#                                          os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]
#                           }
#                },
#       windows=[{'script': "main.py"}],
#       )


# """
# from cx_Freeze import setup, Executable
#
# os.environ['TCL_LIBRARY'] = r'C:\Users\Tobias\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Users\Tobias\AppData\Local\Programs\Python\Python35\tcl\tk8.6'
#
#
#
# base = None
# if sys.platform == "win32":
#     base = 'Win32GUI'
#
# executables = [
#     Executable('main.py', base=base, targetName="RaceAppCSV.exe")
# ]
#
# PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
#
# options = {
#     'build_exe': {
#         "packages": ["tkinter", "openpyxl"],
#         # "includes": ["numpy.core._methods"],
#         "excludes": [],
#         'include_files': [
#             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
#             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
#          ]
#     }
# }
#
# setup(name='RaceAppCSV',
#       version='1.0',
#       description='RaceApp CSV Beautifier',
#       options=options,
#       executables=executables, requires=['cx_Freeze', 'openpyxl']
#       )
# """
