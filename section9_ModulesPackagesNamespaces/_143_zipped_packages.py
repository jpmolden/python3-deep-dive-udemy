import sys
from pprint import pprint
pprint(sys.path)

# Tell python to loook in the zip too
sys.path.append('./shared_zipped.zip')
pprint(sys.path)

import shared_zipped
