cd "C:\Users\Ruslan\.PyCharm2018.3*\config"
rmdir "eval" /s /q
del "options\options.xml"
reg delete "HKEY_CURRENT_USER\Software\JavaSoft\Prefs\jetbrains\pycharm" /f
