"""
1.3 表达式、运算符和优先级
【逻辑运算】
    not
    and
    or
    is
    is not
    ==
    !=
    (注: <>不可用)
【比较运算】
    >
    <
    >=
    <=
【算数运算】
    + - + /
    // 整除
    % 模运算
    ** 乘方、开根号
【位运算】
    ~ 非
    & 与
    | 或
    ^ 异或（注意：乘方是**）
    <<
    >>
【序列运算符】
    s[i]
    s[i: j] 索引为[i, j)的切片
    s[i: j: k] 切片，步长为k，步长可为负数
    s + t 序列的连接
    k * s 序列s连接k次

    val in s （可以用于判断字符串中的子串） "amp" in "example"
    val not in s

    注：
    s[i] = val
    del s[i]
    del s[i: j]
    s[1: 3] = [2, 3]
    s[1: 3] = [999, 999, 999, 999, 999] (和pandas不太一样)

【集合运算符】
    key in s
    key not in s
    s1 == s2
    s1 != s2
    s1 <= s2 （s1是s2的子集）
    s1 < s2 （s1是s2的真子集）

    s1 | s2 并集（条件或）
    s1 & s2 交集（条件与）
    s1 - s2 差集
    s1 ^ s2 对称差分（补集的并集）

    注意！在使用set定义集合之后，顺序已经按照系统默认进行确定
【字典运算符】
    d[key]
    d[key] = value
    del d[key]

    key in d （检查键值是否在字典里）
    key not in d

    d1 == d2
    d1 != d2

【扩展赋值运算】
    b = [1, 2]
    a = b
    a += [2, 3] （会加到b上）
    a = a + [5, 6] （不会加到b上）
`   # 对于list有这个规律，对于普通的数字运算则没有

python支持多级赋值和链式表达式
    a = b = 0
    0 <= a + b <= 10

1.4 控制流程
    if
    elif
    elif
    else

    if response: (等价于不为空, ""或者None)
    注意，不能用这种方法判断np.nan

    while condition:
        body

    for element in iterable:
        body

    其中，iterable可以是list, tuple, str, set, dict, file

    break和continue

1.5 函数

    函数：无需了解特定类的内容或该类的实例
    方法：某一个类实例化后的成员函数

    调用函数时，会创建专用的活动记录来存储相关信息，【局部作用域】的命名空间与其他作用域的变量不冲突

    可以有多个return

    形参和值参
    变参：一个参数时可变对象时（比如list），一些交互也许会改变状态
    如：data.append(1)
    def scale(l, factor):
        for i in range(len(l)):
            l[i] *= factor

    a = [1, 2, 3]
    scale(a, 2)
    print(a)

    # 注意，l[i] = l[i] * factor和l[i] *= factor的不同

    默认参数值，如:
    def foo(a, b=2, c=10):
    注意，不允许出现def foo(a, b=1, c)的情况。有默认参数则必须放在后面
    def foo(a, b=None):
        if b:
            return a + b
        return a

    默认【按顺序调用】如foo(5)默认给a参数5
    也可以【按关键词参数调用】如foo(c=5)

    函数的参数也可以传入一个函数
    如：max(-1, -2, key=abs)
    df.groupby("stkcd").apply(calc)等等

    【python的内置函数】
    ord("A")
    # 65
    chr(65)
    # "A"

    abs(a)
    divmod(a, b) 返回整除和求余的结果
    pow(x, y) 等价于 x ** y
    round(val, d)
    sum(iterable, a)
        把iterable相加，在加上a

    print
        sep=, end=,
    input
        str.split()

    【文件的读写】
    f = open("sample.txt")
    默认"r" 只读
    "w" 可以写操作（覆盖）
    "a" 追加

    f.read()
    f.read(k)
    f.readline()
    f.readlines()
    for line in f:
    f.seek(k)
    f.tell()
    f.write(s)
    f.writelines(s)
    print(s, file=f)

    f.close()

    【抛出异常】
    raise Exception("哈咯")
        会有更多详细的异常类 pp.23

    def sqrt(x)
        if isinstance(x, (int, float)):
            raise TypeError("必须是数值")
        elif x < 0:
            raise ValueError("不能是负数")
        ...

    【捕捉异常】
        1. 三思而后想：积极地思考 异常的情况
        2. 遇到异常应该如何处理

    try:
        ...
    except Exception:
        print(...)
        raise

    可以except一个具体的异常类，如
    except ValueError:
    except EOFError:

1.8  迭代器与生成器
    字典支持的方法
        .keys() 返回键的迭代器
        .values() 返回值的迭代器
        .items() 返回元组的迭代器

    d = {"A": 1, "B": 2, "C": 88}
"""
a = 1
b = a
print(a is b)

print(1 << 2)

a = [1, 2, 5]
print(3 * a)

a = [i for i in range(10)]
print(a[9: 1: -1])
# 步长k为负, 但是i和k也要颠倒过来

a[1: 3] = [99, 99]
print(a)
del a[1: 3]
a[1: 3] = [999, 999, 999, 999, 999]

print("amp" in "example")
print([1, 2] in [1, 2, 3])
print([1, 2] in [1, 2, 3, [1, 2]])
print([1, 2] <= [1, 2, 3])