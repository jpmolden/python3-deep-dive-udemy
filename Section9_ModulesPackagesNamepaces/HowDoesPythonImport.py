

# Import happens at runtime

import sys
from pprint import pprint as Print

print("Where is python installed:\n",sys.prefix)
print("W vhere is the C binaries located:\n",sys.exec_prefix)



print("\nOther Stuff:")
Print(sys.path)




