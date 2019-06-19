import time
from selenium import webdriver


from tool.loginFile.login import Login
from tool.random.randomMember import RandomMember
from tool.random.randomPhone import RandomPhone
from tool.random.randomSupplier import RandomSupplier
from tool.time.loadingTime import LoadTime

url = Login.location(1)
addname = Login.name(1)
addpwd = Login.password(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
manufacturer = RandomSupplier.manufacturer_name(1)
lxr = RandomMember.member_name(1)
phone = RandomPhone.phone(1)


# 退货设置
def test108():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    # 输入账号
    name=driver.find_element_by_id('user')
    name.click()
    name.clear()
    name.send_keys(addname)

    # 输入密码
    pwd=driver.find_element_by_id('pwd')
    pwd.click()
    pwd.clear()
    pwd.send_keys(addpwd)

    # 登陆
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()
    print('test108:进入批发→分组→厂商设置→退货设置')

    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    #厂商信息
    driver.find_element_by_link_text('退货设置').click()
    time.sleep(time1)

    # 厂商搜索输入
    driver.find_element_by_xpath('//*[@id="supplier_id"]/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[1]').click()
    time.sleep(time1)

    #查询
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    #首单编辑
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/a/i').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_save = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save == correct:
        print("退货设置编辑成功\n", "退货设置编辑功能正常\n")
    else:
        print(result_save + "\n退货设置编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 补单编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/a/i').click()
    time.sleep(time1)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_save1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_save1 == correct:
        print("退货设置编辑成功\n", "退货设置编辑功能正常\n")
    else:
        print(result_save1 + "\n退货设置编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)
    driver.quit()
