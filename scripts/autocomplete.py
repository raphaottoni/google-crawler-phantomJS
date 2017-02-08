#!/usr/bin/env python

import csv
import urllib2

#Variables

#google autocomplete api
google_auto_complete_api = "http://suggestqueries.google.com/complete/search?output=firefox&client=firefox&hl=en-US&q="

# Read all unique names from csv
with open('../data/names.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        name = row[0]

        # question = Why is ...
        output  =  open("../results/"+row[0]+"_why_is_name.json","w")
        response = urllib2.urlopen(google_auto_complete_api + "why%20is%20" + row[0] + "%20")
        html = response.read()
        output.write(html)
        response.close()

        # question = is ...
        output  =  open("../results/"+row[0]+"_name_is.json","w")
        response = urllib2.urlopen(google_auto_complete_api + row[0] + "%20is%20")
        html = response.read()
        output.write(html)
        response.close()



