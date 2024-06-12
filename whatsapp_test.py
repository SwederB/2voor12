import pywhatkit
import datetime

phonenumber_sweder = "+31649852889" # Sweder
print(phonenumber_sweder)
phonenumber_schelto = "+31653163887" # Schelto

now = datetime.datetime.now()

# message = "Hello, this is a test message"
message = "Ik kom nu naar idkafee"

time_hour = now.hour
time_min = now.minute + 1
wait_time = 10
tab_close = True
close_time = 11


pywhatkit.sendwhatmsg(phonenumber_schelto, message, time_hour, time_min, wait_time, tab_close, close_time)