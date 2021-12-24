import re
 
 # 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('abc'))
    return str(value * 2)
def test():
    pass
s = 'A23G4HFD567'
print(re.sub('(?P<abc>\d+)', double, s))
