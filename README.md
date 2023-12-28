secure_system下settings设置邮件发送功能

![image-20231228103727150](https://img-1303964016.cos.ap-chengdu.myqcloud.com/typora_image/image-20231228103727150.png)

设置数据库连接

![image-20231228103812614](https://img-1303964016.cos.ap-chengdu.myqcloud.com/typora_image/image-20231228103812614.png)

终端运行：

> 首先进行数据库迁移
>
> python manage.py migrate 
>
> 
>
> 创建超级管理员账户
>
> python manage.py createsuperuser
>
> 
>
> 启动（没有启用ssl）
>
> python .\manage.py runserver
>
> 
>
> 启动（启用ssl）
>
> python manage.py runserver_plus --cert server.crt 127.0.0.1:7000
>
> 其中server.crt是自签名证书
>
> 步骤：
>
> 首先安装相关包
>
> ```
> pip install django-extensions
> pip install django-werkzeug-debugger-runserver
> pip install pyOpenSSL
> ```
>
> 解压目录下的创建ssl证书的工具，openssl-0.9.8k_WIN32.zip
>
> 解压后找到解压目录的bin文件件，找到openssl.exe文件，双击打开指令窗口，输入如下指令进行配置，每执行一条指令，均需要配置相关参数，随意填写均可
>
> ```
> 1、genrsa -des3 -out server.key 2048
> 2、req -new -key server.key -out server.csr -config openssl.cnf
> 3、rsa -in server.key -out server_no_passwd.key
> 4、x509 -req -days 365 -in server.csr -signkey server_no_passwd.key -out server.crt
> ```
>
> 这样即可生成server.crt证书，放到Secure-identity-authentication根目录即可



运行之后效果

![image-20231228105021548](https://img-1303964016.cos.ap-chengdu.myqcloud.com/typora_image/image-20231228105021548.png)

![image-20231228105059278](https://img-1303964016.cos.ap-chengdu.myqcloud.com/typora_image/image-20231228105059278.png)

![image-20231228105109129](https://img-1303964016.cos.ap-chengdu.myqcloud.com/typora_image/image-20231228105109129.png)