import time
from selenium import webdriver

from tool.random.randomGoods import RandomGoods
from tool.time.loadingTime import LoadTime
from wholesale.group.procurement.login import Login

url = Login.location(1)
addname = Login.name(1)
addpwd = Login.password(1)
#商品款号
goods_number = RandomGoods.goods_number(1)
#商品名称
goodname = RandomGoods.goods_name(1)
# 指导定价
price = RandomGoods.price(1)
# 零售价
retail = RandomGoods.retail_price(1)
time1 = LoadTime.time1(1)
time2 = LoadTime.time2(1)
time3 = LoadTime.time3(1)

# 库存信息
def test10():
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
        name.send_keys(addname)

        # 输入密码
        pwd=driver.find_element_by_id('pwd')
        pwd.click()
        pwd.clear()
        pwd.send_keys(addpwd)

        # 登陆
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[3]/div/div/span/button').click()

        # 零售业务
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button[1]').click()

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/div/a').click()

        # 点击库存管理
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[5]/div[1]/span/span').click()
        print('test7:进入零售→店铺→库存管理→库存信息')
        time.sleep(time1)

        # 库存信息
        driver.find_element_by_link_text('库存信息').click()
        time.sleep(time1)

        driver.find_element_by_xpath('').click()
        time.sleep(time1)

        # 商品款号
        spkh = driver.find_element_by_xpath('//*[@id="code"]')
        spkh.click()
        spkh.clear()
        spkh.send_keys(goods_number)

        # 商品品牌
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[1]/div[3]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
        time.sleep(time1)

        # 商品名称
        pp = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div[1]/div/div[2]/div/span/input')
        pp.click()
        pp.clear()
        pp.send_keys(goodname)

        # 商品类别
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div[3]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
        time.sleep(time1)


        # 季节
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div[5]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()

        # 单位
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/span/div/div/div/div[1]').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()

        # 面料
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[3]/div[3]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[1]').click()

        # 里料
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[3]/div[5]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()

        # 颜色
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[4]/div[1]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/ul/li[1]').click()

        # 尺码组
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[4]/div[3]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()

        # 商品风格
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/form/div[5]/div[1]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(time2)
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul/li[1]').click()


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
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(time3)
        print(goodname + ":商品创建成功\n","商品新增功能正常\n")

        # 搜索输入商品款号
        sskh = driver.find_element_by_xpath('//*[@id="name"]')
        sskh.click()
        sskh.clear()
        sskh.send_keys(goods_number)
        #搜索
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[1]/form/div[2]/div/button[1]').click()
        time.sleep(time2)
        #搜索款号名称结果
        sskhmc = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div').text
        if goodname == sskhmc:
            print(goodname + "等于" + sskhmc,"\n商品资料按名称搜索正常")
        else:
            print("商品名称搜索异常")
        time.sleep(time1)
    except:
        print('商品资料异常')

    finally:
        driver.close()