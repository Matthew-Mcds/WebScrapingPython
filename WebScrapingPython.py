from bs4 import BeautifulSoup
import requests
import csv

# * This is an example of python program that collects data from a website. In this example medical infomation is
# *  collected from a medical website and put in a excel CVS file.


# * Creates to parse through pages on a website
page = 0
counter = 97

# * This loops through all the pages on the website
for page in range(97, 123):
    page = chr(counter)
    link = "https://www.drugs.com/alpha/" + str(page) + ".html"

    # * This stores the link in a variable that BeautifulSoup can access
    source = requests.get(link).text

    # * This scrapes the websites html through a  parser
    scrape = BeautifulSoup(source, 'html.parser')

    # * This creates an excel file to write data onto.
    csv_file = open('cms_scrape2.csv', 'a', newline='')

    # * This creates the heading on the file for codes and diseases.
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Drug', 'Description'])

    # * This gets the ul that contains all the drugs
    webScrape = scrape.find('ul', class_='ddc-list-column-2')

    # * This loops through the li's that contain all the different individual drugs
    for drugs in webScrape.find_all('li'):
        print(drugs.text)
        csv_writer.writerow([drugs.text])

    # * This is a counter for the ascii value to change the webpage.
    counter = counter + 1

csv_file.close()
