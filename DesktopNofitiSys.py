#Source Code for Desktop Notification System:
from plyer import notification 
import time

#Setting up Notification:
notification_title = "Notification Title"
notification_message = "Drink Water"

notification_timeout = 5 #in seconds
#Display Notification:
for i in range(5):
    notification.notify(
        title = notification_title,
        message = notification_message,
        timeout = notification_timeout
        )
#Selected 