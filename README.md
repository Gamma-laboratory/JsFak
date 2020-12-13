# JsFak

## 背景：

#### Author:0xAXSDD By Gamma安全实验室
#### version:1.0
#### explain:这是一款用户绕过前端js加密进行密码爆破的工具，你无需在意js加密的细节，只需要输入你想要爆破url，以及username输入框的classname，password输入框的classname，点击登录框classname,爆破用户名，密码字典等就可，暂时不支持带验证码校验的爆破
 ## 例子：
    只爆破密码：```python JsFak.py -u url -user admin -Pd password.txt -cu user_classname -cp pass_classname -l login_classname```
    爆破密码和用户：```python main.py -ud username.txt -pd password.txt -cu user_classname -cp user_classname -l user_classname -u url```
    详情功能参考  -h
    也可以指定输出结果文件：-f

    注意：如果遇到的classname  带空格  请用""括起来 Sever服务默认的是8080端口，如果需要修改，直接点Sever类修改，并指定参数-p,填入的类名一定要是input标签的哟
    
    该工具还有局限性，因为只是我实战时遇到的一个站，所以按需开发，如果有什么好的建议想法欢迎和我交流


欢迎关注微信公众号"Gamma安全实验室"，接触最前线的安全骚操作，以及实用的好工具！
如果有任何bug，欢迎留言！

## 说明:
请严格遵守网络安全法，切勿走上违法犯罪的道路，工具只用于安全技术研究，实验室不承担任何责任

## 安装说明：

工具使用的是python3的环境，python2会报错，请大家运行切换到python3的环境

因为在最初的设计的时候，没想那么多，只想的能爆破密码账号就好，所以工具环境具有局限性，默认是本机安装chrome浏览器，这里没有用chromedriver，如果想用的自行修改源码。

### 1.安装chromedriver

自带chromederiver，如果想自己指定，需修改源码配置

### 2.安装selenium

selenium可以直接可以用pip安装。

```
pip install selenium
```

### 3.下载browsermobproxy

源码以及附带了一个browsermobproxy文件，所以就不需要下载，如果需要重新下载，还得修改源码重新指定。
### 4.安装python -browsermobproxy包

```
pip install browsermob-proxy
```
### 5.无法通过class来查找input标签
如果通过input没有class属性就必须更换查找的方式了，可以通过id，什么的
参考：
```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
多个元素选取
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
```
