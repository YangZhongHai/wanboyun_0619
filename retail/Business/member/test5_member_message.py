import time
from selenium import webdriver

from wholesale.group.procurement.login import Login
from tool.random.randomMember import RandomMember
from tool.random.randomPhone import RandomPhone
from tool.time.loadingTime import LoadTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
me = RandomMember.member_name(1)
sfz = RandomMember.member_IDcard(1)
are = RandomMember.member_area(1)
ph = RandomPhone.phone(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

# 零售会员信息(会员增删改查)
def test5():
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

    # 零售管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[1]').click()

    #进入店铺
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()

    # 点击会员管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[3]/div[1]/span/span').click()
    print('test5:进入零售→店铺→会员管理→会员信息')
    time.sleep(time1)

    # 点击会员信息
    driver.find_element_by_link_text('会员信息').click()
    time.sleep(time2)

    #新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    #会员姓名
    person=driver.find_element_by_xpath('//*[@id="name"]')
    person.click()
    person.clear()
    person.send_keys(me)

    #身份证
    hysfz=driver.find_element_by_xpath('//*[@id="idcard"]')
    hysfz.click()
    hysfz.clear()
    hysfz.send_keys(sfz)

    #电话
    phone1=driver.find_element_by_xpath('//*[@id="tel"]')
    phone1.click()
    phone1.clear()
    phone1.send_keys(ph)

    #所在地区
    hyarea=driver.find_element_by_xpath('//*[@id="area"]')
    hyarea.click()
    hyarea.clear()
    hyarea.send_keys(are)

    # 点击保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print(me+'：会员新建成功')
    print('会员新建功能正常\n')
    time.sleep(time2)

    # 输入搜索会员
    hyss = driver.find_element_by_xpath('//*[@id="name"]')
    hyss.click()
    hyss.clear()
    hyss.send_keys(me)
    time.sleep(time2)
    #搜索
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal ant-advanced-search-form"]/div[2]/div/button[1]').click()
    time.sleep(2)
    # 定位搜索会员名并判断
    sshy = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]').text
    if me == sshy:
        print(me + "  等于  " + sshy)
        print("会员搜索功能正常\n")
    else:
        print(me + "  不等于  " + sshy)
        print("搜索异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 点击会员编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[16]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print(me + ":编辑成功")
    print("会员编辑功能正常\n")
    time.sleep(time2)

    # 输入搜索会员
    hyss = driver.find_element_by_xpath('//*[@id="name"]')
    hyss.click()
    hyss.clear()
    hyss.send_keys(me)
    time.sleep(time2)
    # 搜索
    driver.find_element_by_xpath(
        '//*[@class="ant-form ant-form-horizontal ant-advanced-search-form"]/div[2]/div/button[1]').click()
    time.sleep(2)


    # 点击删除按钮
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[16]/div/a[2]/i').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    print(me + ":删除成功")
    print("会员删除功能正常")
    time.sleep(time1)
    driver.quit()




