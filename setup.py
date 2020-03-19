#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from cx_Freeze import *
from bin import __version__, ABOUTPROGRAM, PROGRAM_NAME
from bin.license import information
from os import curdir, sep

app_title = PROGRAM_NAME
main_python_file = "support-client.py"
icon = curdir+sep+"bin"+sep+"image"+sep+"support-client.ico"
copyright = information

include_files = [r'C:\Python36\DLLs\tcl86t.dll', r'C:\Python36\DLLs\tk86t.dll', "bin", "support-client.ico",
                 "LICENSE.txt", "config.json"]
#excludes = ["backup", "temp", "html", "email", "http", "logging", "unittest", "urllib"]
excludes = []
packages = []

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",                  # Shortcut
     "DesktopFolder",                    # Directory_
     "Support Client",                   # Name
     "TARGETDIR",                        # Component_
     "[TARGETDIR]support-client.exe",    # Target
     None,                               # Arguments
     ABOUTPROGRAM,                       # Description
     None,                               # Hotkey
     "support-client.ico",               # Icon
     None,                               # IconIndex
     None,                               # ShowCmd
     'TARGETDIR'                         # WkDir
     )
]

msi_data = {'Shortcut': shortcut_table}
# bdist_msi_options = {'data': msi_data}
bdist_msi_options = {
    'upgrade_code': '{C1168458-7459-4B4F-85A7-8B4D0387D17C}',
    'data': msi_data
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
    os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'
else:
    base = None

setup(
    name=app_title,
    description=ABOUTPROGRAM,
    version=__version__,
    url="https://www.bailey-solution.com",
    license='MIT',
    author='Bailey Solution',
    author_email='guenter.bailey@bailey-solution.com',
    options={'build_exe': {'packages': packages, 'include_files': include_files, 'excludes': excludes,
                           'include_msvcr': True, 'optimize': 2, 'includes': packages},
             'bdist_msi': bdist_msi_options},
    executables=[Executable("support-client.py", base=base)]
)
