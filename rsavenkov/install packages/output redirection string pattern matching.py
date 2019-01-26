import sys

sys.stderr.write('Warning, log file not found starting a new one\n')

import re

all = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(all)