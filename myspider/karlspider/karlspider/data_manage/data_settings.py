from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT

'''the connection to the database'''
'''
for example:
engine = create_engine("mysql://karlname:karlpassword@localhost/spider?charset=utf8",isolation_level="READ UNCOMMITTED")
'''
engine = create_engine("mysql://"此处数据库用户名":"此处密码"@"数据库服务地址"/"数据库名"?charset=utf8",isolation_level="READ UNCOMMITTED") 
'''the construct of the database table'''
Base = declarative_base()

class NewsTitle():
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    link = Column(String(500))
    lock = Column(String(1))
    
class NewsContent():
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    content = Column(LONGTEXT)
    
class Joke():
    id = Column(Integer, primary_key=True)
    content = Column(LONGTEXT)
    
class User():
    id = Column(Integer,primary_key=True)
    username = Column(String(500))
    password = Column(String(500))
    malitary = Column(String(500))
    chinanews = Column(String(500))
    internews = Column(String(500))
    community = Column(String(500))
    
class ChinaNewsTitle(Base,NewsTitle):
    __tablename__ = 'chinanewstitle'
    
class ChinaNewsContent(Base,NewsContent):
    __tablename__ = 'chinanewscontent'
    
class InterNewsTitle(Base,NewsTitle):
    __tablename__ = 'internewstitle'
    
class InterNewsContent(Base,NewsContent):
    __tablename__ = 'internewscontent'

class CommunityTitle(Base,NewsTitle):
    __tablename__ = 'communitytitle'
    
class CommunityContent(Base,NewsContent):
    __tablename__ = 'communitycontent'
    
class MalitaryTitle(Base,NewsTitle):
    __tablename__ = 'malitarytitle'
    
class MalitaryContent(Base,NewsContent):
    __tablename__ = 'malitarycontent'
    
class JokeContent(Base,Joke):
    __tablename__ = 'jokecontent'
    
class SportsTitle(Base,NewsTitle):
    __tablename__ = 'sportstitle'
    
class SportsContent(Base,NewsContent):
    __tablename__ = 'sportscontent'
    
class EntertainmentTitle(Base,NewsTitle):
    __tablename__ = 'entertainmenttitle'
    
class EntertainmentContent(Base,NewsContent):
    __tablename__ = 'entertainmentcontent'
    
Base.metadata.create_all(engine)
