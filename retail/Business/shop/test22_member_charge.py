import time

from selenium import webdriver

from tool.random.randomGoods import RandomGoods
from tool.addMember.randomMember import RandomMember
from tool.time.nowTime import addTime
from tool.time.loadingTime import LoadTime
from tool.time.randomPhone import RandomPhone
from wholesale.group.procurement.login import Login

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
me = RandomMember.member_name(1)
sfz = RandomMember.member_sfz(1)
are = RandomMember.member_area(1)
ph = RandomPhone.phone(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
number = RandomGoods.import_number(1)
money = RandomGoods.shop_price(1)

# 零售订单
def test22():
    try:
        # r"D:\Python36-32\chromedriver.exe"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(url)
        # 输入账号
        name = driver.find_element_by_id('user')
        name.click()
        name.clear()
        name.send_keys(login_name)

        # 输入密码
        pwd = driver.find_element_by_id('pwd')
        pwd.click()
        pwd.clear()
        pwd.send_keys(login_pwd)

        # 登陆
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()

        # 零售业务
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button[1]').click()

        # 进入店铺
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
        time.sleep(time1)

        # 前台业务
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[7]/div/span/span').click()
        print('test18:进入零售→店铺→前台业务→会员充值')
        time.sleep(time1)

        # 点击会员充值
        driver.find_element_by_link_text('会员充值').click()
        time.sleep(time2)

        driver.find_element_by_link_text('新增').click()
        time.sleep(time2)

        # 选择会员
        driver.find_element_by_xpath('//*[@id="member_code"]/div/div/div[1]').click()

        # 输入会员名字
        driver.find_element_by_xpath('//*[@id="member_code"]/div/div/div[2]/div/input').send_keys(number)
        time.sleep(time1)
        member_name = driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[1]')
        member_name.click()
        hy_name = member_name.text

        # 充值金额
        driver.find_element_by_xpath('//*[@id="amount"]').send_keys(money)

        # 赠送金额
        driver.find_element_by_xpath('//*[@id="gifts_price"]').send_keys(number)

        # 赠送积分
        driver.find_element_by_xpath('//*[@id="gifts_score"]').send_keys(number)


        # 输入备注
        bz = driver.find_element_by_xpath('//*[@id="comment"]')
        bz.click()
        bz.clear()
        bz.send_keys("充值" + addTime())

        #保存
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time2)
        try:
            #取消打印单据
            driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
            print('会员:' + hy_name + "充值" + money + ':元,  赠送' + number + ':元','赠送' + number + ':积分',"\n会员充值功能正常\n ")
            time.sleep(time1)
        except:
            driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
            print('会员:' + hy_name + "充值" + money + ':元,  赠送' + number + ':元', '赠送' + number + ':积分', "\n会员充值功能正常\n ")
            time.sleep(time1)

        # 搜索输入
        bz = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/div[2]/div/span/input')
        bz.click()
        bz.clear()
        bz.send_keys(number)

        # 查询
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)
        print('会员查询正常')
    except:
        print('会员充值异常')
    finally:
        driver.close()
