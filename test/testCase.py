import unittest
from retail.Business.goods.test7_goods_data import test7
from retail.Business.goods.test8_goods_attribute import test8
from retail.Business.member.test5_member_message import test5
from retail.Business.member.test6_member_grade import test6
from retail.Business.money.test2_add_money import test2
from retail.Business.money.test3_expend_money import test3
from retail.Business.procurement.test15_add_shop import test15

from retail.Business.procurement.test16_return_shop import test16
from retail.Business.shop.test18_shoping import test18
from retail.Business.shop.test19_sales_return import test19
from wholesale.group.goods.test114_goods_message import test114
from wholesale.group.goods.test115_goods_attribute import test115
from wholesale.group.manufacturer.test107_manufacturer import test107
from wholesale.group.manufacturer.test108_sales_return_set import test108
from wholesale.group.member.test109_member_message import test109
from wholesale.group.member.test110_member_grade import test110
from wholesale.group.money.test102_make_money import test102
from wholesale.group.money.test103_expend_money import test103
from wholesale.group.procurement.test117_add_shop import test117
from wholesale.group.procurement.test118_return_shop import test118
from wholesale.group.store.test127_delivery import test127
from wholesale.group.wholesaleGoods.test123_wholesale_goods import test123
from wholesale.setting.setup.test184_person import test184


class Test(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')

    def test_002(self):
        # 日常收入
        test2()
    def test_003(self):
        # 日常支出
        test3()
    def test_005(self):
        # 会员管理
        test5()
    def test_006(self):
        # 会员等级
        test6()
    def test_007(self):
        # 商品资料
        test7()
    def test_008(self):
        # 属性管理
        test8()
    def test_015(self):
        # 采购入库
        test15()
    def test_016(self):
        # 采购退货
        test16()
    def test_018(self):
        # 零售订单
        test18()
    def test_019(self):
        # 零售退货
        test19()

    def test_102(self):
        #日常收入
        test102()
    def test_103(self):
        #日常支出
        test103()
    def test_107(self):
        #厂商信息
        test107()
    def test_108(self):
        #退货设置
        test108()
    def test_109(self):
        #客户信息
        test109()
    def test_110(self):
        #客户等级
        test110()
    def test_114(self):
        #商品资料
        test114()
    def test_115(self):
        #商品属性
        test115()
    def test_117(self):
        #采购入库
        test117()
    def test_118(self):
        #采购退货
        test118()
    def test_123(self):
        #批发发货
        test123()
    def test_127(self):
        #批发订单
        test127()
    def test_184(self):
        #员工基础信息
        test184()






# class Test2(unittest.TestCase):
#
#     def test_001(self):
#         print('201')
#
#     def test_002(self):
#         print('202')

if __name__ == '__main__':
    # unittest.main()

    # 创建测试套件
    suit = unittest.TestSuite()
    # 定义一个测试用例列表
    case_list= ['test1','test2']
    for case in case_list:
        suit.addTest()

    # 运行测试用例，verbosity=2为每一个测试用例输出报告,run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)


# 1.unittest.main()运行时，框架自动寻找TestCase子类，并且运行
# 2.在TestCase类中，只把以test开头的方法当做测试用例，然后执行
# 3.setUp()用于初始化一些参数，在测试用例执行前自动被调用，tearDown()用于清理，在测试用例执行后被调用