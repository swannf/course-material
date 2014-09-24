import sys
import operator
signs = {"+": operator.add,
         "-": operator.sub,
         "/": operator.truediv,
         "*": operator.mul,
         "%": operator.mod,
         "^": operator.pow}
p = sys.argv
if (isinstance(int(p[1]), int) and
        '.' not in p[1] and
        isinstance(int(p[3]), int) and
        '.' not in p[3] and
        p[2] in '/+-*%^'):
    if ('.' in p[1] or '.' in p[3]):
        print('input error')
    if p[2] == '/' and int(p[3]) == 0:
        print('input error')
    sol = signs[p[2]](int(p[1]), int(p[3]))
    print(sol)
else:
    print('usage: python3 ./solution.py a_n\
umber (an_operator +-*/%^) a_number')
