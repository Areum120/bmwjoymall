# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['run.py'],
             pathex=['C:\\Users\\웍스컴바인\\Desktop\\work\\bmwjoymall_rpa'],
             binaries=[],
             datas=[('./gui/*.ui','./gui'),
                    ('./gui/email_list.xlsx', './gui'),
                    ('./gui/listOfPartners.xlsx', './gui'),
                    ('./gui/listOfPartners_name.xlsx', './gui'),
                    ('./gui/sendRequest.xls', './gui'),
                    ],
             hiddenimports=['gui.rpa_thread',
                            'product_classification.convert_to_xlsx',
                            'product_classification.create_email_list',
                            'product_classification.excel_classification',
                            'product_classification.mailing_auto',],
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

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
