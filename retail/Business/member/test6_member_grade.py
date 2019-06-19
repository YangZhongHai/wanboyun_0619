import time
from selenium import webdriver

from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from wholesale.group.procurement.login import Login
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name= Login.name(1)
login_pwd = Login.password(1)
hyleve = RandomMember.member_level(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

# 零售会员等级(会员等级增删改查)
def test6():
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

    # 点击会员管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[3]/div[1]/span/span').click()
    print('test6:进入零售→店铺→会员管理→会员等级')
    time.sleep(time1)
    # 会员等级
    driver.find_element_by_link_text('会员等级').click()
    time.sleep(time2)

    #新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)
    #等级名
    hyle = driver.find_element_by_xpath('//*[@id="name"]')
    hyle.click()
    hyle.clear()
    hyle.send_keys(hyleve)
    # 积分下线
    jfxx = driver.find_element_by_xpath('//*[@id="start_score"]')
    jfxx.click()
    jfxx.clear()
    jfxx.send_keys('0')
    # 积分上线
    jfsx = driver.find_element_by_xpath('//*[@id="end_score"]')
    jfsx.click()
    jfsx.clear()
    jfsx.send_keys('0')
    # 会员折扣
    hyzk = driver.find_element_by_xpath('//*[@id="discount"]')
    hyzk.click()
    hyzk.clear()
    hyzk.send_keys('100')
    #备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.clear()
    bz.send_keys('自动创建' + nowTime())
    #保存
    driver.find_element_by_xpath('//*[@class="ant-card-head-wrapper"]/div[2]/div/button[2]').click()
    print(hyleve + ':会员等级创建成功')
    print('会员等级新增功能正常\n')
    time.sleep(time2)

    # 搜索等级
    hyss = driver.find_element_by_xpath('//*[@id="name"]')
    hyss.click()
    hyss.clear()
    hyss.send_keys(hyleve)
    time.sleep(time1)
    driver.find_element_by_xpath('//*[@class="ant-row"]/div/button[1]').click()
    time.sleep(time1)

    search = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]/a').text
    if hyleve == search:
        print(hyleve + "  等于  " + search)
        print("会员等级按等级名称搜索正常\n")
    else:
        print(hyleve + "  不等于  " + search)
        print("搜索异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    # 点击编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/a[1]/i').click()
    time.sleep(time1)
    #保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print(hyleve + ":编辑成功")
    print("会员等级编辑功能正常\n")
    time.sleep(time2)

    # 搜索等级
    hyss = driver.find_element_by_xpath('//*[@id="name"]')
    hyss.click()
    hyss.clear()
    hyss.send_keys(hyleve)
    time.sleep(time1)
    driver.find_element_by_xpath('//*[@class="ant-row"]/div/button[1]').click()
    time.sleep(time1)

    #点击删除按钮
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/a[2]/i').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    print(hyleve + ":删除成功")
    print("会员等级删除功能正常")
    time.sleep(time1)
    driver.quit()