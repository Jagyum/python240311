# DemoOSPath.py
import random

print(random.random())
print(random.random())
print("--randrange--")
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("--sample--")
print(random.sample(range(20),10))
print(random.sample(range(20),10))

print("--lotto--")
lotto = random.sample(range(1,46),6)
print(lotto)
# random.shuffle(lotto)
# print(lotto)


# 파일과 폴더 다루기
from os.path import *
print(abspath("python.exe"))
print(basename("c:\\work\\python.exe"))
if exists("c:\\python310\\python.exe"):
    print("파일 있음")
else:
    print("파일 없음")

print("-----------------")
print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))

from os import *
print("운영체제이름:{0}".format(name))

print("-----------------")
import glob
print("현재폴더:{0}".format(getcwd()))
chdir("..")
chdir("c:\\work")
lst = glob.glob("*.py")
for item in lst:
    print(item)
