# JsFak

## 背景：

 Author:0xAXSDD By Gamma安全实验室
 version:1.0
 explain:这是一款用户绕过前端js加密进行密码爆破的工具，你无需在意js加密的细节，只需要输入你想要爆破url，以及username输入框的classname，password输入框的classname，点击登录框classname,爆破用户名，密码字典等就可，暂时不支持带验证码校验的爆破
 ## 例子：
    只爆破密码：python JsFak.py -u url -user admin -Pd password.txt -cu user_classname -cp pass_classname -l login_classname
    爆破密码和用户：python main.py -ud username.txt -pd password.txt -cu user_classname -cp user_classname -l user_classname -u url
    详情功能参考  -h
    也可以指定输出结果文件：-f

    注意：如果遇到的classname  带空格  请用""括起来 Sever服务默认的是8080端口，如果需要修改，直接点Sever类修改，并指定参数-p


欢迎关注微信公众号"Gamma安全实验室"，接触最前线的安全骚操作，以及实用的好工具！
如果有任何bug，欢迎留言！

## 说明
请严格遵守网络安全法，切勿走上违法犯罪的道路，工具只用于安全技术研究，实验室不承担任何责任
