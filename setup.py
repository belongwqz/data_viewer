# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
setup(
    version='0.1.0',
    windows=[{'script': 'main.py', 'icon_resources': [(0, 'app.ico')]}],
    #console=[{'script': 'main.py', 'icon_resources': [(0, 'app.ico')]}],
    options={'py2exe': {
        'optimize': 2,
        'compressed': 1,
        'includes': [],
        'dll_excludes': ['w9xpopen.exe', 'MSVCP90.dll'],
        'bundle_files': 3
    }
    },
    data_files=['app.ico', 'zh_CN.qm' , ('imageformats', ['imageformats/qico4.dll']), ('sqldrivers', ['sqldrivers/qsqlite4.dll'])], requires=['PySide']
)
