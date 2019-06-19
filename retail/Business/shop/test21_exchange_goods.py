import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.addMember.randomMember import RandomMember
from tool.time.nowTime import addTime
from tool.time.loadingTime import LoadTime
from tool.time.randomPhone import RandomPhone
from wholesale.group.procurement.login import Login

url = Login.location(1)
addname = Login.name(1)
addpwd = Login.password(1)
me = RandomMember.member_name(1)
sfz = RandomMember.member_sfz(1)
are = RandomMember.member_area(1)
ph = RandomPhone.phone(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
number = RandomGoods.import_number(1)

# 零售换货
def test21():
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
        name.send_keys(addname)

        # 输入密码
        pwd = driver.find_element_by_id('pwd')
        pwd.click()
        pwd.clear()
        pwd.send_keys(addpwd)

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
        print('test21:进入零售→店铺→前台业务→零售换货')
        time.sleep(time1)

        # 点击零售换货
        driver.find_element_by_link_text('零售换货').click()
        time.sleep(time2)

        driver.find_element_by_link_text('新增').click()
        time.sleep(time2)

        # 选择业务导购
        driver.find_element_by_xpath('//*[@id="sales"]/div/div/div[1]').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[3]/div//ul/li[1]').click()
        time.sleep(time1)

        # 输入备注
        bz = driver.find_element_by_xpath('//*[@id="comment"]')
        bz.click()
        bz.clear()
        bz.send_keys("换货" + addTime())
        #点击会员信息框
        driver.find_element_by_xpath('//*[@id="vip"]/div/div/div[1]').click()
        time.sleep(time1)
        #输入会员名字
        driver.find_element_by_xpath('//*[@id="vip"]/div/div/div[2]/div/input').send_keys(number)
        time.sleep(time2)
        #选择搜索出来的第一个会员
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
        time.sleep(time1)

        # 点击换回商品框
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div[1]').click()
        time.sleep(time1)
        # 输入商品名字
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(number)
        time.sleep(time2)
        # 选择搜索出来的第一个商品
        driver.find_element_by_xpath('/html/body/div[5]/div/div//ul/li[1]').click()
        time.sleep(time1)

        # 点击换出商品框
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[3]/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(time1)
        # 输入商品名字
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[3]/div[1]/div/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(number)
        time.sleep(time2)
        # 选择搜索出来的第一个商品
        driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[1]').click()
        time.sleep(time1)

        # 弹窗商品选择
        driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label/span/input').click()
        #确认
        driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        # 获取应收金额
        exchange_price = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div/div/div/div[3]/div[2]/strong').text
        time.sleep(time1)
        # 现金支付输入
        xjzf = driver.find_element_by_xpath('//*[@id="cash"]')
        xjzf.click()
        xjzf.send_keys(exchange_price)
        time.sleep(time1)
        # 保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time1)
        print('换货成功')

    except:
        print('零售订货异常')

    finally:
        driver.close()
