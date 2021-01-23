#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/21 11:12
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

https://www.cnblogs.com/denise1108/p/10339068.html
"""

from selenium.webdriver.common.by import By
from jjsht import htmain
import time,unittest


class ht_testcase(unittest.TestCase):
    url = 'http://172.16.22.100/jjslogin/tologin'
    # url = 'https://www.baidu.com/'
    browser = 'Chrome'
    empno = '000012'
    password = '1'

    @classmethod
    def setUpClass(cls):  # 必须使用 @ classmethod装饰器, 所有test运行之前运行一次
        print('-----------开始智能合同web自动化巡检--------------')

    @classmethod
    def tearDownClass(cls):  # 必须使用 @ classmethod装饰器, 所有test运行结束后运行一次
        print('-----------结束智能合同web自动化巡检--------------')

    def setUp(self):  # 每条用例执行之前都会先执行它
        print('开始执行用例')

    def tearDown(self):  # 每条用例执行之后都会执行它
        print('结束执行用例')


    def test_ht001(self):
        '''进入智能合同'''
        print('开始执行用例：进入智能合同')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        info = p.browser.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/a[1]').text
        print(info)
        #校验
        self.assertEqual(info,'智能合同管理列表',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht002(self):
        '''智能合同列表通过编号搜索'''
        print('开始执行用例：智能合同列表通过编号搜索')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME,'htNumber','MM-0001')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print(info)
        # 校验
        self.assertEqual(info,'二手房买卖及居间服务合同',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht003(self):
        '''智能合同列表通过合同名称搜索'''
        print('开始执行用例：智能合同列表通过合同名称搜索')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME, 'htName', '二手房买卖及居间服务合同')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print(info)
        # 校验
        self.assertEqual(info,'二手房买卖及居间服务合同',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht004(self):
        '''智能合同列表通过业务类型搜索'''
        print('开始执行用例：智能合同列表通过业务类型搜索')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.combo-input.text-input')
        p.Time(1)
        p.ClickElement(By.XPATH, '//*[@id="searchForm"]/div[3]/div/ul/li[3]')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[4]').text
        print(info)
        # 校验
        self.assertEqual(info,'二手买卖',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht005(self):
        '''智能合同列表通过组合搜索'''
        print('开始执行用例：智能合同列表通过组合搜索')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME, 'htNumber', 'MM-0001')
        p.Time(1)
        p.ImputElement(By.NAME, 'htName', '二手房买卖及居间服务合同')
        p.Time(1)
        p.ClickElement(By.CSS_SELECTOR,'.combo-input.text-input')
        p.Time(1)
        p.ClickElement(By.XPATH, '//*[@id="searchForm"]/div[3]/div/ul/li[3]')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print(info)
        # 校验
        self.assertEqual(info,'二手房买卖及居间服务合同',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht006(self):
        '''智能合同列表搜索点击重置'''
        print('开始执行用例：智能合同列表搜索点击重置')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.XPATH,'//*[@id="resetBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[4]').text
        print(info)
        # 校验
        self.assertEqual(info,'二手买卖',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht007(self):
        '''进入创建智能合同页面一'''
        print('开始执行用例：进入创建智能合同页面一')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.btn.btn-primary.fr')#点击创建智能合同按钮
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="createButton"]').text
        print(info)
        # 校验
        self.assertEqual(info,'创建',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht008(self):
        '''进入创建智能合同页面一点击取消'''
        print('开始执行用例：进入创建智能合同页面一点击取消')
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.btn.btn-primary.fr')#点击创建智能合同按钮
        p.Time(2)
        p.ClickElement(By.XPATH,'//*[@id="backBtn"]')
        p.Time(2)
        info = p.browser.find_element_by_xpath('//*[@id="orderTablePeople"]/thead/tr/td[4]').text
        print(info)
        # 校验
        self.assertEqual(info,'业务类型',msg='执行失败')
        p.Time(2)
        p.Close()
        p.Quit()