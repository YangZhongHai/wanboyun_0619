import time
from selenium.webdriver import ActionChains  # 鼠标双击模块
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from wholesale.group.procurement.login import Login
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
import_number = RandomGoods.import_number(1)
tim = nowTime()


# 采购退货
def test16():
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
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/a').click()
    print('test16:进入零售→店铺→采购管理→采购退货')
    # 库存管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[5]/div[1]/span/span').click()
    time.sleep(time1)
    # 库存信息
    driver.find_element_by_link_text('库存信息').click()
    time.sleep(time3)
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time1)
    shop_number = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/span[1]/span').text
    print('采购退货前库存: ' + shop_number + '件')
    # 采购管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[6]/div[1]/span/span').click()
    time.sleep(time1)
    # 采购退货
    driver.find_element_by_link_text('采购退货').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 供应商
    driver.find_element_by_xpath(
        '/html//div/section/section/main/div/div/div[3]/div[2]/div/div/div/div/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/span/div/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
    # 选择仓库
    driver.find_element_by_xpath(
        '//*[@id="warehouse_id"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 支付货款
    zfhk = driver.find_element_by_xpath(
        '//*[@id="payment_amount"]')
    zfhk.click()
    zfhk.clear()
    zfhk.send_keys(import_number)

    # 采购费用
    cgfy = driver.find_element_by_xpath(
        '//*[@id="costs"]')
    cgfy.click()
    cgfy.clear()
    cgfy.send_keys(import_number)

    # 费用说明
    fybz = driver.find_element_by_xpath(
        '//*[@id="costs_comment"]')
    fybz.click()
    fybz.clear()
    fybz.send_keys('费用备注' + tim)

    # 选择业务导购
    driver.find_element_by_xpath(
        '//*[@id="salesId"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 采购费用备注
    djbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    djbz.click()
    djbz.clear()
    djbz.send_keys('单据备注' + tim)

    # 点击添加商品框输入搜索数字
    srsp = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[3]/div[2]/div/div/div[2]/div/span[1]/div/div/div/ul/li/div/input')
    srsp.click()
    srsp.clear()
    srsp.send_keys(import_number)
    time.sleep(time1)
    # 选择搜索出来的第一个商品
    driver.find_element_by_xpath('/html/body/div[6]/div/div//ul/li[1]').click()
    time.sleep(time1)

    # 输入进货折扣
    input_ZK = driver.find_element_by_xpath(
        '//*[@id="discount"]/div/div/ul/li/div/input')
    input_ZK.click()
    input_ZK.send_keys(Keys.CONTROL, 'a')
    input_ZK.send_keys('30')
    time.sleep(time2)


    # 定位数量输入框
    input_number = driver.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div')
    # 鼠标双击选择
    ActionChains(driver).double_click(input_number).perform()
    time.sleep(time1)
    # 输入数量
    driver.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/input').send_keys(import_number)

    # 确定
    driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(time1)
    # 获取进货商品名字
    shop_name = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/span/span').text
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time2)
    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print(shop_name + ":采购退货下单成功\n")
    else:
        print(result_save + "\n采购退货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)


    # 审核
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[14]/div/a[2]/i').click()
    time.sleep(time1)

    try:
        # 确认
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    except:
        # 确认
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_save1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save1 == correct:
        print(shop_name + ":采购退货" + import_number + "件,审核成功\n")
    else:
        print(result_save1 + "\n采购退货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 库存管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[5]/div/span/span').click()
    time.sleep(time1)
    # 库存信息
    driver.find_element_by_link_text('库存信息').click()
    time.sleep(time2)
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time1)
    shop_number1 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/span[1]/span').text
    print('采购退货后库存: ' + shop_number1 + '件')
    a = int(shop_number) - int(import_number)
    b = int(shop_number1)
    if a == b:
        print('采购退货正常')
    else:
        print('采购退货异常!!!!!!!!!!!')
    driver.quit()