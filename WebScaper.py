from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

myurl = 'https://www.amctheatres.com/movies'

Client = urlopen(myurl)

htmlpage = Client.read()

Client.close()

filename = "Moviesdb.csv"
file = open(filename,"w")
file.write("Movie, Date, Length \n")
page_soup = soup(htmlpage, "html.parser")

Containers = page_soup.main.findAll("div",{"class":"Slide"})

for container in Containers:
    movies = container.h3.text
    datearray = container.findAll("span",{"class":"MoviePosters__released-month clearfix"})
    if datearray != []:
        date = datearray[0].text
    else:
        date = ""
    timelengthobj = container.findAll("span",{"class":"u-separator js-runtimeConvert u-inlineFlexCenter"})
    if timelengthobj != []:
        timelength = timelengthobj[0].text
    else:
        timelength = ""
    print("Movies:" + movies)
    print(date)
    print("Timelength:" + timelength)
    print("\n")
    file.write(movies.replace(","," ") + "," + date.replace(","," ") + "," + timelength + "\n")
file.close()