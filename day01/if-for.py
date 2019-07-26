# -*- coding: UTF-8 -*- #
# 掷色子决定做什么
from random import randint

face = randint(1, 6)
if face == 1:
    result = u'唱首歌'
elif face == 2:
    result = u'跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)


# 用for循环实现1~100之间的偶数求和
sumd = 0
for x in range(1, 101):
    if x % 2 == 0:
        sumd += x
print(sumd)

print(sum([0,1,2], 2))

print(dict(a='a',b='b'))

