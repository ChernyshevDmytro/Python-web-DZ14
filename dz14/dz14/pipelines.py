# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Person, Keywords, Quotes




class Dz14Pipeline(object):

    def process_item(self, item, authors):        
        engine = create_engine('sqlite:///dz14.db') 
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        
        
        #print(f"sssssssssssssssssssssss{item}")
        try:
            

            if item['author']:
                print(f"fffffffffff{item['author']}")
                name  = item['author']
                name=name[0]
                #name.replace("[", "")
                #name.replace("]", "")
                #name.replace("'", "")
                print(f"fffffffffff {name}")     
                person=Person(author_name = f"{name}")
                session.add(person)
                session.commit()
                session.close()                    
            if item['quote'] and not person.quotes:
                print(f"qqqqqq{item['quote']}")
                print(type(f"qqqq{item['quote']}"))
                person.quotes = Quotes(quote= str(item['quote'])) 
            if item['keywords'] and person.keywords:
                for i in item['keywords']:
                    person.keywords.append(Keywords(keyword=f"{i}"))
            if item['keywords'] and not person.keywords:
                for i in item['keywords']:
                    person.keywords = Keywords(keyword=f"{i}") 

                            
            
            #session.add(person)
            #session.commit()

        finally:
           print("aaa")
           #session.close()
        
        return item
#a= Dz14Pipeline()