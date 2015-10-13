'''
this model contain the methods you can use the options:
add information in database
get information in database
'''

from sqlalchemy.orm.session import sessionmaker
from data_settings import ChinaNewsContent,ChinaNewsTitle,CommunityContent,CommunityTitle,\
                    InterNewsContent,InterNewsTitle,JokeContent,engine,MalitaryTitle,MalitaryContent,\
                    SportsTitle,SportsContent,EntertainmentTitle,EntertainmentContent
'''
insert the information into database
'''
def Session_Adapter_Add(data_information):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(data_information)
    session.flush()
    session.commit()
'''
return a session
'''    
def Get_Session():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session

class DataOptionSave():
    '''
    use this method to save the joke content in database
    '''
    def Joke_Save(self,contents):
        jokeContent = JokeContent()
        jokeContent.content = contents
        Session_Adapter_Add(jokeContent)
        
    def Chnews_Title_Save(self,s,t):
        li = eval(s)
        lis = eval(t)
        for i in range(len(li)):
            chNewsTitle = ChinaNewsTitle()
            chNewsTitle.link = "http://news.qq.com"+li[len(li)-1-i]
            chNewsTitle.title = lis[len(li)-1-i]
            chNewsTitle.lock = 0
            Session_Adapter_Add(chNewsTitle)
            
    def Sport_Title_Save(self,s,t):
        for i in range(len(s)):
            SportTitle = SportsTitle()
            SportTitle.link = "http://www.chinanews.com"+s[len(s)-1-i]
            SportTitle.title = t[len(s)-1-i]
            SportTitle.lock = 0
            Session_Adapter_Add(SportTitle)
        
    def Chnews_Content_Save(self,title,content):
        chNewsContent = ChinaNewsContent()
        chNewsContent.title = title
        chNewsContent.content = content
        Session_Adapter_Add(chNewsContent)
        
    def Sport_Content_Save(self,title,content):
        sportContent = SportsContent()
        sportContent.title = title
        sportContent.content = content
        Session_Adapter_Add(sportContent)
        
    def Inter_Title_Save(self,s,t):
        li = eval(s)
        lis = eval(t)
        for i in range(len(li)):
            interNewsTitle = InterNewsTitle()
            interNewsTitle.link = "http://news.qq.com"+li[len(li)-1-i]
            interNewsTitle.title = lis[len(li)-1-i]
            interNewsTitle.lock = 0
            Session_Adapter_Add(interNewsTitle)
        
    def Inter_Content_Save(self,title,content):
        interContent = InterNewsContent()
        interContent.title = title
        interContent.content = content
        Session_Adapter_Add(interContent)
        
    def Comu_Title_Save(self,s,t):
        for i in range(len(s)):
            comuNewsTitle = CommunityTitle()
            comuNewsTitle.link = s[len(s)-1-i]
            comuNewsTitle.title = t[len(s)-1-i]
            comuNewsTitle.lock = 0
            Session_Adapter_Add(comuNewsTitle)
            
    def Entertainment_Title_Save(self,s,t):
        for i in range(len(s)):
            comuNewsTitle = EntertainmentTitle()
            comuNewsTitle.link = s[len(s)-1-i]
            comuNewsTitle.title = t[len(s)-1-i]
            comuNewsTitle.lock = 0
            Session_Adapter_Add(comuNewsTitle)
        
    def Comu_Content_Save(self,title,content):
        comuContent = CommunityContent()
        comuContent.title = title
        comuContent.content = content
        Session_Adapter_Add(comuContent)
        
    def Entertainment_Content_Save(self,title,content):
        comuContent = EntertainmentContent()
        comuContent.title = title
        comuContent.content = content
        Session_Adapter_Add(comuContent)
        
    def Mali_Title_Save(self,s,t):
        for i in range(len(s)):
            malitaryTitle = MalitaryTitle()
            if "http://www.chinanews.com" in s[len(s)-1-i]:
                malitaryTitle.link = s[len(s)-1-i]
            else:
                malitaryTitle.link = "http://www.chinanews.com"+s[len(s)-1-i]
            malitaryTitle.title = t[len(s)-1-i]
            malitaryTitle.lock = 0
            Session_Adapter_Add(malitaryTitle)
            
    def Mali_Content_Save(self,title,content):
        maliContent = MalitaryContent()
        maliContent.title = title
        maliContent.content = content
        Session_Adapter_Add(maliContent)
        
class DataOptionGet():
    '''
    get the number message
    '''
    def get_title_num(self,table_name):
        session = Get_Session()
        num = 0
        if table_name == 'joke':
            missing = session.query(JokeContent).all()
            num = 10*len(missing)
        elif table_name == 'china':
            missing = session.query(ChinaNewsTitle).all()
            num = len(missing)
        elif table_name == 'internation':
            missing = session.query(InterNewsTitle).all()
            num = len(missing)
        elif table_name == 'sports':
            missing = session.query(SportsTitle).all()
            num = len(missing)
        elif table_name == 'malitary':
            missing = session.query(MalitaryTitle).all()
            num = len(missing)
        elif table_name == 'community':
            missing = session.query(CommunityTitle).all()
            num = len(missing)
        elif table_name == 'entertainment':
            missing = session.query(EntertainmentTitle).all()
            num = len(missing)
        return num
    '''
    get the message in the table
    '''
    def get_table_message(self,table_name):
        session = Get_Session()
        if table_name == 'joke':
            missing = session.query(JokeContent).all()
        elif table_name == 'china':
            missing = session.query(ChinaNewsTitle).all()
        elif table_name == 'internation':
            missing = session.query(InterNewsTitle).all()
        elif table_name == 'sport':
            missing = session.query(SportsTitle).all()
        elif table_name == 'malitary':
            missing = session.query(MalitaryTitle).all()
        elif table_name == 'community':
            missing = session.query(CommunityTitle).all()
        elif table_name == 'entertainment':
            missing = session.query(EntertainmentTitle).all()
        return missing
    '''
    get unlock links and last link from ChinaNewsTitle
    lock the link used in ChinaNewsTitle
    '''
    def get_Unlock_Links_CH(self):
        session = Get_Session()
        missing = session.query(ChinaNewsTitle).filter(ChinaNewsTitle.lock=="0").all()
        return missing
    def get_Last_Link_CH(self):
        session = Get_Session()
        try:
            missing = session.query(ChinaNewsTitle).order_by(ChinaNewsTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_CH(self):
        session = Get_Session()
        session.query(ChinaNewsTitle).filter(ChinaNewsTitle.lock=='0').update({ChinaNewsTitle.lock:'1'})
        session.flush()
        session.commit()
    '''
    get unlock links and last link from InterNewsTitle
    lock the link used in InterNewsTitle
    '''    
    def get_Unlock_Links_IN(self):
        session = Get_Session()
        missing = session.query(InterNewsTitle).filter(InterNewsTitle.lock=="0").all()
        return missing
    def get_Last_Link_IN(self):
        session = Get_Session()
        try:
            missing = session.query(InterNewsTitle).order_by(InterNewsTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_IN(self):
        session = Get_Session()
        session.query(InterNewsTitle).filter(InterNewsTitle.lock=='0').update({InterNewsTitle.lock:'1'})
        session.flush()
        session.commit()
    '''
    get unlock links and last link from CommunityTitle
    lock the link used in CommunityTitle
    '''
    def get_Unlock_Links_CO(self):
        session = Get_Session()
        missing = session.query(CommunityTitle).filter(CommunityTitle.lock=="0").all()
        return missing
    def get_Last_Link_CO(self):
        session = Get_Session()
        try:
            missing = session.query(CommunityTitle).order_by(CommunityTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_CO(self):
        session = Get_Session()
        session.query(CommunityTitle).filter(CommunityTitle.lock=='0').update({CommunityTitle.lock:'1'})
        session.flush()
        session.commit()
    '''
    get unlock links and last link from MalitaryTitle
    lock the link used in MalitaryTitle
    '''
    def get_Unlock_Links_MA(self):
        session = Get_Session()
        missing = session.query(MalitaryTitle).filter(MalitaryTitle.lock=="0").all()
        return missing
    def get_Last_Link_MA(self):
        session = Get_Session()
        try:
            missing = session.query(MalitaryTitle).order_by(MalitaryTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_MA(self):
        session = Get_Session()
        session.query(MalitaryTitle).filter(MalitaryTitle.lock=='0').update({MalitaryTitle.lock:'1'})
        session.flush()
        session.commit()
    '''
    get unlock links and last link from SportsTitle
    lock the link used in SportsTitle
    '''
    def get_Unlock_Links_Sport(self):
        session = Get_Session()
        missing = session.query(SportsTitle).filter(SportsTitle.lock=="0").all()
        return missing
    def get_Last_Link_Sport(self):
        session = Get_Session()
        try:
            missing = session.query(SportsTitle).order_by(SportsTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_Sport(self):
        session = Get_Session()
        session.query(SportsTitle).filter(SportsTitle.lock=='0').update({SportsTitle.lock:'1'})
        session.flush()
        session.commit()
        
    '''
    get unlock links and last link from EntertainmentTitle
    lock the link used in SportsTitle
    '''
    def get_Unlock_Links_ET(self):
        session = Get_Session()
        missing = session.query(EntertainmentTitle).filter(EntertainmentTitle.lock=="0").all()
        return missing
    def get_Last_Link_ET(self):
        session = Get_Session()
        try:
            missing = session.query(EntertainmentTitle).order_by(EntertainmentTitle.id.desc()).first()
            return missing.link
        except:
            return ''
    def lock_Links_ET(self):
        session = Get_Session()
        session.query(SportsTitle).filter(EntertainmentTitle.lock=='0').update({EntertainmentTitle.lock:'1'})
        session.flush()
        session.commit()        
        
        
        
