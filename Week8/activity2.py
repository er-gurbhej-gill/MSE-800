class email:
    def send(self):
        print("sending_email")

class sms:
    def send(self):
        print("sending_sms")

class push:
    def send(self):
        print("sending_push_notification")

class email_factory:
    def create_notification(self):
        return email()

class sms_factory:
    def create_notification(self):
        return sms()
    
class push_factory:
    def create_notification(self):
        return push()

email_factory_obj = email_factory()
email_notification = email_factory_obj.create_notification()
email_notification.send()

sms_factory_obj = sms_factory()
sms_notification = sms_factory_obj.create_notification()
sms_notification.send()

push_factory_obj = push_factory()
push_notification = push_factory_obj.create_notification()
push_notification.send()