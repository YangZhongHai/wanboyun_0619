from selenium import webdriver
import time

from wanboyun.tool.addMember.randomMember import RandomMember
from wanboyun.tool.addPhone.addTime import addTime
from wanboyun.tool.addPhone.loadingTime import LoadTime
from wanboyun.tool.loginFile.login import Login


class Common(object):
    # 初始化
    def __init__(self):
        url = Login.location(1)
        loginname = Login.name(1)
        loginpwd = Login.password(1)
        tim = addTime()
        time1 = LoadTime.time1(1)
        time2 = LoadTime.time2(1)
        time3 = LoadTime.time3(1)
        fkr = RandomMember.member_name(1)

        # 创建浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)

        # 输入账号
        self.name = self.find_element_by_id('user')
        self.name.click()
        self.name.clear()
        self.name.send_keys(loginname)

        # 输入密码
        pwd = self.driver.find_element_by_id('pwd')
        pwd.click()
        pwd.clear()
        pwd.send_keys(loginpwd)

        # 登陆
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()

        # 零售业务
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button[1]').click()

    # 访问指定url
    def open_every(self):
        # 进入店铺
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()

        # 点击财务管理
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[2]/div[1]').click()
        print('test2:进入零售→店铺→财务管理→日常收入')
        time.sleep(self.time1)

        # 点击日常收入
        self.driver.find_element_by_xpath('//*[@id="finance$Menu"]/li[1]/a').click()
        time.sleep(self.time2)
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(self.time2)

        # 业务部门
        self.driver.find_element_by_xpath('//*[@id="department"]/div/div').click()
        time.sleep(self.time1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()

        # 款项名称
        self.driver.find_element_by_xpath('//*[@id="name"]/div/div').click()
        time.sleep(self.time1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[2]').click()

        # 收款人
        skr = self.driver.find_element_by_xpath('//*[@id="payee"]')
        skr.click()
        skr.send_keys(self.fkr)

        # 支付金额
        skr = self.driver.find_element_by_xpath('//*[@id="payment"]')
        skr.click()
        skr.send_keys('100')

        # 付款方式
        self.driver.find_element_by_xpath('//*[@id="method"]/div/div').click()
        time.sleep(self.time1)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[2]').click()

        # 业务员
        self.driver.find_element_by_xpath('//*[@id="salesman"]/div/div').click()
        time.sleep(self.time1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()

        # 备注
        bz = self.driver.find_element_by_xpath('//*[@id="comment"]')
        bz.click()
        bz.send_keys('自动备注' + self.tim)

        # 保存
        self.driver.find_element_by_xpath('//*[@role="tabpanel"]/div[2]/div/div/div/div/div[2]/div/button[2]').click()
        print('日常收入订单新建成功\n', '日常收入订单新增功能正常')
        time.sleep(self.time2)


    def close_driver(self):
        self.driver.quit()

    # 结束的时候清理了
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

# 判断文件是否自身执行，如果是则，执行之后的语句
if __name__ == '__main__':
    com = Common()
    com.open_every()

    com.close_driver()