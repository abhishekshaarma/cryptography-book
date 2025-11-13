from latextool_basic import *
p = Plot()
m00 = [['$x \pmod{26}$']]
m10 = [['%s' % i] for i in range(26)]
m01 = [['$x^{-1} \pmod{26}$']]
m11 = [['None']] + [[''] for i in range(25)]
M = [[m00, m01],
     [m10, m11]]
N = table3(p, M, width=3, height=0.6)
print(p)

