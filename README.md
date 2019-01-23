# Trustpilot-Location-Reviews
How to use the Trustpilot API and tags to calculate specific Trustscores for certain tagged reviews. 

# How to Use 
* Use the Trustpilot API to tag reviews with location specific titles as they come in using the "tag" field (https://developers.trustpilot.com/invitation-api)
* You will now have reviews in your platform that are "tagged" with a location tag
* Time to update the python script: 
  * add your Trustpilot Business Unit ID on line 8. This shoul be a string of characters and numbers that you can retreive from your Trustpilot Customer Sucess Team or by calling the API (https://developers.trustpilot.com/business-units-api#find-a-business-unit)
  * update line 11 with your location tag value 
  * update line 23 with your account's API Key. This can be found within your Trustpilot business acount (https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs) 
* Run the script!

# Technologies Used 
`Python`
`Trustpilot API`


