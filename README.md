# GOOGLE FLIGHTS SCRAPER 

This simple python script scrape price and information about the first flight sorted on GoogleFlights and mails the information about the cheapest flights to the user

Given a list of airport codes as departure flights option, a list of ariport codes as possible destinations and the search date range, the program will scrape all combination one by one, storing data of first A/R flight shown by GoogleFlights for each search.

The search parameters are in the settings.json file.

## Example of settings.json

{
    "from": [
        "NAP"
    ],
    "to": [
        "CCU"
    ],
    "outbound": "2023-12-26",
    "delta": 2,
    "flexdays": 1,
    "weekend": false,
    "lastdate": "2024-01-15",
    "fastmode": true,
    "timeout": 10
}
