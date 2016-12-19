from bs4 import BeautifulSoup
fo1=open("index.html","r+")
data=fo1.read()
soup = BeautifulSoup(data)
list=[]
li1=[]
count=0
inner_ul = soup.find('ul')
fo = open("result.json", "wb")
for li in inner_ul.find_all('li'):
    list.append(li.text.strip())
fo.write ("{" '"capitals"'": [");
for li in list:
    listadd=li.split("\n")
    if list[-1]:
        fo.write("{" '"capital"' ":" +listadd[0]+ "," '"state"' ":" +listadd[1]+"}")
    else:
        fo.write("{" '"capital"' ":" +listadd[0]+ "," '"state"' ":" +listadd[1]+"},")
    count+=1
count=str(count)
fo.write("],"'"summary"'": {" '"number of capitals"' ":"+count+"}}")
fo.close()
