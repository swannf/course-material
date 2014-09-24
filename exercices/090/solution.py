import sys
param = sys.argv
lparam = list(enumerate(param))
for i in lparam:
    print(i[0], i[1])
