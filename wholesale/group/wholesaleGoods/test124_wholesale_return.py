import time
from selenium.webdriver import ActionChains  # 鼠标双击模块
from selenium import webdriver
from wholesale.group.procurement.login import Login
from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
money = RandomGoods.shop_price(1)
import_number = RandomGoods.import_number(1)
random_number = RandomMember.random_number(1)
tim = nowTime()


# 批发订单
def test124():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Login.location(1))
    # 输入账号
    name = driver.find_element_by_id('user')
    name.click()
    name.clear()
    name.send_keys(Login.name(1))

    # 输入密码
    pwd = driver.find_element_by_id('pwd')
    pwd.click()
    pwd.clear()
    pwd.send_keys(Login.password(1))

    # 登陆
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()
    # driver.find_element_by_class_name('ant-btn ant-btn-primary')

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/a').click()
    time.sleep(time1)

    # 点击批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[9]/div[1]/span/span').click()
    print('test124:进入批发→组→批发管理→批发退货')
    time.sleep(time1)

    # 批发退货
    driver.find_element_by_link_text('批发退货').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 订货客户
    driver.find_element_by_xpath('//*[@id="client_id"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time2)

    # 选择仓库
    driver.find_element_by_xpath(
        '//*[@id="warehouse_id"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 业务员
    driver.find_element_by_xpath('//*[@id="salesId"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div//ul/li[%s]' % random_number).click()
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

    # 本次收款
    fybz = driver.find_element_by_xpath(
        '//*[@id="payment_amount"]')
    fybz.click()
    fybz.clear()
    fybz.send_keys(money)

    # 支付方式
    driver.find_element_by_xpath('//*[@id="payment_method"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[1]').click()

    # 批发备注
    djbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    djbz.click()
    djbz.clear()
    djbz.send_keys('批发' + tim)

    # 点击添加商品框输入搜索数字
    srsp = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/span/div/div/div/ul/li/div/input')
    srsp.click()
    srsp.clear()
    srsp.send_keys(import_number)
    time.sleep(time1)
    # 选择搜索出来的第一个商品
    driver.find_element_by_xpath('/html/body/div[7]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 定位数量输入框
    input_number = driver.find_element_by_xpath(
        '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div')
    # 鼠标双击选择
    ActionChains(driver).double_click(input_number).perform()
    time.sleep(time2)
    # 输入数量
    driver.find_element_by_xpath(
        '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/input').send_keys(random_number)

    # 确定
    driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(time1)
    # 获取进货商品名字
    shop_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div/span').text
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    print(shop_name + ':批发订单' + '1件下单成功', '\n批发订单下单正常\n')
    time.sleep(time1)
    # 抓取结果
    result_savel = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    time.sleep(time1)
    zi = '库存'
    re = '备用'
    resul = zi in result_savel
    resull = zi in result_savel
    # 判断是否成功
    if resul == True:
        print(result_savel + "\n批发审核异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif resull == True:
        print(result_savel + "\n批发审核异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # 取消打印
    try:
        driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    time.sleep(time1)

    # 审核
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[13]/div/a[1]/i').click()
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
        print(shop_name + ":批发审核成功\n", "批发审核正常\n")
    else:
        print(result_save + "\n批发审核异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 提交发货
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[13]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()

    # 抓取结果
    result_save1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save1 == correct:
        print(shop_name + ":批发发货成功\n", "批发发货正常\n")
    else:
        print(result_save1 + "\n批发发货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    driver.quit()


