# sm-liquidator-3000
Safemoon Liquidator Bot
This isn't robinhood, people deserve to be able to sell.

## Notes
This is a command line bot that submits market sell orders for 10million safemoon to Bitmart every minute. 

It does nothing else.

You'll need an API key from Bitmart, instructions here https://developer-pro.bitmart.com/en/part1/question/apikey.html

You will need your api_key, secret_key, and memo.

## How to Install
```
- Install python3
- Go to command line, install dotenv with `pip3 install dotenv` for linux and mac users,`python -m pip install dotenv` for windows users
- Create a file called `.env` in the same directory as `main.py`
```

## .env File
The .env file fills in information to let Bitmart use your account when making the sell orders. It has the following format:
```
API_PUBLIC_KEY="ENTER YOUR API KEY HERE"
API_SECRET_KEY="ENTER YOUR SECRET KEY HERE"
API_MEMO="ENTER YOUR MEMO HERE"
```
Keep the quotes.

## To run
```
python3 main.py
```

## To stop
```
ctrl-c
```
