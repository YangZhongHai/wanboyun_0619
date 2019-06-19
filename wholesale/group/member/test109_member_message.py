import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.loginFile.login import Login
from tool.random.randomMember import RandomMember
from tool.random.randomPerson import RandomStaff
from tool.random.randomPhone import RandomPhone
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
menber_name = RandomMember.member_name(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

# 客户信息
def test109():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    # 输入账号
    name=driver.find_element_by_id('user')
    name.click()
    name.clear()
    name.send_keys(Login.name(1))

    # 输入密码
    pwd=driver.find_element_by_id('pwd')
    pwd.click()
    pwd.clear()
    pwd.send_keys(Login.password(1))

    # 登陆
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()
    print('test109:进入批发→分组→客户管理→客户管理')

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    # 客户管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[5]/div[1]/span/span').click()
    time.sleep(time1)

    # 客户信息
    driver.find_element_by_link_text('客户信息').click()
    time.sleep(time1)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time1)

    # 客户名称
    person = driver.find_element_by_xpath('//*[@id="name"]')
    person.click()
    person.clear()
    person.send_keys(menber_name)

    # 客户等级
    driver.find_element_by_xpath('//*[@id="client_level"]/div/div/div[1]').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
    # 负责人
    phone1 = driver.find_element_by_xpath('//*[@id="principal"]')
    phone1.click()
    phone1.clear()
    phone1.send_keys(RandomStaff.person_name(1))

    # 手机号码
    hyarea = driver.find_element_by_xpath('//*[@id="phone"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys(RandomPhone.phone(1))

    # 店铺地址
    hyarea = driver.find_element_by_xpath('//*[@id="address"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys(RandomMember.member_area(1))

    # 座机号码
    hyarea = driver.find_element_by_xpath('//*[@id="tel"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys('0830-4892927')

    # 邮箱
    hyarea = driver.find_element_by_xpath('//*[@id="mail"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys('1518542154@qq.com')

    # 授信额度
    hyarea = driver.find_element_by_xpath('//*[@id="credits"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys(RandomGoods.retail_price(1))

    # 备注
    hyarea = driver.find_element_by_xpath('//*[@id="comment"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys(nowTime() + '客户新建')

    # 点击保存
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_member = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_member == correct:
        print(menber_name + ":客户新增成功\n", "客户新增功能正常\n")
    else:
        print(result_member + "\n客户新增异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 输入搜索客户
    member_search = driver.find_element_by_xpath('//*[@id="name"]')
    member_search.click()
    member_search.clear()
    member_search.send_keys(menber_name)
    time.sleep(time2)
    # 查询
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(2)
    # 定位搜索客户名并判断
    search_member_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]').text
    if menber_name == search_member_name:
        print(menber_name + "  等于  " + search_member_name)
        print("客户搜索功能正常\n")
    else:
        print(menber_name + "  不等于  " + search_member_name)
        print("客户搜索异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 点击客户编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[12]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_member1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_member1 == correct:
        print(menber_name + ":客户编辑成功\n", "客户编辑功能正常\n")
    else:
        print(result_member + "\n客户编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 输入搜索客户
    member_search = driver.find_element_by_xpath('//*[@id="name"]')
    member_search.click()
    member_search.clear()
    member_search.send_keys(menber_name)
    time.sleep(time2)
    # 查询
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(1)

    # 点击删除按钮
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[12]/div/a[2]/i').click()
    time.sleep(time2)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(0.5)
    delect = driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/span').text
    wenzi = ('存在组绑定该客户，请解除绑定在进行作废')
    if delect == wenzi:
        print(menber_name + ":删除成功\n","客户删除功能正常")
    else:
        print(delect + "\n客户删除异常!!!!!!!")
    time.sleep(time1)
    driver.quit()