import requests as req
from bs4 import BeautifulSoup as bf
web = req.get('https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do')
soup = bf(web.content, 'html5lib')
# table = soup.select('.menu-tbl')
date = soup.select('.menu-tbl .date')
day = soup.select('.menu-tbl .day')
won = soup.select('h3.menu-tit01')
menu = soup.select('h3.menu-tit01+p')
def hk():
    for y,d,w,m in zip(date,day,won,menu):
        print('-'*18)
        print(y.text, "(", d.text, ")")
        print('-'*18)
        print(w.text)
        print('-'*18)
        print(m.text)
if __name__ == '__main__':
    hk()
    
