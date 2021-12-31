# Imports
import wikipediaapi
import requests
import pyperclip
import os
import sys
from dotenv import load_dotenv

# Load environment variables using load_env
load_dotenv()
SMMRYAPIKEY = os.getenv(SMMRY_API_KEY)
RAPIDAPIKEY = os.getenv(RAPIDAPI_KEY)


# set URL as rapidAPI link
# initialising wiki object and setting language as english
URL = "https://community-smmry.p.rapidapi.com/"
wiki = wikipediaapi.Wikipedia('en')

# check the length of Command line arguments
# if no additional arguments are present, then the clipboard content
# is used as URL and passed to the API request.
# Otherwise, get url for Wiki page by passing the command line arguments

if len(sys.argv) < 2:
    smmryText = pyperclip.paste()
else:
    wikiPage = wiki.page(' '.join(sys.argv[1:]))
    if wikiPage.exists():
        smmryText = wikiPage.fullurl
    else:
        print("Wikipedia page does not exist.")
        sys.exit()

# querystring with the SMMRY API key and the URL to be summarized.
# headers with rapidAPI key and url

querystring = {"SM_API_KEY": SMMRYAPIKEY,
               "SM_URL": smmryText
               }

headers = {
    'x-rapidapi-host': "community-smmry.p.rapidapi.com",
    'x-rapidapi-key': RAPIDAPIKEY
}

# Making a GET request to the API by passing URL, headers and the parameters

response = requests.request("GET", URL, headers=headers, params=querystring)

# storing the response received into a dictionary

responseDict = response.json()

# Printing the summary by accessing the value for "sm_api_content" key

print(responseDict["sm_api_content"])
