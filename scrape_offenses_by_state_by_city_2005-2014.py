#!/usr/bin/env python
# coding: utf-8

import requests

from bs4 import BeautifulSoup

import os

import csv

#import StringIO

import urlparse

current_dir = os.path.dirname(os.path.realpath(__file__))



state_names_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", \
"Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", \
"Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", \
"Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", \
"New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", \
"South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", \
"Washington", "West Virginia", "Wisconsin", "Wyoming"]


# For testing
#state_names_list = ["Alabama"]


# For states that were sometimes labeled differently / incorrectly
state_name_replacements = {
    "District Of Columbia": "District of Columbia",
    "Massachuetts": "Massachusetts"
}



offenses_links_by_year = {
    2005: "https://www2.fbi.gov/ucr/05cius/data/table_08.html",
    2006: "https://www2.fbi.gov/ucr/cius2006/data/table_08.html",
    2007: "https://www2.fbi.gov/ucr/cius2007/data/table_08.html",
    2008: "https://www2.fbi.gov/ucr/cius2008/data/table_08.html",
    2009: "https://www2.fbi.gov/ucr/cius2009/data/table_08.html",
    2010: "https://ucr.fbi.gov/crime-in-the-u.s/2010/crime-in-the-u.s.-2010/tables/10tbl08.xls/view",
    2011: "https://ucr.fbi.gov/crime-in-the-u.s/2011/crime-in-the-u.s.-2011/tables/table_8_offenses_known_to_law_enforcement_by_state_by_city_2011.xls/view",
    2012: "https://ucr.fbi.gov/crime-in-the-u.s/2012/crime-in-the-u.s.-2012/tables/8tabledatadecpdf/table_8_offenses_known_to_law_enforcement_by_state_by_city_2012.xls/view",
    2013: "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls/view",
    2014: "https://ucr.fbi.gov/crime-in-the-u.s/2014/crime-in-the-u.s.-2014/tables/table-8/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2014.xls/view"
}


for year in offenses_links_by_year:
    print year
    #print offenses_links_by_year[year]

    year_dir = current_dir+'/output/'+str(year)


    if not os.path.exists(year_dir):
        print 'creating directory:', year_dir
        os.mkdir(year_dir)  

    url = offenses_links_by_year[year]

    url_parts = url.split('/')
    url_parts.pop()
    url_for_relative_links = '/'.join(url_parts)+'/'

    print url_for_relative_links


    r = requests.get(url, allow_redirects=False)

    state_links_html = BeautifulSoup(r.content)

    for link in state_links_html.find_all('a'):
        #print dir(state_link)
        if link.text in state_names_list or link.text in state_name_replacements:

            state_text = link.text
            if link.text in state_name_replacements:
                state_text = state_name_replacements[link.text]

            state_csv_file_output = year_dir+'/'+state_text.replace(' ', '_')+'.csv'

            if not os.path.exists(state_csv_file_output):

                print link.text
                state_url = link.get('href')

                if state_url[:2] != 'ht':
                    state_url = url_for_relative_links+state_url

                r = requests.get(state_url, allow_redirects=False)

                state_data_html = BeautifulSoup(r.content)

                state_data = []
                #strIO = StringIO.StringIO()
                #writer = csv.writer(strIO)

                with open(state_csv_file_output, 'w') as csvfile:
                    csv_writer = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator='\r\n', \
                        quotechar = '"', quoting=csv.QUOTE_ALL)

                    for tr in state_data_html.find_all('tr'):
                        row = []

                        for th in tr.find_all('th'):
                            #print th
                            row.append(th.text.encode('utf-8').strip())

                        for td in tr.find_all('td'):
                            #print td
                            row.append(td.text.encode('utf-8').strip())

                        state_data.append(row)
                        #writer.writerow(row)
                        csv_writer.writerow(row)

                    #strIO.seek(0)

                    #state_csv = open(state_csv_file_output, 'w')

                    csvfile.close()

            #print state_data





