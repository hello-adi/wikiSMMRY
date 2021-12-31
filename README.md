# wikiSMMRY
Python application that summarizes wikipedia articles using SMMRY API. 

## Introduction
This project utilises the wikipedia API and the SMMRY API to enable the user to summarize wiki pages through a command line interface

## Requirements
wikiSMMRY uses:
* Python version: 3.8.10
* Requests version: 2.22.0
* Pyperclip version: 1.8.2
* Wikipedia-API version: 0.5.4
* [SMMRY API](smmry.com/api)
* [RapidAPI](https://rapidapi.com/community/api/smmry-1/)

## How to run on local machine
In order to successfully run wikiSMMRY, you will need to sighn up for a [partner account](smmry.com/partner). This enables you to make 100 requests per day. A partner account comes with an API key that is needed to make API requests. I used RapidAPI to test the endpoints and that required a RapidAPI key. If you decide to use the environment you will need to register for RapidAPI as well. 
The application uses libraries not offered by the default python module and can be downloaded using [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt
```
Further, the SMMRY API key and the RapidAPI key can be loaded as environment variables or simply replaced in the program. However, it can be a security issue. 
### Environment Variables
```python
import os
from dotenv import load_dotenv
SMMRYAPIKEY = os.getenv(SMMRY_API_KEY)
RAPIDAPIKEY = os.getenv(RAPIDAPI_KEY)
```
Once the requirements are obtained, the application is ready to go.

## Using wikiSMMRY
wikiSMMRY is a CLI tool that can be utilised two ways.
1. The first method is passing the name of the wikipedia page you wish to summarize as a command line argument. The program checks if the name is indeed a valid wikipedia page and then obtains the URL and makes a request to the SMMRY API to summarize the page.
2. The second method revolves no command line arguments. Here, the link of the wikipedia page needs to be copied and stored in the clipboard. When the program is called without any arguments, it utilises the URL stored in the clipboard to make the API request. 

## Credits
A lot of this README was inspired from the one designed by dsynkov for their API wrapper https://github.com/dsynkov/smmryAPI.





