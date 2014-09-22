import sys
if len(sys.argv) != 3:
    print('usage: python3 solution.py OP1 OP2')
else:
    OP1 = sys.argv[1]
    OP2 = sys.argv[2]
    print(float(OP1)+float(OP2))