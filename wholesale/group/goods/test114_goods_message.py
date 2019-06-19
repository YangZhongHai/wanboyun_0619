import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from wholesale.group.procurement.login import Login

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
goods_number = RandomGoods.goods_number(1)
goods_name = RandomGoods.goods_name(1)
price = RandomGoods.price(1)
retail = RandomGoods.retail_price(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)
person_name = RandomMember.member_name(1)

# 批发商品资料
def test114():
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
    print('test114:进入批发→分组→商品管理→商品资料')
    # 批发管理
    driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/button[2]').click()

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    # 点击商品管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[6]/div[1]/span/span').click()
    time.sleep(time1)

    # 商品资料
    driver.find_element_by_link_text('商品资料').click()
    time.sleep(time1)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time1)

    # 商品款号
    spkh = driver.find_element_by_xpath('//*[@id="code"]')
    spkh.click()
    spkh.clear()
    spkh.send_keys(goods_number)

    # 商品品牌
    driver.find_element_by_xpath('//*[@id="brand"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
    time.sleep(time1)

    # 商品名称
    pp = driver.find_element_by_xpath('//*[@id="name"]')
    pp.click()
    pp.clear()
    pp.send_keys(goods_name)

    # 商品类别
    driver.find_element_by_xpath('//*[@id="type"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
    time.sleep(time1)


    # 季节
    driver.find_element_by_xpath('//*[@id="season"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()

    # 单位
    driver.find_element_by_xpath('//*[@id="unit"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()

    # 面料
    driver.find_element_by_xpath('//*[@id="shell_fabric"]/div/div/div').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[1]').click()

    # 里料
    driver.find_element_by_xpath('//*[@id="inside_fabric"]/div/div/div').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()

    # 颜色
    driver.find_element_by_xpath('//*[@id="color"]/div/div/div').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/ul/li[1]').click()

    # 尺码组
    driver.find_element_by_xpath('//*[@id="size_group"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()

    # 商品风格
    driver.find_element_by_xpath('//*[@id="style"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul/li[1]').click()

    # 洗衣规则
    driver.find_element_by_xpath('//*[@id="laundry"]/div/div/div[1]').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[12]/div/div//ul/li[1]').click()

    # 执行标准
    driver.find_element_by_xpath('//*[@id="standard"]/div/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[13]/div/div//ul/li[1]').click()

    # 安全类别
    driver.find_element_by_xpath('//*[@id="safetyclass"]/div/div/div').click()
    time.sleep(time1)
    driver.find_element_by_xpath('/html/body/div[14]/div/div//ul/li[1]').click()

    # 检验员
    person = driver.find_element_by_xpath('//*[@id="inspectors"]')
    person.click()
    person.clear()
    person.send_keys(person_name)



    # 指导定价
    zddj = driver.find_element_by_xpath('//*[@id="wholesale_price"]')
    zddj.click()
    zddj.clear()
    zddj.send_keys(price)

    # 批发价格
    lsjg = driver.find_element_by_xpath('//*[@id="wp_price"]')
    lsjg.click()
    lsjg.clear()
    lsjg.send_keys(retail)

    # 指导定价
    zddj = driver.find_element_by_xpath('//*[@id="price"]')
    zddj.click()
    zddj.clear()
    zddj.send_keys(price)

    # 零售价格
    lsjg = driver.find_element_by_xpath('//*[@id="retail_price"]')
    lsjg.click()
    lsjg.clear()
    lsjg.send_keys(retail)

    # 保存
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time2)

    # 抓取保存结果
    result = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    #判断是否成功
    if result == correct:
        print(goods_number + ":商品创建成功\n", "商品新增功能正常\n")
    else:
        print(result + "\n商品创建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    # 搜索输入商品款号
    sskh = driver.find_element_by_xpath('//*[@id="name"]')
    sskh.click()
    sskh.clear()
    sskh.send_keys(goods_number)
    #查询
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    #搜索款号名称结果
    sskhmc = driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/a').text
    if goods_number == sskhmc:
        print(goods_number + " 等于 " + sskhmc,"\n商品资料按名称搜索正常\n")
    else:
        print("商品名称搜索异常!!!!!!!!!")
    time.sleep(time1)

    # 编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[16]/div/a[1]/i').click()
    time.sleep(time2)

    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time2)
    # 抓取保存结果
    result1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result1 == correct:
        print(goods_number + ":商品编辑成功\n", "商品编辑功能正常\n")
    else:
        print(result1 + "\n商品编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 搜索输入商品款号
    sskh = driver.find_element_by_xpath('//*[@id="name"]')
    sskh.click()
    sskh.clear()
    sskh.send_keys(goods_number)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time1)

    #删除
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[16]/div/a[2]/i').click()
    time.sleep(time1)
    #确认
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)

    # 抓取删除结果
    result_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    # 判断是否成功
    if result_delect == correct:
        print(goods_number + ":商品删除成功\n", "商品删除功能正常\n")
    else:
        print(result_delect + "\n商品删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    driver.quit()