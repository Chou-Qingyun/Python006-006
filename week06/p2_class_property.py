class Human(object):
    # 静态字段
    live = True

    def __init__(self,name):
        # 普通字段
        self.name = name


man = Human('Adam')
woman = Human('Eve')

# 有静态字段，live属性
Human.__dict__
print(Human.__dict__)
Human.newattr = 1
# print(dir(Human))

# 有普通字段，name属性
print(man.__dict__)

# 显示object类的所有子类
print( ().__class__.__base__[0].__subclasses__() )

class Human2(object):

    # 人为不可修改
    _age = 18

    # 私有属性
    __fly = False

    # 魔术方法，不会自动改名
    # 如 __init__
