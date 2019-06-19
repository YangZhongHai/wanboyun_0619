import time
from selenium.webdriver import ActionChains  # 鼠标双击模块
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tool.loginFile.login import Login
from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
money = RandomGoods.shop_price(1)
import_number = RandomGoods.import_number(1)
random_number = RandomMember.random_number(1)
tim = nowTime()


# 店铺配货
def test127():
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
    # driver.find_element_by_class_name('ant-btn ant-btn-primary')

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/a').click()
    time.sleep(time1)

    # 店铺管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[11]/div[1]/span/span').click()
    print('test127:进入批发→组→店铺管理→店铺配货')
    time.sleep(time1)

    # 批发订单
    driver.find_element_by_link_text('店铺配货').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 自营店铺
    driver.find_element_by_xpath('//*[@id="selfStore"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time2)

    # 发货仓库
    driver.find_element_by_xpath(
        '//*[@id="warehouse"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 支付方式
    driver.find_element_by_xpath('//*[@id="payment_method"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div//ul/li[1]').click()
    time.sleep(time2)

    # 业务费用
    zfhk = driver.find_element_by_xpath(
        '//*[@id="costs"]')
    zfhk.click()
    zfhk.clear()
    zfhk.send_keys(money)

    # 费用备注
    fybz = driver.find_element_by_xpath(
        '//*[@id="costs_comment"]')
    fybz.click()
    fybz.clear()
    fybz.send_keys('费用说明' + tim)

    # 业务员
    driver.find_element_by_xpath('//*[@id="salesId"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time2)

    # 备注
    djbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    djbz.click()
    djbz.clear()
    djbz.send_keys('店配' + tim)

    # 点击添加商品框输入搜索数字
    srsp = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/ul/li/div/input')
    srsp.click()
    srsp.clear()
    srsp.send_keys(import_number)
    time.sleep(time1)
    # 选择搜索出来的第一个商品
    driver.find_element_by_xpath('/html/body/div[7]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 输入进货折扣
    input_ZK = driver.find_element_by_xpath(
        '//*[@id="discount"]/div/div/ul/li/div/input')
    input_ZK.click()
    input_ZK.send_keys(Keys.CONTROL, 'a')
    input_ZK.send_keys('50')


    # 定位数量输入框
    input_number = driver.find_element_by_xpath(
        '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div')
    # 鼠标双击选择
    ActionChains(driver).double_click(input_number).perform()
    time.sleep(time2)
    # 输入数量
    driver.find_element_by_xpath(
        '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/input').send_keys(random_number)
    # 确定
    driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(time1)
    # 获取进货商品名字
    shop_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div/span/div').text
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print(shop_name + ':店铺配货1件下单成功', '\n配货下单正常\n')
    time.sleep(time1)
    # 抓取结果
    result_savel = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    time.sleep(time1)
    zi = '单据金额'
    re = '第1'
    resul = zi in result_savel
    resull = zi in result_savel
    # 判断是否成功
    if resul == True:
        print(result_savel + "\n店铺配货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif resull == True:
        print(result_savel + "\n店铺配货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 审核
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[15]/div/a[1]/i').click()
    time.sleep(time1)

    # 确认
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print(shop_name + ":店铺配货审核成功\n", "店铺配货正常\n")
    else:
        print(result_save + "\n店铺配货审核异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 提交发货
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[15]/a/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]').click()
    # time.sleep(time1)
    # # 抓取结果
    # result_save2 = driver.find_element_by_xpath(
    #     '/html/body/div[2]/div/span/div/div/div/span').text
    # zi = '没有'
    # resul = zi in result_save2
    # # 判断是否成功
    # if resul == True :
    #     print(result_save2 + "\n批发审核异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # 抓取结果
    result_save1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save1 == correct:
        print(shop_name + ":批发发货成功\n", "批发发货正常\n")
    else:
        print(result_save1 + "\n批发发货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    driver.quit()

