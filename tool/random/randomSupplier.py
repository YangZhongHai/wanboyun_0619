import random
import string

#供应商生成类
class RandomSupplier(object):
    # 供应商名字
    def supplier_name(self):
        num_start = ['A随机', 'B华润', 'C阿里', 'D山寨', 'E高仿']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 6))
        res = start + end
        return res
    #厂商名称
    def manufacturer_name(self):
        num_start = ['A厂商', 'B厂商', 'C厂商', 'D厂商', 'E厂商']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 5))
        res = start + end
        return res