import requests
import time
import re
import datetime

def http_request(url, currency):
    """Returns the data inside request with the choice of currency."""
    request = requests.get(url)
    data = request.json()
    return data[currency]

def time_parser(time_period):
    """Parsing the time period you want the program to run, convert to seconds to be comparable across the program."""
    time_lst = [int(x) for x in re.findall("\d+", time_period)]
    if len(time_lst) != 4: # Check if it works
        error_message = "Time input not compatible, run program again!"
        return error_message
    else:
        day_to_sec = ((time_lst[0] * 24) * 60) * 60
        hour_to_sec = (time_lst[1] * 60) * 60
        minute_to_sec = time_lst[2] * 60
        total_sec = day_to_sec + hour_to_sec + minute_to_sec + time_lst[3]
        return total_sec

def info_parser(url, currency, period, interval):
    """Equivalent of main function."""
    period_sec = time_parser(period)
    
    if isinstance(period_sec, int) == False:
        return print(period_sec)
    
    iterations = period_sec // interval

    for _ in range(iterations):
        data = http_request(url, currency)
        bitcoin_value_buy = data["buy"]
        bitcoin_value_sell = data["sell"]
        current_time = datetime.datetime.now()
        print(f"\nCurrent value to buy Bitcoin is: {bitcoin_value_buy} in {currency}\n\
Current value to sell Bitcoin is: {bitcoin_value_sell} in {currency}\n\
at {current_time.month}/{current_time.day}/{current_time.year}\
 {current_time.hour}:{current_time.minute}:{current_time.second}")
        time.sleep(interval)
    
    print("\nProgram finished soundly.")




if __name__ == "__main__":
    # "https://blockchain.info/ticker"
    print("Welcome to the bitcoin live value program!")
    url = "https://blockchain.info/ticker"
    period_of_time = input("\nInsert the amount of time you want to monitor the value in the format \
\n(days:hours:minutes:seconds, example of 15 seconds: 0:0:0:15): ")
    interval = int(input("\nSet the time interval in seconds you want to update the value: "))
    currency = input("\nInsert the curency you want your value to be: ").upper()
    info_parser(url, currency, period_of_time, interval)