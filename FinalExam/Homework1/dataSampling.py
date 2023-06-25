import random
import string
import time


# args: datatype, num, length
def dataSampling(**kwargs):
    """
    name: CuiCan
    id: 2022103255
    :param args:
    :return:
    """
    try:
        # print("系统正在生成数据，请稍后...")
        # time.sleep(1)
        pass
    except ValueError:
        print("输入数据格式错误")
    else:
        result = []
        for dtype, num in kwargs.items():
            if dtype == 'int':
                item = random.choices(range(100), k=num)
                result.append(item)
            elif dtype == "float":
                item = [random.uniform(0, 100) for _ in range(num)]
                result.append(item)
            elif dtype == "str":
                item = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(num)]
                result.append(item)
            elif dtype == "tuple":
                item = [(random.randint(0, 100), random.uniform(0, 100),
                         ''.join(random.choices(string.ascii_letters + string.digits, k=10))) for _ in range(num)]
                result.append(item)
            else:
                continue

        return result

result = []
result = dataSampling(tuple = 3)

# if __name__ == '__main__':
#     print(dataSampling(tuple=3))


    # print("******************\n"
    #       "输入格式：\n"
    #       "1、整数：int, num, start, end\n"
    #       "2、浮点：float, num ,start, end\n"
    #       "3、字符串：str, num, length\n"
    #       "4、元组: tuple, num, length, group_num")
    # print(dataSampling(int,5,1,10))
    # print(dataSampling(float, 5, 1, 10))
    # print(dataSampling(str, 5, 10))
    # print(dataSampling(tuple,5,7,2))
    # print("选择要生成的项目：")
    # c = input()
    # pa = []
    # if c == '1':
    #     a,b,c=map(int,input('').split())
    #     print(dataSampling(int,a,b,c))

