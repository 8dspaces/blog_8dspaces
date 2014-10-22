<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>
##sqlalchemy学习教程[转]  

1. slqalchemy的版本  

        import sqlalchemy
        slqalchemy.__version__

2. 创建连接  

        :::python
        #数据库设置
        MYSQL_DB = 'clwy_cms'
        MYSQL_USER = 'root'
        MYSQL_PASS = ''
        MYSQL_HOST = '127.0.0.1'
        MYSQL_PORT = 3306

        from sqlalchemy import create_engine
        engine = create_engine(
                'mysql://%s:%s@%s:%s/%s?charset=utf8' % \
                (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT,MYSQL_DB), 
                encoding='utf8',
                echo=True,
                )

        #如果是连接sqlite
        #engine = create_engine('sqlite:///:memory:', echo=True)
        
3. 声明基类  

        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()
        
4. 定义表

        from sqlalchemy import Column, Integer, String
        class User(Base):
            __tablename__ = 'users'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            fullname = Column(String(50), nullable=False, default=False)
            password = Column(String(50))
            
            #nullalbe 不为空, defalut 默认值

            def __init__(self, name, fullname, password):
                self.name = name
                self.fullname = fullname
                self.password = password

            def __repr__(self):
                return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
                
    如果不写__init__,将会有一个默认的构造函数

5. 创建会话

        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine)
        
6. 常用操作

    绑定session后就可以进行一系列操作了哦

    先来一个添加的

        my_user = session.add(User('aaron','aaron lau', '123456789'))
        session.add(myUser)
        session.commit()
        #只有执行了commit()才是提交
    
    
##查询语句 

1. 第一种

        for instance in session.query(User).order_by(User.id):
            print instance.name, instance.fullname

2. 第二种

        for name, fullname in session.query(User.name, User.fullname):
            print name, fullname

3. 第三种 

        for row in session.query(User, User.name).all(): 
            print row.User, row.name

4. 第四种 切片的哦

        for u in session.query(User).order_by(User.id)[1:3]: 
            print u

5. 第五种 用filter()匹配的

        for name, in session.query(User.name).filter_by(fullname='Ed Jones'): 
            print name

6. 第六种 两次filter()  

        for user in session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones'): 
            print user
            
###常用filter()  

+ 等于

  `query.filter(User.name == 'ed')`

+ 不等于

  `query.filter(User.name != 'ed')`

+ 像

  `query.filter(User.name.like('%ed%'))`

+ 在 

  `query.filter(User.name.in_(['ed', 'aaron', 'jack']))`
  `query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))`

+ 不在

  `query.filter(~User.name.in_(['ed', 'wendy', 'jack']))`

+ 为空

  `filter(User.name == None)`

+ 不为空

  `filter(User.name != None)`

+ 和

        from sqlalchemy import and_
        filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
        filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

+ 或

        from sqlalchemy import or_
        filter(or_(User.name == 'ed', User.name == 'wendy'))

+ 匹配

        query.filter(User.name.match('wendy'))
        返回列表和标量
        query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
        query.all() #所有数据
        query.first() #第一条数据
        
        关联型数据库
        
        from sqlalchemy import ForeignKey
        from sqlalchemy.orm import relationship, backref
        class Address(Base):
            __tablename__ = 'addresses'
            id = Column(Integer, primary_key=True)
            email_address = Column(String, nullable=False)
            user_id = Column(Integer, ForeignKey('users.id'))
      
            user = relationship("User", backref=backref('addresses', order_by=id))

            def __init__(self, email_address):
                self.email_address = email_address

            def __repr__(self):
                return "<Address('%s')>" % self.email_address