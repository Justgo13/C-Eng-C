# -*- mode: python ; coding: utf-8 -*-
from pyzbar import pyzbar
from pathlib import Path

block_cipher = None


a = Analysis(['main.py'],
             pathex=['venv/Lib/site-packages/'],
             binaries=[],
             datas=[('venv\\Lib\\site-packages\\mediapipe\\modules', 'mediapipe\\modules')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# dylibs not detected because they are loaded by ctypes
a.binaries += TOC([
    (Path(dep._name).name, dep._name, 'BINARY')
    for dep in pyzbar.EXTERNAL_DEPENDENCIES
])

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )