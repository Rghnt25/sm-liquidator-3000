# All people should be able to liquidate their holdings.
# This is DeFi, not RobinHood & Execs trading.
# Power to the people.

# Get your api key here: https://developer-pro.bitmart.com/en/part2/auth.html

from bitmart.api_spot import APISpot
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    api_key = os.getenv("API_PUBLIC_KEY")  # put your api key here
    secret_key = os.getenv("API_SECRET_KEY")  # put your secret key here
    memo = os.getenv("API_MEMO")

    spotAPI = APISpot(api_key, secret_key, memo, timeout=(3, 10))

    while True:
        print("Current Time: ", datetime.now())
        print("Attempting to sell 10mil Safemoon:")
        result = spotAPI.post_submit_market_sell_order("SAFEMOON_USDT", size='10000000')
        print(result)
        time.sleep(60)
