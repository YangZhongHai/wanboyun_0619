import random
import string
import re

#会员生成类
class RandomMember(object):
    #会员名字
    def member_name(self):
        num_start = ['张杰', '夸父', '后羿', '李六', '哪吒']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 3))
        res = start + end
        return res
    #会员身份证
    def member_IDcard(self):
        res = ('510503199409223478')
        return res

    #会员所在地区
    def member_area(self):
        num_start = ['成都', '北京', '上海', '绵阳', '泸州', '广元']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 3))
        res = start + end
        return res

    #会员等级
    def member_level(self):
        num_start = ['白银', '黄金', '砖石', '星耀']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 3))
        res = start + end
        return res

    # 选择随机数
    def random_number(self):
        num_start = ['2', '1']
        start = random.choice(num_start)
        res = start
        return res

    # 提取数字
    def extract_number(self):
        totalCount = self
        totalCount = re.sub("\D", "", totalCount)
        return totalCount

