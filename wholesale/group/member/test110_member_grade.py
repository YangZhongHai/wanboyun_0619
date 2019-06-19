import time
from selenium import webdriver

from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.loginFile.login import Login

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
level = RandomMember.member_level(1)
# 授信额度
number = RandomGoods.retail_price(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
discount = '30'

# 客户等级
def test110():
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
    print('test110:进入批发→分组→客户管理→会员等级')
    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    # 客户管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[5]/div[1]/span/span').click()

    # 客户等级
    driver.find_element_by_link_text('客户等级').click()
    time.sleep(time1)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time1)

    # 等级名称
    leve = driver.find_element_by_xpath('//*[@id="name"]')
    leve.click()
    leve.clear()
    leve.send_keys(level)
    time.sleep(time1)

    # 授信额度
    money1 = driver.find_element_by_xpath('//*[@id="credit_price"]')
    money1.click()
    money1.clear()
    money1.send_keys(number)

    # 批发折扣
    zhekou = driver.find_element_by_xpath('//*[@id="discount"]')
    zhekou.click()
    zhekou.clear()
    zhekou.send_keys(discount)

    # 退货比例
    tuihuo = driver.find_element_by_xpath('//*[@id="proportion"]')
    tuihuo.click()
    tuihuo.clear()
    tuihuo.send_keys(discount)


    # 点击保存
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_grade = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_grade == correct:
        print(level + ":等级新建成功\n", "等级新建功能正常\n")
    else:
        print(result_grade + "\n等级新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 输入搜索客户
    level_search = driver.find_element_by_xpath('//*[@id="name"]')
    level_search.click()
    level_search.clear()
    level_search.send_keys(level)
    # 查询
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[4]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(1)
    # 定位搜索会员等级名并判断
    search_leve_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if level == search_leve_name:
        print(level + "  等于  " + search_leve_name)
        print("等级搜索功能正常\n")
    else:
        print(level + "  不等于  " + search_leve_name)
        print("等级搜索异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 点击等级编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[6]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_grade1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_grade1 == correct:
        print(level + ":等级编辑成功\n", "等级编辑功能正常\n")
    else:
        print(result_grade1 + "\n等级编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 输入搜索等级
    level_search = driver.find_element_by_xpath('//*[@id="name"]')
    level_search.click()
    level_search.clear()
    level_search.send_keys(level)
    # 查询
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[4]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(1)

    # 点击删除按钮
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[6]/div/a[2]/i').click()
    time.sleep(time2)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(0.5)
    delect = driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/span').text
    wenzi = ('操作成功')
    if delect == wenzi:
        print(level + ":等级删除成功\n","等级删除功能正常")
    else:
        print(delect + ":等级删除失败!!!!!!!!!!\n")
    time.sleep(time1)
    driver.quit()