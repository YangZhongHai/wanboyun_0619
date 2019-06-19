import time
from selenium.webdriver import ActionChains   #鼠标双击模块
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.loginFile.login import Login
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
number = RandomGoods.import_number(1)
random_number = RandomMember.random_number(1)

# 零售订货
def test20():
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
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[1]').click()

    # 进入店铺
    driver.find_element_by_link_text('进入店铺').click()
    time.sleep(time1)

    # 前台业务
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[7]/div[1]/span/span').click()
    print('test19:进入零售→店铺→前台业务→零售退货')
    time.sleep(time1)

    # 零售订货
    driver.find_element_by_link_text('零售订货').click()
    time.sleep(time2)

    #查询
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    s1 = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[1]/strong').text
    s2 = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[2]/strong').text
    shop_money = RandomMember.extract_number(s1)
    singular = RandomMember.extract_number(s2)
    print('定 货 前: ' + singular + '件   '+ shop_money + '元   ')
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)
    # 选择业务导购
    driver.find_element_by_xpath('//*[@id="salesId"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time1)

    # 输入备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.clear()
    bz.send_keys("生成时间" + nowTime())
    #点击会员信息框
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/div[1]/div/div[1]/div[2]/div/span/div/div/div/div[1]').click()
    time.sleep(time1)
    #输入会员名字
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/div[1]/div/div[1]/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(random_number)
    time.sleep(time2)
    #选择搜索出来的会员
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[%s]' % random_number).click()

    # 添加商品
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/span/div/div/div/div/ul/li/div/input').click()
    time.sleep(time1)
    # 输入商品名字
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/span/div/div/div/div/ul/li/div/input').send_keys(random_number)
    time.sleep(time2)
    # 选择搜索出来的商品
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[%s]' % random_number).click()
    time.sleep(time2)
    # 弹窗商品选择
    gmsp = driver.find_element_by_xpath(
        '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]')
    # 鼠标双击选择
    ActionChains(driver).double_click(gmsp).perform()
    time.sleep(time2)
    # 获取应收金额
    ysje = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/span').text
    pay_money = ysje.split('.')[0]
    # 现金支付输入
    xjzf = driver.find_element_by_xpath('//*[@id="payment-method"]/div[1]/span/span/input')
    xjzf.click()
    xjzf.send_keys(pay_money)
    time.sleep(time2)
    # 保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time2)

    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print('订货成功')
    else:
        print(result_save + "\n订货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    s11 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[1]/strong').text
    s22 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[2]/strong').text

    shop_money1 = RandomMember.extract_number(s11)
    shop_money2 = int(shop_money) + int(pay_money)
    singular1 = RandomMember.extract_number(s22)
    singular2 = int(singular) + 1

    print('实际订货: 1件  ' + pay_money + '元\n')
    if singular2 == int(singular1) and shop_money2 == int(shop_money1):
        print('订 货 后: ' + singular1 + '件     ' + shop_money1 + '元')
    else:
        a = 1/0
        print(a)
    time.sleep(time1)
    driver.quit()
