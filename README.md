# pycopypaste
Configurable automation tool for multiple copypaste operations according to regex-style template script.

The tool parses the Clipboard content as a tab-separated columns list (expected a line from MS Excel or LibreOffice Calc, copied to the Clipboard) and processes them one-by-one according to the template script commands.

Usage:
```
python3 pycopypaste.py [-v] [-q] [-t <TIME>] -s "<SCRIPT>"
```
-v - verbose output to console

-p TIME - pause after Ctrl+V in seconds. Default 0

-s SCRIPT - copy-paste sequence script

-s - Wait for confirmation before start

Template SCRIPT commands:
-  a - perform Alt+Tab to switch back to previous window
-  t - perform Ctrl+V to insert text data. Press Tab to move to next UI control.
-  c - perform Space press if value is 1. Skip otherwise. Press Tab afterwards.
-  s - skip operation (Do nothing). Press Tab to move to next UI control.
-  r - move to the previous UI control as Shift+Tab.
-  . - skip data column without moving to the next UI control.
-  b - press BackSpace
-  d - press Delete
-  e - press Enter

Example usage:
```
python3 pycopypaste.py -s "atcrrttctttcttct.tttccccttttt"
```

# Installation
In general the tool does not need installation. Python installation should meet requirements.txt

```
python -m pip -r requirements.txt
```

# Build standalone binary
```
pyinstaller pycopypaste.py
```

The resulting prebuilt binary and dependencies are in dist/ directory
