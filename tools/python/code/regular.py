# import re
# pattern = r"(ab)cd(ef)"
# s = "abcdefghijkabcdef"
# #re模块直接调用
# l=re.findall(pattern,s)
# print(l)
# #compile对象调用
# regex = re.compile(pattern)
# print(dir(regex))
# l = regex.findall(s,1)
# print(l)

# l = re.split(r"\s+","Hello world China")
# print("split():",l)

# s = re.subn(r"\s+",'#',"Hello world China byebye",2)
# print(s)

# s = re.subn(r"\s+",'#',"Hello world China byebye")
# print(s)

# it = re.finditer(r'\d+','2008-2018 10nian,\
# 	中国发生了翻天覆地的变化')
# for i in it:
# 	print(i.group())

# obj = re.fullmatch(r'\w+','abcdef123')
# print(dir(obj))      #没匹配到时返回none，none没group会报错

# obj = re.match(r'foo','foo,food on the table')
# print(obj.group())

