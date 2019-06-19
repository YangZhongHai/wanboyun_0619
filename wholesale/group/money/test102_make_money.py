import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from wholesale.group.procurement.login import Login
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
tim = nowTime()
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
person_name = RandomMember.member_name(1)
money = RandomGoods.shop_transportation_price(1)


# 批发财务管理--日常收入
def test102():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    # 输入账号
    name=driver.find_element_by_id('user')
    name.click()
    name.clear()
    name.send_keys(login_name)

    # 输入密码
    pwd=driver.find_element_by_id('pwd')
    pwd.click()
    pwd.clear()
    pwd.send_keys(login_pwd)

    # 登陆
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()
    print('test102:进入批发→组→财务管理→日常收入')
    time.sleep(time1)

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    # 点击财务管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[2]/div[1]/span/span').click()
    time.sleep(time1)

    # 点击日常收入
    driver.find_element_by_link_text('日常收入').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 款项名称
    driver.find_element_by_xpath('//*[@id="name"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[1]').click()

    #付款人
    person = driver.find_element_by_xpath('//*[@id="payee"]')
    person.click()
    person.clear()
    person.send_keys(person_name)

    #收款金额
    add_money = driver.find_element_by_xpath('//*[@id="payment"]')
    add_money.click()
    add_money.clear()
    add_money.send_keys(money)

    #支付方式
    driver.find_element_by_xpath('//*[@id="method"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[1]').click()

    # #业务员
    # driver.find_element_by_xpath('//*[@id="salesman"]/div/div').click()
    # time.sleep(time1)
    # driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()

    #备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.send_keys('收入' + tim)

    # 保存
    driver.find_element_by_xpath('//*[@role="tabpanel"]/div[2]/div/div/div/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_add = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_add == correct:
        print("日常收入订单新建成功\n", "日常收入新建功能正常\n")
    else:
        print(result_add + "\n批发端日常收入异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    driver.quit()