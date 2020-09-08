import schedule
import time
import sys
import ramlanWaktus as rw

schedule.every().day.at("00:00:10").do(rw.ramBook)
schedule.every().day.at("00:13").do(sys.exit)

#tester
#schedule.every().day.at("14:27:04").do(rw.ramBook)

schedule.every().day.at("00:13").do(sys.exit)


while True:
    schedule.run_pending()
    time.sleep(1)