import random
import string

#商品资料随机生成类
from random import randint


class RandomGoods(object):
    # 商品款号
    def goods_number(self):
        num_start = ['1阿迪', '2椰子', '3耐克', '4李林', '5高仿']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 商品名称
    def goods_name(self):
        num_start = ['1上衣', '2短裤', '3泳衣', '4鞋子', '5袜子']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 商品类别
    def goods_type(self):
        num_start = ['L类别', 'B类别', 'A类别', 'W类别']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 面料
    def goods_materials(self):
        num_start = ['P面料', 'M面料', 'Q面料', 'R面料']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 里料
    def goods_liliao(self):
        num_start = ['E里料', 'B里料', 'Z里料', 'X里料']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 计量单位
    def goods_unit(self):
        num_start = ['H套', 'A件', 'Q个', 'F支']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 颜色
    def goods_colour(self):
        num_start = ['V黄色', 'C白色', 'G粉色', 'F紫色']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 季节
    def goods_season(self):
        num_start = ['F春天', 'X夏天', 'Q秋天', 'D冬天']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 洗涤规格名称
    def goods_xidi(self):
        num_start = ['Y手洗', 'X轻柔', 'Q洗衣', 'D干洗']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res
    # 洗涤规格排序序号
    def goods_order(self):
        num_start = ['1', '2', '3', '4']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 零售商品指导定价
    def price(self):
        res = ('100')
        return res

    # 零售价格
    def retail_price(self):
        res = ('50')
        return res
    #商品品牌
    def brand(self):
        num_start = ['S品牌', 'L品牌', 'S品牌', 'A品牌']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    def norm(self):
        num_start = ['AA', 'BB', 'CC', 'SS']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    # 采购支付货款
    def shop_price(self):
        num_start = ['1', '2', '3', '4']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 1))
        res = start + end
        return res

    # 采购费用
    def shop_transportation_price(self):
        num_start = ['1', '2', '3', '4']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 1))
        res = start + end
        return res

    # 输入商品选择商品数字
    def import_number(self):
        num_start = ['1', '2', '3']
        start = random.choice(num_start)
        res = start
        return res

    # 进货折扣
    def shop_zhekou(self):
        num_start = ['3', '4', '2', '5']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 1))
        res = start + end
        return res

    def random_number(self):
        res = randint(1, 100)
        return res

