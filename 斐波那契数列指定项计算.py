# !/usr/bin/python3
while True:
    i = input("请输入您希望计算的项序号：")
    i = int(i)
    if i <= 0:
        print('请输入一个大于0的数。')
    else:
        break

a, b = 0, 1
count = 0
while count < i:
    a, b = b, a + b
    count += 1
print('斐波那契数列第',i,'项的值为',a)
input()
exit()
