import time
from selenium import webdriver



from wholesale.group.procurement.login import Login
from tool.random.randomPerson import RandomStaff
from tool.random.randomPhone import RandomPhone
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
tim = nowTime()

time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
person_id = RandomStaff.person_id(1)
pname = RandomStaff.person_name(1)
phone = RandomPhone.phone(1)


# 系统--员工基础信息
def test184():
    try:
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

        # 批发管理
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

        # 系统管理
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/section/main/div/div[1]/button[1]').click()
        time.sleep(time1)


        # 点击员工基础信息
        driver.find_element_by_link_text('员工基础信息').click()
        time.sleep(time2)
        driver.find_element_by_link_text('新增').click()
        time.sleep(time2)

        # 员工编号
        person_id1 = driver.find_element_by_xpath('//*[@id="code"]')
        person_id1.click()
        person_id1.clear()
        person_id1.send_keys(person_id)

        # 员工姓名
        person_name1 = driver.find_element_by_xpath('//*[@id="name"]')
        person_name1.click()
        person_name1.clear()
        person_name1.send_keys(pname)

        # 员工身份证
        person_sfz = driver.find_element_by_xpath('//*[@id="idcard"]')
        person_sfz.click()
        person_sfz.clear()
        person_sfz.send_keys('510503199409223478')

        #性别
        driver.find_element_by_xpath('//*[@id="sex"]/div/div/div[1]').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div//ul/li[1]').click()

        # 员工电话
        person_phone = driver.find_element_by_xpath('//*[@id="tel"]')
        person_phone.click()
        person_phone.clear()
        person_phone.send_keys(phone)

        # 籍贯
        person_jg = driver.find_element_by_xpath('//*[@id="native_place"]')
        person_jg.click()
        person_jg.clear()
        person_jg.send_keys('成都')

        # 公积金账号
        person_gjj = driver.find_element_by_xpath('//*[@id="accumulation_fund"]')
        person_gjj.click()
        person_gjj.clear()
        person_gjj.send_keys('12345678')

        # 社保账号
        person_sb = driver.find_element_by_xpath('//*[@id="social_num"]')
        person_sb.click()
        person_sb.clear()
        person_sb.send_keys('12345678')

        # 紧急联系人
        person_lxr = driver.find_element_by_xpath('//*[@id="emergency_contact"]')
        person_lxr.click()
        person_lxr.clear()
        person_lxr.send_keys(pname)

        # 联系人电话
        person_phone1 = driver.find_element_by_xpath('//*[@id="emergency_tel"]')
        person_phone1.click()
        person_phone1.clear()
        person_phone1.send_keys(phone)

        # 联系人地址
        person_phone1 = driver.find_element_by_xpath('//*[@id="address"]')
        person_phone1.click()
        person_phone1.clear()
        person_phone1.send_keys('成都市天府新区天府菁蓉大厦')

        #保存
        driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time1)
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
        time.sleep(time2)
        # 抓取结果
        result11 = driver.find_element_by_xpath(
            '/html/body/div[2]/div/span/div/div/div/span').text
        correct1 = ('操作成功')
        # 判断是否成功
        if result11 == correct1:
            print(pname + ":员工新建成功\n", "员工新建功能正常\n")
        else:
            print(result11 + "\n员工新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time2)

        # 员工搜索输入
        seach = driver.find_element_by_xpath('//*[@id="code"]')
        seach.click()
        seach.clear()
        seach.send_keys(pname)

        #查询
        driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time1)
        # 定位搜索员工名并判断
        search_member_name = driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]').text
        if search_member_name == pname:
            print(pname + "  等于  " + search_member_name + "\n员工搜索功能正常\n")
        else:
            print("员工搜索异常!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        time.sleep(time1)

        #编辑
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[11]/div/a[1]/i').click()
        time.sleep(time1)
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time1)
        # 抓取结果
        result111 = driver.find_element_by_xpath(
            '/html/body/div[2]/div/span/div/div/div/span').text
        correct11 = ('操作成功')
        # 判断是否成功
        if result111 == correct11:
            print(pname + ":员工编辑成功\n", "员工编辑功能正常\n")
        else:
            print(result11 + "\n员工编辑异常!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time2)

        # # 员工搜索输入
        # seach = driver.find_element_by_xpath('//*[@id="code"]')
        # seach.click()
        # seach.clear()
        # seach.send_keys(pname)
        #
        # # 查询
        # driver.find_element_by_xpath(
        #     '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        # time.sleep(time1)
        #
        # #删除
        # driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[11]/div/a[2]/i').click()
        # time.sleep(time1)
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        # time.sleep(time1)
        # # 抓取结果
        # result_delect = driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/span/div/div/div/span').text
        # correct = ('操作成功')
        # # 判断是否成功
        # if result_delect == correct:
        #     print(pname + ":员工删除成功\n", "员工删除功能正常\n")
        # else:
        #     print(result_delect + "\n员工删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # time.sleep(time1)

    except:
        print('员工信息异常')

    finally:
        driver.close()
