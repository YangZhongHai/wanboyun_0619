import time
from selenium.webdriver import ActionChains  # 鼠标双击模块
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from wholesale.group.procurement.login import Login
from tool.random.randomGoods import RandomGoods
from tool.random.randomMember import RandomMember
from tool.time.loadingTime import LoadTime
from tool.time.nowTime import nowTime