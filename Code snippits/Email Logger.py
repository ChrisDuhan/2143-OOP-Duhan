class Email(object):
  def __init__(self, msg, subj, sndr, rcivr):
    self.message = msg
    self.subject = subj
    self.sender = sndr
    self.receiver = rcivr
  
  def __str__(self):
    return self
    
class logger(object):
  def __init__(self):
    self.me = "chris.m.duhan@gmail.com"
    self.all_emails = []
    self.emails_sent = []
    self.emails_received = []

  def add(self, email):
    self.all_emails.append(email)
    if email.sender is self.me:
      self.emails_sent.append(email)
    if email.receiver is self.me:
      self.emails_received.append(email)
  
  def get_sent_by(self, name):
    sent = []
    for i in self.all_emails:
      if i.sender is name:
        sent.append(i)
    return sent
  
  def get_received_by(self, name):
    received = []
    for i in self.all_emails:
      if i.receiver is name:
        received.append(i)
    return received
    


Logger = logger()

Email1 = Email("fake message 1","fake subject 1","joe@yahoo.com","sue@gmail.com")
Logger.add(Email1)

Email2 = Email("fake message 2","fake subject 2","bill@yahoo.com","sue@gmail.com")
Logger.add(Email2)

Email3 = Email("fake message 3","fake subject 3","bill@yahoo.com","joe@yahoo.com")
Logger.add(Email3)

Email4 = Email("fake message 4","fake subject 4","jon@hotmail.com","sue@gmail.com")
Logger.add(Email4)


list1 = Logger.get_sent_by("bill@yahoo.com")
print(list1)
list2 = Logger.get_received_by("sue@gmail.com")
print(list2)
