import schedule
import time
import taqiWaktus as tw
import sys


schedule.every().monday.at("00:00:00").do(tw.mondayToSaturdayExceptFriday)
schedule.every().tuesday.at("00:00:00").do(tw.mondayToSaturdayExceptFriday)
schedule.every().wednesday.at("00:00:00").do(tw.mondayToSaturdayExceptFriday)
schedule.every().thursday.at("00:00:00").do(tw.friday)
schedule.every().friday.at("00:00:00").do(tw.mondayToSaturdayExceptFriday)
schedule.every().sunday.at("00:00:00").do(tw.mondayToSaturdayExceptFriday)

#tester
#schedule.every().day.at("14:27:00").do(tw.mondayToSaturdayExceptFriday)
#schedule.every().day.at("14:37").do(sys.exit)


schedule.every().day.at("00:13").do(sys.exit)

while True:
    schedule.run_pending()
    time.sleep(1)
