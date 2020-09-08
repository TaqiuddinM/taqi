import schedule
import time
import hajiWaktus as hw


schedule.every().monday.at("00:00:02").do(hw.mondayToSundayExceptFriday)
schedule.every().tuesday.at("00:00:02").do(hw.mondayToSundayExceptFriday)
schedule.every().wednesday.at("00:00:02").do(hw.mondayToSundayExceptFriday)
schedule.every().thursday.at("00:00:02").do(hw.friday)
schedule.every().friday.at("00:00:02").do(hw.mondayToSundayExceptFriday)
schedule.every().saturday.at("00:00:02").do(hw.mondayToSundayExceptFriday)
schedule.every().sunday.at("00:00:02").do(hw.mondayToSundayExceptFriday)

#tester
#schedule.every().day.at("14:27:02").do(hw.mondayToSundayExceptFriday)

schedule.every().day.at("00:13").do(hw.stopRec)



while True:
    schedule.run_pending()
    time.sleep(1)
