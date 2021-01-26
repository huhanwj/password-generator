import string, random
src_upp = string.ascii_uppercase
src_let = string.ascii_lowercase
src_num = string.digits
lis = []
count = input('请输入次数：').strip()


# for 循环实现（产生密码数可能不足）
for i in range(int(count)):
    print(i)
    # 先随机定义3种类型各自的个数（总数为8）
    upp_c = random.randint(1, 6)
    low_c = random.randint(1, 8-upp_c - 1)
    num_c = 8 - (upp_c + low_c)
    # 随机生成密码
    password = random.sample(src_upp, upp_c)+random.sample(src_let, low_c)+random.sample(src_num, num_c)
    # 打乱列表元素
    random.shuffle(password)
    # 列表转换为字符串
    new_password = ''.join(password)+'\n'
    if new_password not in lis:
        lis.append(new_password)
with open('password.txt', 'w') as fw:
    fw.seek(0)
    fw.writelines(lis)
fw.close()


# while 循环实现（只有密码不重复才+1）
j=0
while j< int(count):
    print(j)
    upp_c = random.randint(1, 6)
    low_c = random.randint(1, 8 - upp_c - 1)
    num_c = 8 - (upp_c + low_c)
    # 随机生成密码
    password = random.sample(src_upp, upp_c) + random.sample(src_let, low_c) + random.sample(src_num, num_c)
    # 打乱列表元素
    random.shuffle(password)
    # 列表转换为字符串
    new_password = ''.join(password) + '\n'
    if new_password not in lis:
        lis.append(new_password)
        j += 1
with open('password.txt', 'w') as fw:
    fw.seek(0)
    fw.writelines(lis)
fw.close()