import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.loginFile.login import Login
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
number = RandomGoods.import_number(1)
random_number = RandomMember.random_number(1)

# 零售退货
def test19():
    # try:
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

    # 零售业务
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[1]').click()

    # 进入店铺
    driver.find_element_by_link_text('进入店铺').click()
    time.sleep(time1)

    # 前台业务
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[7]/div[1]/span/span').click()
    print('test19:进入零售→店铺→前台业务→零售退货')
    time.sleep(time1)

    # 零售退货
    driver.find_element_by_link_text('零售退货').click()
    time.sleep(time2)

    #查询
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    s1 = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[1]/strong').text
    s2 = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[2]/strong').text
    singular = RandomMember.extract_number(s1)
    shop_money = RandomMember.extract_number(s2)
    print('退 货 前: ' + singular + '件   '+ shop_money + '元   ')
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)
    # 选择业务导购
    driver.find_element_by_xpath('//*[@id="salesId"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[%s]' % random_number).click()
    time.sleep(time1)

    # 输入备注
    bz = driver.find_element_by_xpath('//*[@id="comment"]')
    bz.click()
    bz.clear()
    bz.send_keys("生成时间" + nowTime())
    #点击会员信息框
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[1]/div/div/div[2]/div/span/div/div/div/div[1]').click()
    time.sleep(time1)
    #输入会员名字
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[1]/div/div/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(random_number)
    time.sleep(time2)
    #选择搜索出来的会员
    driver.find_element_by_xpath('/html/body/div[4]/div/div//ul/li[%s]' % random_number).click()

    # 正常退货
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/form/div/div[1]/div[2]/div[1]/div/div[2]/div/button[1]').click()
    time.sleep(time1)
    # 选择订单
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span/label/span/input').click()
    time.sleep(time2)
    # 确定
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    time.sleep(time2)

    #获取应收金额
    ysje = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[7]/div/div[1]/div/div[2]/span').text
    pay_money = ysje.split('.')[0]
    #现金支付输入
    xjzf = driver.find_element_by_xpath('//*[@id="return_balance"]')
    xjzf.click()
    xjzf.send_keys(pay_money)
    time.sleep(time2)

    #保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print('退货单生成成功')
    else:
        print(result_save + "\n零售退货异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    #取消打印单据
    try:
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    except:
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    s11 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[1]/strong').text
    s22 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/span[2]/strong').text

    singular1 = RandomMember.extract_number(s11)
    singular2 = int(singular) + 1
    number1 = RandomMember.extract_number(s22)
    number2 = int(shop_money) + int(pay_money)

    print('实际退货: 1件  ' + pay_money + '元\n')
    if singular2 == int(singular1) and number2 == int(number1):
        print('退 货 后: ' + singular1 + '件   ' + number1 + '元   \n' + '零售退货正常')
    else:
        print('退货异常!!!!!')
        time.sleep(time1)
    driver.quit()
