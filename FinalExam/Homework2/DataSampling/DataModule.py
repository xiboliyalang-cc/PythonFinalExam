import random
import string
import time


class DataModule:
    def __init__(self, int_value=0, float_value=0, str_value=0, tuple_value=0):
        self.int_value = int_value
        self.float_value = float_value
        self.str_value = str_value
        self.tuple_value = tuple_value

    def __call__(self, func):
        def wrapper(**kwargs):
            # 生成随机数据结构
            print("Generating random data structure...")
            data = self.generate_data_structure(**kwargs)

            return data

        return wrapper

    def generate_data_structure(self, **kwargs):
        data = {}
        if 'int' in kwargs:
            data['int'] = self.generate_random_int(kwargs['int'])
        if 'float' in kwargs:
            data['float'] = self.generate_random_float(kwargs['float'])
        if 'str' in kwargs:
            data['str'] = self.generate_random_string(kwargs['str'])
        if 'tuple' in kwargs:
            data['tuple'] = self.generate_random_tuple(kwargs['tuple'])
        return data

    def generate_random_int(self, n):
        # 生成随机整数
        # 实现具体的生成逻辑
        return [random.randint(1, 100) for _ in range(n)]

    def generate_random_float(self, n):
        # 生成随机浮点数
        # 实现具体的生成逻辑
        return [random.uniform(0, 1) for _ in range(n)]

    def generate_random_string(self, n):
        # 生成随机字符串
        # 实现具体的生成逻辑
        return ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(n)]

    def generate_random_tuple(self, n):
        # 生成随机元组
        # 实现具体的生成逻辑
        return [(random.randint(1, 10), random.uniform(0, 1), random.choice(string.ascii_letters)) for _ in range(n)]


@DataModule(int_value=5, float_value=3, str_value=4, tuple_value=2)
def dataSampling(**kwargs):
    return kwargs


# 调用示例
data = dataSampling(int=3, float=2, str=1, tuple=2)
print("Generated data structure:", data)
