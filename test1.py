import sys

print('================Python import mode==========================')
print('命令行参数为:')
print(sys.argv)
for i in sys.argv:
    print(i)
# print('\n python path is ', sys.path)

print(type(1), type(2.0), type(4+3j),type(True))