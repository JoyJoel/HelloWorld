import sys
import traceback  # 回溯对象,快速定位问题根源

from pprint import pprint

pprint(dir(sys))

try:
    raise KeyError
except:
    print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
