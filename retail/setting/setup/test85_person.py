import time
from selenium import webdriver

from tool.addMember.randomMember import RandomMember
from tool.time.nowTime import addTime
from tool.time.loadingTime import LoadTime
from tool.time.randomPhone import RandomPhone
from tool.addStaff.randomPerson import RandomStaff
from tool.loginFile.login import Login

url = Login.location(1)
loginname = Login.name(1)
loginpwd = Login.password(1)
tim = addTime()
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
id = RandomStaff.person_id(1)
personname = RandomStaff.person_name(1)
ph = RandomPhone.phone(1)
lxrname = RandomMember.member_name(1)

# 零售系统员工信息
def test85():
    try:
        # r"D:\Python36-32\chromedriver.exe"
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
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button[1]').click()

        # 系统管理端
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/button[1]').click()
        time.sleep(time1)

        #系统设置
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[1]/div[1]').click()
        print('test85:进入零售→系统管理→系统设置→员工信息')
        time.sleep(time1)

        #员工信息
        driver.find_element_by_xpath('//*[@id="settings$Menu"]/li[5]/a').click()
        time.sleep(time2)
        driver.find_element_by_link_text('新增').click()
        time.sleep(time2)
        #员工编号
        ygbh = driver.find_element_by_xpath('//*[@id="code"]')
        ygbh.click()
        ygbh.clear()
        ygbh.send_keys(id)

        #员工姓名
        ygxm = driver.find_element_by_xpath('//*[@id="name"]')
        ygxm.click()
        ygxm.clear()
        ygxm.send_keys(personname)

        #身份证
        sfz = driver.find_element_by_xpath('//*[@id="idcard"]')
        sfz.click()
        sfz.clear()
        sfz.send_keys('510503199409223478')
        #性别
        driver.find_element_by_xpath('//*[@id="sex"]/div').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
        time.sleep(time1)
        #电话
        dh = driver.find_element_by_xpath('//*[@id="tel"]')
        dh.click()
        dh.clear()
        dh.send_keys(ph)
        #籍贯
        jg = driver.find_element_by_xpath('//*[@id="native_place"]')
        jg.click()
        jg.clear()
        jg.send_keys('汉')
        #公积金账号
        gjj = driver.find_element_by_xpath('//*[@id="accumulation_fund"]')
        gjj.click()
        gjj.clear()
        gjj.send_keys('12345678')
        #社保账号
        sb = driver.find_element_by_xpath('//*[@id="social_num"]')
        sb.click()
        sb.clear()
        sb.send_keys(ph)
        #紧急联系人
        lxrr = driver.find_element_by_xpath('//*[@id="emergency_contact"]')
        lxrr.click()
        lxrr.clear()
        lxrr.send_keys(lxrname)
        #紧急联系人电话
        lxrrph = driver.find_element_by_xpath('//*[@id="emergency_tel"]')
        lxrrph.click()
        lxrrph.clear()
        lxrrph.send_keys(ph)
        #通讯地址
        dz = driver.find_element_by_xpath('//*[@id="address"]')
        dz.click()
        dz.clear()
        dz.send_keys('成都')

        # 所属部门
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div[2]/div/span/span/span/span[1]/span').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li/ul/li/span[2]/span').click()
        # 店铺
        driver.find_element_by_xpath('//*[@id="store"]/div/div/div[1]').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()
        # 角色
        driver.find_element_by_xpath('//*[@id="position_id"]/div/div/div[1]').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[3]').click()
        # 业务范围
        driver.find_element_by_xpath('//*[@id="access_rigths"]/div/div/div[1]').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[1]').click()
        # 保存
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time1)

        # 保存
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
        print(personname+':员工新建成功\n')
        time.sleep(time1)

        # 员工搜索输入
        ygss = driver.find_element_by_xpath('//*[@class="ant-col-4"]/div/div[2]/div/span/input')
        ygss.click()
        ygss.clear()
        ygss.send_keys(personname)
        # 查询
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)
        # 搜素结果获取
        ssygmz = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a').text
        if id == ssygmz:
            print(id + ' 等于 ' + ssygmz,'\n员工搜索正常\n')
        else:
            print('员工搜索异常')

        # 点击员工编辑
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/a[1]/i').click()
        time.sleep(time1)
        # 保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        print(id + ":编辑成功\n","会员编辑功能正常\n")
        time.sleep(time2)

        # 员工搜索输入
        ygss = driver.find_element_by_xpath('//*[@class="ant-col-4"]/div/div[2]/div/span/input')
        ygss.click()
        ygss.clear()
        ygss.send_keys(personname)
        # 查询
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)

        # # 点击删除按钮
        # driver.find_element_by_xpath(
        #     '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td/div/a[2]/i').click()
        # time.sleep(time1)
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        # print(id + ":员工删除成功\n","员工删除功能正常\n")
        # time.sleep(time1)

    except:
        print('员工信息异常')

    finally:
        driver.close()
