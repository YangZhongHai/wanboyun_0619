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
discount = '30'
import_number = RandomGoods.import_number(1)
random_number = RandomMember.random_number(1)
tim = nowTime()


# 采购入库
def test118():
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

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/a').click()
    time.sleep(time1)

    # 点击采购管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[7]/div[1]/span/span').click()
    print('test118:进入批发→组→采购管理→采购退货')
    time.sleep(time1)

    # 点击采购入库
    driver.find_element_by_link_text('采购退货').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 厂商
    driver.find_element_by_xpath('//*[@id="supplier_id"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time2)

    # 选择仓库
    driver.find_element_by_xpath(
        '//*[@id="warehouse_id"]/div/div/div[1]').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()
    time.sleep(time1)

    # 支付货款
    zfhk = driver.find_element_by_xpath(
        '//*[@id="payment_amount"]')
    zfhk.click()
    zfhk.clear()
    zfhk.send_keys(money)

    # 采购费用
    cgfy = driver.find_element_by_xpath(
        '//*[@id="costs"]')
    cgfy.click()
    cgfy.clear()
    cgfy.send_keys(money)

    # 采购费用备注
    fybz = driver.find_element_by_xpath(
        '//*[@id="costs_comment"]')
    fybz.click()
    fybz.clear()
    fybz.send_keys('费用备注' + tim)

    # 支付方式
    driver.find_element_by_xpath('//*[@id="payment_method"]/div/div/div[1]').click()
    time.sleep(time2)
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div//ul/li[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[1]').click()

    # 选择业务导购
    driver.find_element_by_xpath(
        '//*[@id="salesId"]/div/div/div[2]').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[%s]' % random_number).click()
    except:
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[%s]' % random_number).click()
    time.sleep(time1)

    # 采购费用备注
    djbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    djbz.click()
    djbz.clear()
    djbz.send_keys('单据备注' + tim)

    # 点击添加商品框输入搜索数字
    srsp = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/span[1]/div/div/div/ul/li/div/input')
    srsp.click()
    srsp.clear()
    srsp.send_keys(import_number)
    time.sleep(time1)
    # 选择搜索出来的第一个商品
    try:
        driver.find_element_by_xpath('/html/body/div[7]/div/div//ul[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[8]/div/div//ul[1]').click()
    time.sleep(time1)

    # 输入进货折扣
    input_ZK = driver.find_element_by_xpath(
        '//*[@id="discount"]/div/div/ul/li/div/input')
    input_ZK.click()
    input_ZK.send_keys(Keys.CONTROL, 'a')
    input_ZK.send_keys(discount)
    time.sleep(time2)


    # 定位数量输入框
    try:
        input_number = driver.find_element_by_xpath(
            '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div')
    except:
        input_number = driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div')
    # 鼠标双击选择
    ActionChains(driver).double_click(input_number).perform()
    time.sleep(time1)
    # 输入数量
    try:
        driver.find_element_by_xpath(
            '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/input').send_keys(random_number)
    except:
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/input').send_keys(random_number)
    # 确定
    driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(time1)
    # 获取进货商品名字
    shop_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/span/div').text
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_savel = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    zi = '不存在'
    res = '请先'
    resul = zi in result_savel
    resull = res in result_savel
    # 判断是否成功
    if resul == True:
        print(result_savel + shop_name + "\n采购退货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif resull == True:
        print(result_savel + shop_name + "\n采购退货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    try:
        # 取消打印
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    except:
        # 取消
        driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    time.sleep(time1)
    # 审核
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[13]/div/a[2]/i').click()
    time.sleep(time1)
    try:
        # 确认
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        # 确认
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    print(shop_name + '1件商品退货成功\n')
    driver.quit()
