import schedule
import time
import days2 as d
import stopRunning2 as stp


schedule.every().friday.at("00:00").do(d.mondayToWednesdayAndWeekendPrayer)
schedule.every().sunday.at("00:00").do(d.mondayToWednesdayAndWeekendPrayer)
schedule.every().monday.at("00:00").do(d.mondayToWednesdayAndWeekendPrayer)
schedule.every().tuesday.at("00:00").do(d.mondayToWednesdayAndWeekendPrayer)
schedule.every().saturday.at("00:00").do(d.mondayToWednesdayAndWeekendPrayer)
schedule.every().wednesday.at("00:00").do(d.thursdayPrayer)
schedule.every().thursday.at("00:00").do(d.fridayPrayer)

schedule.every().day.at("00:21").do(stp.stopRec)

while True:
    schedule.run_pending()
    time.sleep(1)

