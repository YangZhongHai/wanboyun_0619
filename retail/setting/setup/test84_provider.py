import time
from selenium import webdriver

from wholesale.group.procurement.login import Login
from tool.random.randomPerson import RandomStaff
from tool.random.randomPhone import RandomPhone
from tool.random.randomSupplier import RandomSupplier
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
loginname = Login.name(1)
loginpwd = Login.password(1)
tim = nowTime()
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

gysname = RandomSupplier.supplier_name(1)
personname = RandomStaff.person_name(1)
ph = RandomPhone.phone(1)


# 零售系统供应商信息
def test84():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(url)
        # 输入账号
        name=driver.find_element_by_id('user')
        name.click()
        name.clear()
        name.send_keys(loginname)

        # 输入密码
        pwd=driver.find_element_by_id('pwd')
        pwd.click()
        pwd.clear()
        pwd.send_keys(loginpwd)

        # 登陆
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()

        # 零售业务
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[1]').click()

        # 系统管理端
        driver.find_element_by_xpath('//*[@id="root"]/div/div/section/main/div/div[1]/button[1]').click()
        time.sleep(time1)

        #系统设置
        driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[1]/div[1]/span/span').click()
        print('test84:进入零售→系统管理→系统设置→供应商信息')
        time.sleep(time1)

        #供应商信息
        driver.find_element_by_link_text('供应商信息').click()
        time.sleep(time1)
        driver.find_element_by_link_text('新增').click()
        time.sleep(time1)
        #供应商名称
        gys = driver.find_element_by_xpath('//*[@id="name"]')
        gys.click()
        gys.clear()
        gys.send_keys(gysname)

        #电话
        gysdh = driver.find_element_by_xpath('//*[@id="tel"]')
        gysdh.click()
        gysdh.clear()
        gysdh.send_keys(ph)

        #联系人
        syslxr = driver.find_element_by_xpath('//*[@id="contact"]')
        syslxr.click()
        syslxr.clear()
        syslxr.send_keys(personname)
        #单位地址
        dwdz = driver.find_element_by_xpath('//*[@id="address"]')
        dwdz.click()
        dwdz.clear()
        dwdz.send_keys('成都市天府新区天府菁蓉大厦')
        #银行卡
        yhk = driver.find_element_by_xpath('//*[@id="bank_card"]')
        yhk.click()
        yhk.clear()
        yhk.send_keys('6214837340093073')
        #开户行
        khh = driver.find_element_by_xpath('//*[@id="opening_bank"]')
        khh.click()
        khh.clear()
        khh.send_keys('成都')
        #信用额度
        xyed = driver.find_element_by_xpath('//*[@id="line_of_credit"]')
        xyed.click()
        xyed.clear()
        xyed.send_keys('10000')
        #备注
        bz = driver.find_element_by_xpath('//*[@id="comment"]')
        bz.click()
        bz.clear()
        bz.send_keys('供应商备注' + tim)

        # 保存
        driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        # 抓取保存结果
        result = driver.find_element_by_xpath(
            '/html/body/div[2]/div/span/div/div/div/span').text
        correct = ('操作成功')
        # 判断是否成功
        if result == correct:
            print(gysname + ":供应商创建成功\n", "供应商新增功能正常\n")
        else:
            print(result + "\n供应商创建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time1)

        # 搜索输入
        ygmc = driver.find_element_by_xpath('//*[@id="name"]')
        ygmc.click()
        ygmc.clear()
        ygmc.send_keys(gysname)
        # 查询
        driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)

        # 搜素结果获取
        gyscxjg = driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]/a').text
        if gysname == gyscxjg:
            print(gysname + ' 等于 ' + gyscxjg, '\n供应商搜索正常\n')
        else:
            print('供应商搜索异常')

        # 供应商编辑
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[13]/div/a[1]/i').click()
        time.sleep(time1)
        # 保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        # 抓取保存结果
        result_save = driver.find_element_by_xpath(
            '/html/body/div[2]/div/span/div/div/div/span').text
        correct = ('操作成功')
        # 判断是否成功
        if result_save == correct:
            print(gysname + ":供应商编辑成功\n", "供应商编辑功能正常\n")
        else:
            print(result_save + "\n供应商编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time2)

        # 搜索输入
        ygmc = driver.find_element_by_xpath('//*[@id="name"]')
        ygmc.click()
        ygmc.clear()
        ygmc.send_keys(gysname)
        # 查询
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)

        # 点击删除按钮
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[13]/div/a[2]/i').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        # 抓取保存结果
        result_save1 = driver.find_element_by_xpath(
            '/html/body/div[2]/div/span/div/div/div/span').text
        correct = ('操作成功')
        # 判断是否成功
        if result_save1 == correct:
            print(gysname + ":供应商删除成功\n", "供应商删除功能正常\n")
        else:
            print(result_save + "\n供应商删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time2)
    except:
        print('供应商信息异常')
        time.sleep(1000)

    finally:
        driver.close()
