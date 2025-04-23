import sys
from cx_Freeze import *

base = None
if sys.platform=='win32':base='Win32GUI'

opts = { 'include_files': ['sim1.PNG','sim2.PNG','sim3.PNG','sim4.PNG','sim5.PNG','sim6.PNG'], 'includes':['re']}

setup( name = 'Therapy Robot',
       version = '1.0',
       description = 'A mental health helpful AI',
       author = 'George Peter Thom',
       options = {'build_exe':opts},
       executables=[Executable('AI_Therapist.py',base=base,shortcut_name='AI Therapist',shortcut_dir="DesktopFolder",)])
