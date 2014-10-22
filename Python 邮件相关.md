# Python邮件相关（SMTP and email)

在我们实际收发邮件时常常会涉及到一些邮件相关的协议，如SMTP，POP，IMAP
简单理解SMTP是用来发邮件的， POP和IMAP是收邮件到本地


扯的稍微远一点，每个公司都有公司内部的SMTP服务器，绑定到公司自己的域名，负责对内外发邮件
常用的邮件服务提供商也就相当于提供给所有人的SMTP服务器，负责收发邮件（SMTP，IMAP，POP）
如163邮箱，就提供对应的这些服务。

如果你想把邮件download到本地，可以用outlook之类的软件绑定服务商提供的邮件服务器，来收发邮件。

一些参考：  
[什么是POP3、SMTP和IMAP?](http://help.163.com/09/1223/14/5R7P6CJ600753VB8.html)

在实际的测试中，自动化测试中当脚本检测到一些异常就可以发送邮件给对应的人或team, 所以在脚本中加一些发邮件的功能算是比较常见的需求
发送邮件主要用到了smtplib和email两个模块。 stmplib 可以帮助实现发邮件的需求， 而具体邮件的内容会涉及到email模块中的相关功能

### smtplib模块

**smtplib.SMTP([host[, port[, local_hostname[, timeout]]]])**

SMTP类构造函数，表示与SMTP服务器之间的连接，通过这个连接可以向smtp服务器发送指令，执行相关操作（如：登陆、发送邮件）。

+ host：smtp服务器主机名
+ port：smtp服务的端口，默认是25；如果在创建SMTP对象的时候提供了这两个参数，在初始化的时候会**自动调用connect方法**去连接服务器。
**Note**: smtplib模块还提供了SMTP_SSL类和LMTP类，对它们的操作与SMTP基本一致。


####smtplib.SMTP提供的方法：

+ SMTP.set_debuglevel(level)：设置是否为调试模式。默认为False，即非调试模式，表示不输出任何调试信息。
+ **SMTP.connect([host[, port]])**：连接到指定的smtp服务器。参数分别表示smpt主机和端口。注意: 也可以在host参数中指定端口号（如：smpt.yeah.net:25），这样就没必要给出port参数。
+ SMTP.docmd(cmd[, argstring])：向smtp服务器发送指令。可选参数argstring表示指令的参数。
+ SMTP.helo([hostname]) ：使用"helo"指令向服务器确认身份。相当于告诉smtp服务器“我是谁”。
+ SMTP.has_extn(name)：判断指定名称在服务器邮件列表中是否存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
+ SMTP.verify(address) ：判断指定邮件地址是否在服务器中存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
+ **SMTP.login(user, password)** ：登陆到smtp服务器。现在几乎所有的smtp服务器，都必须在验证用户信息合法之后才允许发送邮件。
+ **SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])** ：msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。  ---> 具体meg可以通过email 模块去实现。
+ **SMTP.quit()** ：断开与smtp服务器的连接，相当于发送"quit"指令。（很多程序中都用到了smtp.close()，具体与quit的区别google了一下，也没找到答案。）

### email模块

emial模块用来处理邮件消息,使用这些模块来定义邮件的内容，是非常简单的。其包括的类有（更加详细的介绍可见[官方文档](http://docs.python.org/library/email.mime.html)）

+ class email.mime.base.MIMEBase(_maintype, _subtype, **_params)：这是MIME的一个基类。一般不需要在使用时创建实例。其中_maintype是内容类型，如text或者image。_subtype是内容的minor type 类型，如plain或者gif。 **_params是一个字典，直接传递给Message.add_header()。
+ class email.mime.multipart.MIMEMultipart([_subtype[, boundary[, _subparts[, _params]]]]：MIMEBase的一个子类，多个MIME对象的集合，_subtype默认值为mixed。boundary是MIMEMultipart的边界，默认边界是可数的。
+ class email.mime.application.MIMEApplication(_data[, _subtype[, _encoder[, **_params]]])：MIMEMultipart的一个子类。
+ class email.mime.audio. MIMEAudio(_audiodata[, _subtype[, _encoder[, **_params]]])： MIME音频对象
+ class email.mime.image.MIMEImage(_imagedata[, _subtype[, _encoder[, **_params]]])：MIME二进制文件对象。
+ class email.mime.message.MIMEMessage(_msg[, _subtype])：具体的一个message实例，使用方法如下：
+ **class email.mime.text.MIMEText(_text[, _subtype[, _charset]]）**  
MIMEText对象，其中_text是邮件内容，_subtype邮件类型，可以是text/plain（普通文本邮件），html/plain(html邮件),  _charset编码，可以是gb2312等等。
+ 普通文本邮件

普通文本邮件发送的实现，关键是要将MIMEText中_subtype设置为plain。首先导入smtplib和mimetext。创建smtplib.smtp实例，connect邮件smtp服务器，login后发送，具体代码如下：（python2.6下实现）

    # -*- coding: UTF-8 -*-
    '''
    发送txt文本邮件
    小五义：http://www.cnblogs.com/xiaowuyi
    '''
    import smtplib  
    from email.mime.text import MIMEText  
    mailto_list=[YYY@YYY.com] 
    mail_host="smtp.XXX.com"  #设置服务器
    mail_user="XXXX"    #用户名
    mail_pass="XXXXXX"   #口令 
    mail_postfix="XXX.com"  #发件箱的后缀
      
    def send_mail(to_list,sub,content):  
        me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
        msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
        msg['Subject'] = sub  
        msg['From'] = me  
        msg['To'] = ";".join(to_list)  
        try:  
            server = smtplib.SMTP()  
            server.connect(mail_host)  
            server.login(mail_user,mail_pass)  
            server.sendmail(me, to_list, msg.as_string())  
            server.close()  
            return True  
        except Exception, e:  
            print str(e)  
            return False  
    if __name__ == '__main__':  
        if send_mail(mailto_list,"hello","hello world！"):  
            print "发送成功"  
        else:  
            print "发送失败"  
            
+ html邮件的发送

与text邮件不同之处就是将将MIMEText中_subtype设置为html。具体代码如下：（python2.6下实现）

    # -*- coding: utf-8 -*-
    '''
    发送html文本邮件
    小五义：http://www.cnblogs.com/xiaowuyi
    '''
    import smtplib  
    from email.mime.text import MIMEText  
    mailto_list=["YYY@YYY.com"] 
    mail_host="smtp.XXX.com"  #设置服务器
    mail_user="XXX"    #用户名
    mail_pass="XXXX"   #口令 
    mail_postfix="XXX.com"  #发件箱的后缀
      
    def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
        me="hello"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
        msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
        msg['Subject'] = sub    #设置主题
        msg['From'] = me  
        msg['To'] = ";".join(to_list)  
        try:  
            s = smtplib.SMTP()  
            s.connect(mail_host)  #连接smtp服务器
            s.login(mail_user,mail_pass)  #登陆服务器
            s.sendmail(me, to_list, msg.as_string())  #发送邮件
            s.close()  
            return True  
        except Exception, e:  
            print str(e)  
            return False  
    if __name__ == '__main__':  
        if send_mail(mailto_list,"hello","<a href='http://www.cnblogs.com/xiaowuyi'>小五义</a>"):  
            print "发送成功"  
        else:  
            print "发送失败"  
            
+ 发送带附件的邮件

发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。

    # -*- coding: utf-8 -*-
    '''
    发送带附件邮件
    小五义：http://www.cnblogs.com/xiaowuyi
    '''

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import smtplib

    #创建一个带附件的实例
    msg = MIMEMultipart()

    #构造附件1
    att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="123.doc"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)

    #构造附件2
    att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="123.txt"'
    msg.attach(att2)

    #加邮件头
    msg['to'] = 'YYY@YYY.com'
    msg['from'] = 'XXX@XXX.com'
    msg['subject'] = 'hello world'
    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect('smtp.XXX.com')
        server.login('XXX','XXXXX')#XXX为用户名，XXXXX为密码
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        print '发送成功'
    except Exception, e:  
        print str(e) 
        
+ 利用MIMEimage发送图片

    # -*- coding: utf-8 -*-

    import smtplib
    import mimetypes
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage

    def AutoSendMail():
        msg = MIMEMultipart()
        msg['From'] = "XXX@XXX.com"
        msg['To'] = "YYY@YYY.com"
        msg['Subject'] = "hello world"


        txt = MIMEText("这是中文的邮件内容哦",'plain','gb2312')     
        msg.attach(txt)
        

        file1 = "C:\\hello.jpg"
        image = MIMEImage(open(file1,'rb').read())
        image.add_header('Content-ID','<image1>')
        msg.attach(image)
        
        
        server = smtplib.SMTP()
        server.connect('smtp.XXX.com')
        server.login('XXX','XXXXXX')
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
        
    if __name__ == "__main__":
        AutoSendMail()

## 总结

+ smtplib.SMTP()
    + connect()
    + login()
    + sendmail()
    + quit()
+ MIMEText  #email.mime.text.MIMEText
    + msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    + msg['Subject'] = sub  
    + msg['From'] = me  
    + msg['To'] = ";".join(to_list) 