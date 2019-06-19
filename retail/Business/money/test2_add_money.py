import time
from selenium import webdriver

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
fkr = RandomMember.member_name(1)


# 零售财务管理--日常收入
def test2():
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

    # 零售管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[1]').click()

    # 进入店铺
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()

    # 点击财务管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[2]/div[1]/span/span').click()
    print('test2:进入零售→店铺→财务管理→日常收入')
    time.sleep(time1)

    # 点击日常收入
    driver.find_element_by_link_text('日常收入').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 业务部门
    driver.find_element_by_xpath('//*[@id="department"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()

    #款项名称
    driver.find_element_by_xpath('//*[@id="name"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[2]').click()

    #收款人
    skr = driver.find_element_by_xpath('//*[@id="payee"]')
    skr.click()
    skr.send_keys(fkr)

    #支付金额
    skr = driver.find_element_by_xpath('//*[@id="payment"]')
    skr.click()
    skr.send_keys('100')

    #付款方式
    driver.find_element_by_xpath('//*[@id="method"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[2]').click()

    #业务员
    driver.find_element_by_xpath('//*[@id="salesman"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()

    #备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.send_keys('自动备注' + tim)

    # 保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print('日常收入订单新建成功\n','日常收入订单新增功能正常')
    time.sleep(time2)
    driver.quit()
