from datetime import datetime   
from playsound import playsound
time = input("Enter the time of alarm to be set at format:HH:MM:SS:AM/PM\n")
hour=time[0:2]
minute=time[3:5]
seconds=time[6:8]
period =time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    org_hour = now.strftime("%I")
    org_minute = now.strftime("%M")
    org_seconds = now.strftime("%S")
    org_period = now.strftime("%p")
    if(period==org_period and hour==org_hour and minute==org_minute and seconds==org_seconds):
        print("Wake Up!")
        playsound('D:\Music\Your_name_OST_RADWIMPS_-_Sparkle_(mp3.pm).mp3')
        break
