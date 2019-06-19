import random
import string

#电话号码生成
class RandomPhone(object):
    #电话号码生成
    def phone(self):
        num_start = ['180', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end + '\n'
        return res


