# 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
f = s[::-1]
print('翻转后的数组:',f)

# 翻转后的数组拼接成字符串
j = ''.join([str(i) for i in f])
print('翻转后的数组拼接成字符串:', j)

# ⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）
q = j[2:8]
print('⽤字符串切⽚的⽅式取出第三到第⼋个字符:',q)

# 将获得的字符串进⾏翻转
ff = q[::-1]
print('将获得的字符串进⾏翻转:',ff)

# 将结果转换为 int 类型
ii = int(ff)
print('将结果转换为 int 类型:',ii)

# 分别转换成⼆进制，⼋进制，⼗六进制
print('⼆进制:',bin(ii))
print('八进制:',oct(ii))
print('十六进制:',hex(ii))