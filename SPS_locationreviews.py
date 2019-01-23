import requests
import getpass
import json
import csv
from requests.auth import HTTPBasicAuth

# enter in customer business unit id here
business_unit_id = '556727b40000ff00057fbace'

# update location tag here
tagValue = "nighttag"

fivestars = 0
fourstars = 0
threestars = 0
twostars = 0
onestar = 0
reviews = 0

page = 1

# API call - "Get a business unit's reviews" filtered by tag (aka location)
url = 'https://api.trustpilot.com/v1/business-units/' + business_unit_id + '/reviews?apikey=x4XHG3cSA2UWj1LBk4stD0ypMtgZ49oP&tagValue=' + tagValue + '&perPage=100&page=%s'
response = requests.get(url % page)
json_data = response.json()
allstars = [item['stars'] for item in json_data['reviews']]
print('All of your star ratings for location ' + tagValue + ' ' + str(allstars))
while json_data['reviews']!=[]:
    for item in json_data['reviews']: # loop through each review
        stars = item['stars']
        reviews += 1 # add to total number of reviews for this location
        if stars == 5:
            fivestars += 1 # add to number of 5 star reviews for this location
        elif stars == 4:
            fourstars += 1 # add to number of 4 star reviews for this location
        elif stars == 3:
            threestars += 1 # add to number of 3 star reviews for this location
        elif stars == 2:
            twostars += 1 # add to number of 2 star reviews for this location
        elif stars == 1:
            onestar += 1 # add to number of 1 star reviews for this location
    page += 1 # increase the page by one after looping through all 100 reviews on the page
    response = requests.get(url % page)
    json_data = response.json()
print(str(fivestars) + ' total 5 star reviews for location ' + tagValue) # this is the total number of reviews received for this location which will go in the schema markup
print(str(fourstars) + ' total 4 star reviews for location ' + tagValue)
print(str(threestars) + ' total 3 star reviews for location ' + tagValue)
print(str(twostars) + ' total 2 star reviews for location ' + tagValue)
print(str(onestar) + ' total 1 star reviews for location ' + tagValue)
print(str(reviews) + ' total reviews for location ' + tagValue)

# Trustscore formula 
trustScore = ((fivestars * 10) + (fourstars * 7.5) + (threestars * 5) + (twostars * 2.5) + (onestar * 0)) / (fivestars + fourstars + threestars + twostars + onestar)
roundedTrustScore = round(trustScore, 1)

# this is your aggregate rating value for the specific location which will go in the schema markup
print('Your Trustscore for location ' + tagValue + ' is ' + str(roundedTrustScore))