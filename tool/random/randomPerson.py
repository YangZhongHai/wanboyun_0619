import random
import string

#员工生成类
class RandomStaff(object):
    # 员工编号
    def person_id(self):
        num_start = ['11', '22', '44', '33']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    #员工姓名
    def person_name(self):
        num_start = ['杰伦', '志玲', '后羿', '德玛']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 4))
        res = start + end
        return res

    #员工身份证
    def person_IDcard(self):
        res = ('510503199409223478')
        return res

    #员工籍贯
    def person_place(self):
        num_start = ['成都', '北京', '上海', '绵阳', '泸州', '广元']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 2))
        res = start + end
        return res

    # 公积金社保号码
    def person_member(self):
        num_start = ['11', '22', '44', '33']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 10))
        res = start + end
        return res

    #通讯地址
    def person_area(self):
        res = ('成都市天府新区天府菁蓉大厦')
        return res