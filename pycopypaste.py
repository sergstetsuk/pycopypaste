import argparse
import pyperclip
import pyautogui

"""
Usage:
Ctrl+C row in MS Excel or LibreOffice Calc
Set cursor on the first field in the web form
pycopypaste -s <paste_flow_script>

a - Alt+Tab
t - insert as plain text
с - set checkbox (1 - toggle checkbox, otherwise - skip)
s - skip web-form gui element
. - skip data column from Excel/Calc without changin focused web-form gui element

Example:
    python3 pycopypaste -s "atttctttcttct.tttccccttttt"
"""
excel_line = pyperclip.paste()
val_list = excel_line.split('\t')

parser = argparse.ArgumentParser(
                    prog='pycopypaste',
                    description='Automates Copy-Paste routine',
                    epilog='License GNU GPL')

parser.add_argument('-s', '--script', required = True)
parser.add_argument('-v', '--verbose', action = 'store_true')
args = parser.parse_args()

type_list = args.script

elem_val = ''

for elem_type in type_list:
    if (elem_type == 'a'):
        pyautogui.hotkey('alt', '\t')
        continue
    if (elem_type == 's'):
        pyautogui.hotkey('\t')
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

    pyautogui.hotkey('\t')

pyperclip.copy(excel_line)
