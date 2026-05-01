class Email:
    def send_message(self):
        print("Sending Email...")

class SMS:
    def send_message(self):
        print("Sending SMS...")

e = Email()
s = SMS()
notifications = [e,s]

for notification in notifications:
    notification.send_message()
