#!C:\breachwall\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlparse','console_scripts','sqlformat'
__requires__ = 'sqlparse'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sqlparse', 'console_scripts', 'sqlformat')()
    )
