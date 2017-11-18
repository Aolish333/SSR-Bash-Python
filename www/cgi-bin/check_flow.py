#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import cgi

# <p class="card-heading">端口：%s</p>
# <p>
# 已使用流量：%s %s <br>
# 总流量限制：%s %s </br></br>
# <a href="../index.html"><button class="btn" type="button">返回</button></a>
# </p>

f = file("/usr/local/shadowsocksr/mudb.json");
json = json.load(f);

# 接受表达提交的数据
form = cgi.FieldStorage() 

# 解析处理提交的数据
getport = form['port'].value

#判断端口是否找到
portexist=0

#循环查找端口
for x in json:
	#当输入的端口与json端口一样时视为找到
	if(str(x[u"port"]) == str(getport)):
		portexist=1
		transfer_enable_int = int(x[u"transfer_enable"])/1024/1024;
		d_int = int(x[u"d"])/1024/1024;
		transfer_unit = "MB"
		d_unit = "MB"

		#流量单位转换
		if(transfer_enable_int > 1024):
			transfer_enable_int = transfer_enable_int/1024
			transfer_unit = "GB"
		if(transfer_enable_int > 1024):
			d_int = d_int/1024
			d_unit = "GB"
		break

if(portexist==0):
	getport = "未找到此端口，请检查是否输入错误！"
	d_int = ""
	d_unit = ""
	transfer_enable_int = ""
	transfer_unit = ""







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

        <!-- Panel (Banner) -->
        <section class="panel banner right">
            <div class="content color0 span-3-75">
                <h1 class="major">端口： %s<br /></h1>
                <p>已使用流量： %s %s <br> 总流量限制： %s %s
                <br><a href="index.html">点我返回首页</a></p>
            </div>
            <div class="image filtered span-1-75" data-position="25% 25%">
                <img src="images/pic01.jpg" alt="" />
            </div>
        </section>


        <!-- Copyright -->
        <div class="copyright">&copy; Lincvic <a href="https://github.com/lincvic">Git</a>.</div>

    </div>

</div>



'''
print formhtml % (getport,d_int,d_unit,transfer_enable_int,transfer_unit)
print footer
f.close();

