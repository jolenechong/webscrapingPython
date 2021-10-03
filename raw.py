from bs4 import BeautifulSoup
import requests

'''
web scraping for local html files
- first ensure your html file is in the same folder as this .py file
'''

# open html file
with open("test.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# to view indented html code (to view code easier)
print("\nINDENTED CODE\n=======\n",doc.prettify())

# get title and print title
tag = doc.title
print("\nPRINT <TITLE> TAG FROM HTML FILE\n=======\n",tag.string)

tags = doc.find_all("p")
# find_all() takes everything and puts it in a list
print("\nPRINT <STRONG> TAG\n=======\n",tags[0].find_all("strong"))
# so lets take the first of the find_all and get the text in it using .string
print(tags[0].find_all("strong")[0].string)
