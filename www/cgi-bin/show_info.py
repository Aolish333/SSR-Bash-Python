#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import cgi
import urllib2

#取得本机外网IP
myip = urllib2.urlopen('http://members.3322.org/dyndns/getip').read()
myip=myip.strip()
#加载SSR JSON文件
f = file("/usr/local/shadowsocksr/mudb.json");
json = json.load(f);

# 接受表达提交的数据
form = cgi.FieldStorage() 

# 解析处理提交的数据
getport = form['port'].value
getpasswd = form['passwd'].value
#判断端口是否找到
portexist=0
passwdcorrect=0
#循环查找端口
for x in json:
	#当输入的端口与json端口一样时视为找到
	if(str(x[u"port"]) == str(getport)):
		portexist=1
		if(str(x[u"passwd"]) == str(getpasswd)):
			passwdcorrect=1
			jsonmethod=str(x[u"method"])
			jsonobfs=str(x[u"obfs"])
			jsonprotocol=str(x[u"protocol"])
		break

if(portexist==0):
	getport = "未找到此端口，请检查是否输入错误！"
	myip = ""
	getpasswd = ""
	jsonmethod = ""
	jsonprotocol = ""
	jsonobfs = ""

if(portexist!=0 and passwdcorrect==0):
	getport = "连接密码输入错误，请重试"
	myip = ""
	getpasswd = ""
	jsonmethod = ""
	jsonprotocol = ""
	jsonobfs = ""


header = '''
<!DOCTYPE HTML>
<html>
<head>
    <title>Ethereal by HTML5 UP</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
</head>
<body>
'''
footer = '''
<!-- Scripts -->
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/skel.min.js"></script>
<script src="assets/js/main.js"></script>

</body>
</html>
'''




#打印返回的内容
print header

formhtml = '''
<!-- Page Wrapper -->
<div id="page-wrapper">

    <!-- Wrapper -->
    <div id="wrapper">
						<section class="panel spotlight medium right" id="first">
							<div class="content span-7">
								<h1 class="major">连接的信息如下</h1>
								<p> <strong>服务器地址：</strong> %s <br>
									<strong>连接端口：</strong> %s <br>
									<strong>连接密码：</strong> %s <br>
									<strong>加密方式： </strong> %s <br>
									<strong>协议方式： </strong> <br> %s <br>
									<strong>混淆方式：</strong> <br>%s <br>
									<a href="index.html">点我返回首页</a></p>
							</div>
							<div class="image filtered tinted" data-position="top left">
								<img src="images/pic02.jpg" alt="" />
							</div>
						</section>


        <!-- Copyright -->
        <div class="copyright">&copy; Lincvic <a href="https://github.com/lincvic">Git</a>.</div>

    </div>

</div>
'''

print formhtml % (myip,getport,getpasswd,jsonmethod,jsonprotocol,jsonobfs)

print footer

f.close();

