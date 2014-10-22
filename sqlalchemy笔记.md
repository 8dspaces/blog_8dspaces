<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

#SQLAlchemy笔记

SQLAlchemy是最优秀的Python ORM(Object Relational **Mapper**) library


## SA layer
 
+ Raw sql   

    `seesion.execute("SELECT * FROM users;")`
    
    防止sql Injectiion   
    `session.execute(text("DELETE FROM students WHERE id = :id", {id: 3}))`
    
+ sql Expression Language(Level 1)

    `select([users]).all()`
    
+ ORM(Level 2)

    `Session.query(User).all()`
    
## engine
一切的开始……  
用于和不同的数据库建立连接

    from sqlalchemy import create_engine
    
    engine = create_engine(r'sqlite://db.sqlite', echo = False)
    
    
## declative 

+ old style mapping(still work)   

        # 创建Table
        users_table = Table('users', metadata,            Column('id', Integer, primary_key=True),            Column('name', Unicode),            Column('fullname', Unicode),        )
        # 创建类        class User:            pass
        # 将类和Table连接起来        mapper(User, users_table)

+ new style  
新的方式，使用declative 方式，将table和类的创建和mapper自动完成
        
        from sqlalchemy.ext.declarative import declarative_base
         
        Base = delcarative_base()

        class User(Base): 
            __tablename__ = "users"
                        id = Column(Integer, primary_key=True)            name = Column(Unicode)            fullname = Column(Unicode)
        Base = declarative_base()
        metadata = Base.metadata
        
        metadata.create_all(engine)## Session 
    rick = User.query.get(13)    rick.fullname = "Bob"    ... elsewhere in the galaxy "Codebase"    logged_in = User.query.get(13)     print logged_in.fullname    >>> Bob
Seesion: let's make some 
    from sqlalchemy import create_engine from sqlalchemy.orm import sessionmaker
        engine = create_engine(...)    # create a configured "Session" class    Session = sessionmaker(bind=some_engine) # create a Session    session = Session()    rick = User('rick', 'Rick Harding')    session.add(rick)    session.commit()#### put it together 
    Session = sessionmaker(bind=engine)    Base = declarative_base()    Base.metadata.bind = engine        # turns docs Session.query(User) into User.query   ----> Important     Base.query = Session.query_property(Query)
        class User(Base): ...        
## Query 
### get(对应SQL select)

Query 是数据库最基本的操作

+ User.query.get(**primary_key**)


### Query --> filter (对应where)

    User.query.filter(User.username == 'rick')    User.query.filter(User.username != 'rick').\           filter(User.age > someage)    User.query.filter(User.username.in_('rick', 'bob')).\           filter(User.bio.contains('science'))    User.query.filter(or_(User.username == 'rick', User.username == 'bob'))

### Firing off the query
+ `.one() `    - exception + `.first() `  - None+ `.all() `    - empty list
### Other query accessories  
+ `.group_by()`+ `.count()`+ `.order_by()`+ `.limit()`+ `.having()`
## Other tricks 
+ ### autoload  

      # does a query against the database at load time to 
      # load the columns
          users_table = Table('users', meta, autoload=True)      class User(object):           pass              mapper...
+ ### autoload declarative 
    class User(Base): 
        __tablename__ = 'users'         __table_args__ = (                UniqueConstraint('fullname'),                {'autoload':True}            )
+ ### fitting to an existing db
        create table Users ( UserID INTEGER,            UserFirstName CHAR(20),            UserLastName CHAR(40)        )        class User(Base):             ...            id = Column('UserID', Integer, primary_key=True)             fname = Column('UserFirstName',Unicode(20))             lname = Column('UserLastName', Unicode(40)            

+ ### Python properties 

      class User(Base):          _password = Column('password', Unicode(60))
          def _set_password(self, password):              salt = bcrypt.gensalt(10)              hashed_password = bcrypt.hashpw(password, salt)               self._password = hashed_password
          def _get_password(self):               return self._password
          password = synonym('_password',                       descriptor=property(_get_password,                                           _set_password))           