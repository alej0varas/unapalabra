from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from sql_create import Base, Lema


engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


with open('rae_crawl.txt', 'r') as input:
    document = []
    for line in input.readlines():
        if '</html>' not in line:
            document.append(line)
            continue
        soup = BeautifulSoup(''.join(document), 'html.parser')
        if soup.article is not None:
            try:
                session.query(Lema).filter(Lema.rae_id == soup.article.attrs['id']).one()
            except NoResultFound:
                lema = Lema(rae_id=soup.article.attrs['id'], text=soup.article.text)
                session.add(lema)
                session.commit()
        document = []
