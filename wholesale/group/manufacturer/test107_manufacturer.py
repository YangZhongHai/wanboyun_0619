import time
from selenium import webdriver
from tool.loginFile.login import Login
from tool.random.randomMember import RandomMember
from tool.random.randomPhone import RandomPhone
from tool.random.randomSupplier import RandomSupplier
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
manufacturer = RandomSupplier.manufacturer_name(1)
phone = RandomPhone.phone(1)


# 厂商信息
def test107():
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
    print('test107:进入批发→分组→厂商设置→厂商信息')

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)


    # 点击商品管理
    # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[5]/div[1]/span/span').click()

    # time.sleep(time1)

    #厂商信息
    driver.find_element_by_link_text('厂商信息').click()
    time.sleep(time1)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time1)

    # 厂商名称
    csmc = driver.find_element_by_xpath('//*[@id="name"]')
    csmc.click()
    csmc.clear()
    csmc.send_keys(manufacturer)

    # 联系人
    lxrr = driver.find_element_by_xpath('//*[@id="contact"]')
    lxrr.click()
    lxrr.clear()
    lxrr.send_keys(RandomMember.member_name(1))

    # 电话
    gysdh = driver.find_element_by_xpath('//*[@id="tel"]')
    gysdh.click()
    gysdh.clear()
    gysdh.send_keys(phone)

    # 单位地址
    dwdz = driver.find_element_by_xpath('//*[@id="address"]')
    dwdz.click()
    dwdz.clear()
    dwdz.send_keys('成都市天府新区天府菁蓉大厦')
    # 银行卡
    yhk = driver.find_element_by_xpath('//*[@id="bank_card"]')
    yhk.click()
    yhk.clear()
    yhk.send_keys('6214837340093073')

    # 开户行
    khh = driver.find_element_by_xpath('//*[@id="opening_bank"]')
    khh.click()
    khh.clear()
    khh.send_keys('成都')
    # 信用额度
    xyed = driver.find_element_by_xpath('//*[@id="line_of_credit"]')
    xyed.click()
    xyed.clear()
    xyed.send_keys('10000')
    # 备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.clear()
    bz.send_keys('厂商' + nowTime())

    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/button[1]').click()
    time.sleep(time1)
    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print(manufacturer + ":厂商新建成功\n", "厂商新建功能正常\n")
    else:
        print(result_save + "\n厂商新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 搜索输入
    ygmc = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ygmc.click()
    ygmc.clear()
    ygmc.send_keys(manufacturer)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 搜素结果获取
    gyscxjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]/a').text
    if manufacturer == gyscxjg:
        print(manufacturer + ' 等于 ' + gyscxjg, '\n厂商搜索正常\n')
    else:
        print('厂商搜索异常')

    # 厂商编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/button[1]').click()
    print(manufacturer + ":厂商编辑成功\n", "厂商编辑功能正常\n")
    time.sleep(time2)

    # 搜索输入
    ygmc = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ygmc.click()
    ygmc.clear()
    ygmc.send_keys(manufacturer)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)


    # 点击删除按钮
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/a[2]/i').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_delect == correct:
        print(manufacturer + ":厂商删除成功\n", "厂商删除功能正常\n")
    else:
        print(result_delect + "\n厂商删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    driver.quit()
