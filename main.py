import datetime
import time

def set_alarm():
    alarm_time = input("Enter the alarm time (format HH:MM): ")
    while True:
        try:
            hour, minute = map(int, alarm_time.split(':'))
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                break
            else:
                print("Invalid time. Please try again.")
        except ValueError:
            print("Incorrect time format. Please try again.")
        alarm_time = input("Enter the alarm time (format HH:MM): ")

    return datetime.time(hour, minute)

def wait_for_alarm(alarm):
    while True:
        now = datetime.datetime.now().time()
        if now >= alarm:
            print("Alarm!")
            break
        time.sleep(1)

alarm_time = set_alarm()
print("The alarm is set for:", alarm_time)
wait_for_alarm(alarm_time)
