import argparse
import time
import pyperclip
import pyautogui

"""
Usage:
Ctrl+C row in MS Excel or LibreOffice Calc
Set cursor on the first field in the web form
pycopypaste [-v] [-q] [-p <TIME>] -s <SCRIPT>

-v - verbose mode
-p - pause in sec
-s - script to execute
-q - prompt query to confirm operation

. - skip data column from Excel/Calc without changing focused web-form gui element
a - Switch to previous window (Alt+Tab)
b - Backspace
d - Del
e - Enter
r - move to the previous web-fortm gui element (Shift+Tab)
s - skip web-form gui element (Tab)
t - insert as plain text (Ctrl+V)
с - set checkbox (1 - toggle checkbox, otherwise - skip) (Space)

Example:
    python3 pycopypaste -s "atscsrrtstscsstststscststscsts.tststscscscscststststst"
"""
parser = argparse.ArgumentParser(
                    prog='pycopypaste',
                    description='pycopypaste v0.2. Automates Copy-Paste routine',
                    epilog='License: GNU General Public License')

parser.add_argument('-s', '--script', required = True)
parser.add_argument('-v', '--verbose', action = 'store_true')
parser.add_argument('-p', '--pause', type = float, default = 0.0)
parser.add_argument('-q', '--query', action = 'store_true')
args = parser.parse_args()

if (args.query):
    input('Press Enter when ready...')

excel_line = pyperclip.paste()
val_list = excel_line.split('\t')

type_list = args.script

elem_val = ''

for elem_type in type_list:
    if (args.verbose):
        print(elem_type, end=": ")

    if (elem_type == 'a'):
        pyautogui.hotkey('alt', 'tab')
    elif (elem_type == 'b'):
        pyautogui.hotkey('backspace')
    elif (elem_type == 'd'):
        pyautogui.hotkey('delete')
    elif (elem_type == 'e'):
        pyautogui.hotkey('enter')
    elif (elem_type == 's'):
        pyautogui.hotkey('tab')
    elif (elem_type == 'r'):
        pyautogui.hotkey('shift', 'tab')
    elif (len(val_list) <= 0):
        print('No data left in clipboard')
        break
    else:

        elem_val = val_list.pop(0)

        if (args.verbose):
            print(elem_val, end = '')

        if (elem_type == '.'):
            continue
        elif (elem_type == 'c'):
            if (elem_val == '1'):
                pyautogui.hotkey(' ')
        elif (elem_type == 't'):
            pyperclip.copy(elem_val)
            pyautogui.hotkey('ctrl', 'v')
        
    if (args.verbose):
        print()
    time.sleep(args.pause)

pyperclip.copy(excel_line)
