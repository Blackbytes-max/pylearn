# !/usr/bin/python3
while True:
    i = input("请输入您希望生成的数列的长度：")
    i = int(i)
    if i <= 0:
        print('请输入一个大于0的数。')
    else:
        break

a, b = 0, 1
count = 0
while count <= i:
    print(b)
    count += 1
    a, b = b, a + b
input()
exit()
