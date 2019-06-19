import time
from selenium import webdriver
from tool.random.randomGoods import RandomGoods
from tool.time.loadingTime import LoadTime
from wholesale.group.procurement.login import Login
from tool.time.nowTime import nowTime

url = Login.location(1)
login_name = Login.name(1)
login_pwd = Login.password(1)
brand = RandomGoods.brand(1)
tim = nowTime()
goods_type = RandomGoods.goods_type(1)
goods_mianliao = RandomGoods.goods_materials(1)
goods_liliao = RandomGoods.goods_liliao(1)
goods_unit = RandomGoods.goods_unit(1)
goods_colour = RandomGoods.goods_colour(1)
season = RandomGoods.goods_season(1)
xidi_name = RandomGoods.goods_xidi(1)
order = RandomGoods.goods_order(1)
norm = RandomGoods.norm(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

# 零售商品资料
def test115():
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

    # 分组
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/section/main/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()
    time.sleep(time2)

    # 点击商品管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/aside/div/ul/li[6]/div[1]/span/span').click()

    time.sleep(time1)

    # 商品资料
    driver.find_element_by_link_text('属性管理').click()
    time.sleep(time2)
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 品牌名称输入
    spkh = driver.find_element_by_xpath(
        '//*[@id="name"]')
    spkh.click()
    spkh.clear()
    spkh.send_keys(brand)
    # 供应商选择
    driver.find_element_by_xpath('//*[@id="supplier_id"]/div/div/div[1]').click()
    time.sleep(time2)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()

    # 品牌备注
    ppbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys("品牌备注" + tim)
    # 品牌保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)


    # 抓取结果
    result = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result == correct:
        print(brand + ":品牌新增成功\n", "品牌新建功能正常\n")
    else:
        print(result + "\n品牌新增异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 品牌搜索输入
    ppbz = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys(brand)

    #查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索款号名称结果
    ssppm = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if brand == ssppm:
        print(brand + "等于" + ssppm, "\n品牌搜索功能正常\n")
    else:
        print("品牌名称搜索异常!!!!!")
    time.sleep(time2)

    # 品牌编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[5]/div/a[1]/i').click()
    time.sleep(time2)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)

    # 抓取结果
    result1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result1 == correct:
        print(brand + ":品牌编辑成功\n", "品牌编辑功能正常\n")
    else:
        print(result1 + "\n品牌编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 品牌搜索输入
    ppbz = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys(brand)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 品牌删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[5]/div/a[2]/i').click()
    time.sleep(time2)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time2)

    # 抓取删除结果
    result2 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result2 == correct:
        print(brand + ":品牌删除成功\n", "品牌删除功能正常\n")
    else:
        print(result2 + "\n品牌删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    time.sleep(time2)


    # 定位执行标准
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 标准名称输入
    bzmc = driver.find_element_by_xpath(
        '//*[@id="name"]')
    bzmc.click()
    bzmc.clear()
    bzmc.send_keys(norm)

    # 保存
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_neibie1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('新增成功')
    # 判断是否成功
    if result_neibie1 == correct:
        print(norm + ":商品执行标准新建成功\n", "执行标准新建功能正常\n")
    else:
        print(result_neibie1 + "\n执行标准新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 执行标准搜索输入
    zxbzsr = driver.find_element_by_xpath(
        '//*[@id="title"]')
    zxbzsr.click()
    zxbzsr.clear()
    zxbzsr.send_keys(norm)

    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[2]/div[2]/div/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索款号名称结果
    sslb1 = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if norm == sslb1:
        print(norm + " 等于 " + sslb1, "\n执行标准搜索功能正常\n")
    else:
        print("执行标准搜索异常!!!!!!!")
    time.sleep(time1)

    # 标准编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_neibie11 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_neibie11 == correct:
        print(norm + ":执行标准编辑成功\n", "执行标准编辑功能正常\n")
    else:
        print(result_neibie11 + "\n执行标准编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 执行标准搜索输入
    zxbzsr = driver.find_element_by_xpath(
        '//*[@id="title"]')
    zxbzsr.click()
    zxbzsr.clear()
    zxbzsr.send_keys(norm)

    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[2]/div[2]/div/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 标准删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time2)
    # 抓取结果
    result_neibie1_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_neibie1_delect == correct:
        print(norm + ":执行标准删除成功\n", "标准删除功能正常\n")
        time.sleep(time1)
    else:
        print(result_neibie1_delect + "\n执行标准删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time1)




    # 定位商品类别
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 类别名称输入
    lbsr = driver.find_element_by_xpath(
        '//*[@id="name"]')
    lbsr.click()
    lbsr.clear()
    lbsr.send_keys(goods_type)

    # 备注
    ppbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys("类别备注" + tim)
    # 类别保存
    driver.find_element_by_xpath(
         '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_neibie = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_neibie == correct:
        print(goods_type + ":商品类别新建成功\n", "类别新建功能正常\n")
    else:
        print(result_neibie + "\n类别新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 类别搜索输入
    ppbz = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys(goods_type)

    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索类别名称结果
    sslb = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if goods_type == sslb:
        print(goods_type + " 等于 " + sslb, "\n类别搜索功能正常\n")
    else:
        print("类别搜索异常!!!!!!!")
    time.sleep(time1)

    # 类别编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[4]/div/a[1]/i').click()
    time.sleep(time1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_neibie1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_neibie1 == correct:
        print(goods_type + ":商品类别编辑成功\n", "类别编辑功能正常\n")
    else:
        print(result_neibie1 + "\n类别编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 类别搜索输入
    ppbz = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ppbz.click()
    ppbz.clear()
    ppbz.send_keys(goods_type)

    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 类别删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[4]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time2)
    # 抓取结果
    result_neibie1_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_neibie1_delect == correct:
        print(goods_type + ":商品类别删除成功\n", "类别删除功能正常\n")
        time.sleep(time1)
    else:
        print(result_neibie1_delect + "\n类别删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(time1)

    # 定位面料管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 面料名称输入
    mlsr = driver.find_element_by_xpath(
        '//*[@id="name"]')
    mlsr.click()
    mlsr.clear()
    mlsr.send_keys(goods_mianliao)

    # 面料保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_mianliao = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_mianliao == correct:
        print(goods_mianliao + ":面料新建成功\n", "面料新建功能正常\n")
    else:
        print(result_mianliao + "\n面料新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 面料搜索输入
    mlss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    mlss.click()
    mlss.clear()
    mlss.send_keys(goods_mianliao)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索面料名称结果
    ssmljg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if goods_mianliao == ssmljg:
        print(goods_mianliao + " 等于 " + ssmljg, "\n面料搜索功能正常\n")
    else:
        print("面料搜索异常")
    time.sleep(time2)

    # 面料编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[1]/i').click()
    time.sleep(1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_mianliao1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_mianliao1 == correct:
        print(goods_mianliao + ":面料编辑成功\n", "面料编辑功能正常\n")
    else:
        print(result_mianliao1 + "\n面料编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 面料搜索输入
    mlss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    mlss.click()
    mlss.clear()
    mlss.send_keys(goods_mianliao)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 面料删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_mianliao_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_mianliao_delect == correct:
        print(goods_mianliao + ":面料删除成功\n", "面料删除功能正常\n")
    else:
        print(result_mianliao_delect + "\n面料删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)


    # 定位里料管理
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[5]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 里料名称输入
    llsr = driver.find_element_by_xpath(
        '//*[@id="name"]')
    llsr.click()
    llsr.clear()
    llsr.send_keys(goods_liliao)

    # 里料保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_liliao = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_liliao == correct:
        print(goods_liliao + ":里料新建成功\n", "里料新建功能正常\n")
    else:
        print(result_liliao + "\n里料新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 里料搜索输入
    llss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    llss.click()
    llss.clear()
    llss.send_keys(goods_liliao)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索里料名称结果
    llsrjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if goods_liliao == llsrjg:
        print(goods_liliao + " 等于 " + llsrjg, "\n里料搜索功能正常\n")
    else:
        print("里料搜索异常")
    time.sleep(time2)

    # 里料编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[1]/i').click()
    time.sleep(1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_liliao1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_liliao1 == correct:
        print(goods_liliao + ":里料编辑成功\n", "里料编辑功能正常\n")
    else:
        print(result_mianliao1 + "\n里料编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 里料搜索输入
    llss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    llss.click()
    llss.clear()
    llss.send_keys(goods_liliao)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 里料删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_liliao_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_liliao_delect == correct:
        print(goods_liliao + ":里料删除成功\n", "里料删除功能正常\n")
    else:
        print(result_liliao_delect + "\n面料删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 计量单位
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[6]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 计量名称输入
    jldw = driver.find_element_by_xpath(
        '//*[@id="name"]')
    jldw.click()
    jldw.clear()
    jldw.send_keys(goods_unit)

    # 单位保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_unit = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_unit == correct:
        print(goods_unit + ":单位新建成功\n", "单位新建功能正常\n")
    else:
        print(result_unit + "\n单位新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 单位搜索输入
    dwss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    dwss.click()
    dwss.clear()
    dwss.send_keys(goods_unit)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索单位名称结果
    jwsrjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if goods_unit == jwsrjg:
        print(goods_unit + " 等于 " + jwsrjg, "\n单位搜索功能正常\n")
    else:
        print("单位搜索异常")
    time.sleep(time2)

    # 单位编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[1]/i').click()
    time.sleep(1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_unit1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_unit1 == correct:
        print(goods_unit + ":单位编辑成功\n", "单位编辑功能正常\n")
    else:
        print(result_unit1 + "\n单位编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 单位搜索输入
    dwss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    dwss.click()
    dwss.clear()
    dwss.send_keys(goods_unit)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 单位删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[6]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_unit_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_unit_delect == correct:
        print(goods_unit + ":单位删除成功\n", "单位删除功能正常\n")
    else:
        print(result_unit_delect + "\n单位删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    time.sleep(time1)


    # 颜色
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[7]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 颜色名称输入
    ysmc = driver.find_element_by_xpath(
        '//*[@id="name"]')
    ysmc.click()
    ysmc.clear()
    ysmc.send_keys(goods_colour)

    # 颜色备注
    ysbz = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    ysbz.click()
    ysbz.clear()
    ysbz.send_keys('颜色' + tim)

    # 颜色保存
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    except:
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[5]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_colour = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_colour == correct:
        print(goods_colour + ":颜色新建成功\n", "颜色新建功能正常\n")
    else:
        print(result_colour + "\n单位新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 颜色搜索输入
    yssss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    yssss.click()
    yssss.clear()
    yssss.send_keys(goods_colour)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索颜色名称结果
    ysssjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]').text
    if goods_colour == ysssjg:
        print(goods_colour + " 等于 " + ysssjg, "\n颜色搜索功能正常\n")
    else:
        print("颜色搜索异常")
    time.sleep(time2)

    # 颜色编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[4]/div/a[1]/i').click()
    time.sleep(1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_colour1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_colour1 == correct:
        print(goods_colour + ":颜色编辑成功\n", "颜色编辑功能正常\n")
    else:
        print(result_colour1 + "\n颜色编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 颜色搜索输入
    yssss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    yssss.click()
    yssss.clear()
    yssss.send_keys(goods_colour)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)


    # 颜色删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[7]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[4]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_colour_delect = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_colour_delect == correct:
        print(goods_colour + ":颜色删除成功\n", "颜色删除功能正常\n")
    else:
        print(result_colour_delect + "\n颜色删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    time.sleep(time1)

    # 季节
    driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[8]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 季节名称输入
    jjmc = driver.find_element_by_xpath(
        '//*[@id="name"]')
    jjmc.click()
    jjmc.clear()
    jjmc.send_keys(season)


    # 季节保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_season = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_season == correct:
        print(season + ":季节新建成功\n", "季节新建功能正常\n")
    else:
        print(result_season + "\n季节新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time2)

    # 季节搜索输入
    jjsssr = driver.find_element_by_xpath(
        '//*[@id="name"]')
    jjsssr.click()
    jjsssr.clear()
    jjsssr.send_keys(season)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索颜色名称结果
    jjssjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if season == jjssjg:
        print(season + " 等于 " + jjssjg, "\n季节搜索功能正常\n")
    else:
        print("季节搜索异常!!!!!!!!!\n")
    time.sleep(time2)

    # 季节编辑
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[1]/i').click()
    time.sleep(1)
    # 保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_season1 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_season1 == correct:
        print(season + ":季节编辑成功\n", "季节编辑功能正常\n")
    else:
        print(result_season1 + "\n季节编辑异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 季节搜索输入
    jjsssr = driver.find_element_by_xpath(
        '//*[@id="name"]')
    jjsssr.click()
    jjsssr.clear()
    jjsssr.send_keys(season)
    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)

    # 季节删除
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[8]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[2]/div/a[2]/i').click()
    time.sleep(time1)
    # 确认删除
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_season2 = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_season2 == correct:
        print(season + ":季节删除成功\n", "季节删除功能正常\n")
    else:
        print(result_season2 + "\n季节删除异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    time.sleep(time1)

    # 洗涤服务
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[9]').click()
    time.sleep(time1)
    # 新增
    driver.find_element_by_link_text('新增').click()
    time.sleep(time2)

    # 洗涤规格名称输入
    xdgg = driver.find_element_by_xpath(
        '//*[@id="name"]')
    xdgg.click()
    xdgg.clear()
    xdgg.send_keys(xidi_name)
    # 是否包洗
    driver.find_element_by_xpath(
        '//*[@id="is_contract"]/div/div').click()
    # 包洗
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()

    # 排序序号
    pxxh = driver.find_element_by_xpath(
        '//*[@id="code"]')
    pxxh.click()
    pxxh.clear()
    pxxh.send_keys(order)

    # 总计包洗
    pxxh = driver.find_element_by_xpath(
        '//*[@id="total"]')
    pxxh.click()
    pxxh.clear()
    pxxh.send_keys(order)

    # 年度包洗
    pxxh = driver.find_element_by_xpath(
        '//*[@id="year_total"]')
    pxxh.click()
    pxxh.clear()
    pxxh.send_keys(order)

    # 备注
    pxxh = driver.find_element_by_xpath(
        '//*[@id="comment"]')
    pxxh.click()
    pxxh.clear()
    pxxh.send_keys("洗涤备注" + tim)

    # 洗涤保存
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[9]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
    time.sleep(time1)
    # 抓取结果
    result_xidi = driver.find_element_by_xpath(
        '/html/body/div[2]/div/span/div/div/div/span').text
    correct = ('操作成功')
    # 判断是否成功
    if result_xidi == correct:
        print(xidi_name + ":洗涤新增成功\n", "洗涤新建功能正常\n")
    else:
        print(result_xidi + "\n洗涤新建异常!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(time1)

    # 洗涤搜索输入
    xdss = driver.find_element_by_xpath(
        '//*[@id="name"]')
    xdss.click()
    xdss.clear()
    xdss.send_keys(xidi_name)

    # 查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[9]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
    time.sleep(time2)
    # 搜索洗涤名称结果
    xdcxjg = driver.find_element_by_xpath(
        '//*[@id="root"]/section/section/main/div/div[3]/div/div[2]/div[3]/div[9]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
    if xidi_name == xdcxjg:
        print(xidi_name + " 等于 " + xdcxjg, "\n洗涤搜索功能正常\n")
    else:
        print("洗涤搜索异常!!!!!!!!!")
    time.sleep(time1)
    driver.quit()