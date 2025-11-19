import argparse
import time
import pyperclip
import pyautogui

"""
Usage:
Ctrl+C row in MS Excel or LibreOffice Calc
Set cursor on the first field in the web form
pycopypaste [-v] [-p 0.2] -s <paste_flow_script>

-v - verbose mode
-p - pause in sec
-s - script to execute

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
    python3 pycopypaste -s "atcrrttcstttcttct.tttccccttttt"
"""
excel_line = pyperclip.paste()
val_list = excel_line.split('\t')

parser = argparse.ArgumentParser(
                    prog='pycopypaste',
                    description='pycopypaste v.0.1. Automates Copy-Paste routine',
                    epilog='License: GNU General Public License')

parser.add_argument('-s', '--script', required = True)
parser.add_argument('-v', '--verbose', action = 'store_true')
parser.add_argument('-p', '--pause', type = float, default = 0.2)
args = parser.parse_args()

type_list = args.script

elem_val = ''

for elem_type in type_list:
    if (elem_type == 'a'):
        pyautogui.hotkey('alt', 'tab')
        continue
    if (elem_type == 'b'):
        pyautogui.hotkey('backspace')
        continue
    if (elem_type == 'd'):
        pyautogui.hotkey('delete')
        continue
    if (elem_type == 'e'):
        pyautogui.hotkey('enter')
        continue
    if (elem_type == 's'):
        pyautogui.hotkey('tab')
        continue
    if (elem_type == 'r'):
        pyautogui.hotkey('shift', 'tab')
        continue
    if (len(val_list) <= 0):
        print('No data left in clipboard')
        break

    elem_val = val_list.pop(0)

    if (args.verbose):
        print(elem_type, elem_val)

    if (elem_type == '.'):
        continue
    elif (elem_type == 'c'):
        if (elem_val == '1'):
            pyautogui.hotkey(' ')
    elif (elem_type == 't'):
        pyperclip.copy(elem_val)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(args.pause)

    pyautogui.hotkey('tab')

pyperclip.copy(excel_line)
