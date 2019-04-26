# 被装饰函数没有参数时
def OuterFunction(func): #<---有且只有一个参数
    print('OuterFunction')
    func()
    def InnerFunction():
        print('InnerFunction')
    func()
    return InnerFunction

@OuterFunction
def Fcunction():
    print('Fcunction')

Fcunction() #<---效果如同：先func = OuterFunction(Fcunction)，然后func()
# Fcunction被传入OuterFunction内部，所以Fcunction与InnerFunction时存在于同一个命名空间之内的
# 被装饰函数不一定要进入内存函数中，开在外层函数内部(与内层函数同一命名空间)被执行
print('**************************************************')

# 被装饰函数有参数时
def OuterFunction1(func): #<---有且只有一个参数
    print('OuterFunction1')
    def InnerFunction1(str1): #<---形参的数量必须要与，被装饰函数的数量相一致
        print('InnerFunction1')
        func(str1)
    return InnerFunction1

@OuterFunction1
def Fcunction1(str1):
    print(str1)

Fcunction1('Fcunction1')# 被装饰函数有参数且外层函数return的是内存函数时，内层函数形参数量必须与传入被装饰函数的实参数量相一致

print('**************************************************')

def OuterFunction2(func): #<---有且只有一个参数
    print('OuterFunction2')
    def InnerFunction1(str2): #<---外层函数返回的是被装饰函数，内层函数的形参与被装饰函数调用时传入的实参毫无关系
        print('InnerFunction2')
    return func

@OuterFunction2
def Fcunction2(str2,str2_1):
    print(str2,str2_1)

Fcunction2('Fcunction2','Fcunction2_1')# 当外层函数return返回的被装饰函数时，内层函数形参数量与传入被装饰函数的实参数量无关，最后被装饰函数其实没有被修改过地运行而已，但外层函数中return前面的代码仍然会运行

print('**************************************************')

# 装饰器可以没有内层函数
def OuterFunction3(func): #<---有且只有一个参数
    print('OuterFunction3')
    return func

@OuterFunction3
def Fcunction2(str3,str3_1):
    print(str3,str3_1)

Fcunction2('Fcunction3','Fcunction3_1')# 当外层函数return返回的被装饰函数时，内层函数形参数量与传入被装饰函数的实参数量无关，最后被装饰函数其实没有被修改过地运行而已，但外层函数中return前面的代码仍然会运行

print('**************************************************')



'''
高度抽象的总结：
            1、被装饰器作为参数传入装饰器外层函数的形参位置
            2、装饰器外层函数return返回的内容必须要是可调用对象(可以使内层函数、被装饰函数，甚至是其他可调用对象)
            3、装饰器的外层函数return返回的是内层函数时：
                3.1内层函数的形参数量要与被装饰函数被调用时传入的实参数量一致
                3.2被装饰函数被调用时传入的实参传入装饰器的内层函数形参位置
            4、装饰器不一定要有内层函数

被装饰函数被调用时，如同以下伪代码顺序：
                        情况1：装饰器外层函数的return是内层函数
                                1、被装饰函数和被装饰函数调用时的实参被拆开
                                2、伪代码：装饰器外层函数(被装饰函数)
                                3、运行装饰器外层函数与内层函数之间的代码
                                4、伪代码：装饰器内层函数(被装饰函数的实参)
                                5、运行装饰器内层函数与外层函数return之间的代码
                                6、对装饰器外层函数return返回的内容(内层函数)进行调用，内层函数的形参数量要与被装饰函数被调用时传入的实参数量相一致
                        情况2：装饰器外层函数的return是被装饰函数
                                1、运行装饰器外层函数中return前面的代码仍然会运行
                                2、把被装饰函数调用的那段语句运行一次，即：return被装饰函数，不用写实参，会自动根据程序员写的被装饰函数调用的代码来运行，其实就是被装饰函数根本没有被装饰过一样
                        情况3：被装饰函数没有形参，其实是有形参的一种特殊形式，
                        情况4：装饰器可以没有内层函数，直接返回被装饰函数，意味着只是在被装饰函数运行前先运行其他代码，根本没有对被装饰函数进行装饰
'''