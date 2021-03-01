class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


class Mailbox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, email_index):
        for index in email_index:
            self.emails[index].send()

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())


mailbox = Mailbox()

while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, content = command.split(" ")

    email = Email(sender, receiver, content)
    mailbox.add_email(email)


emails_to_send = list(map(int, input().split(", ")))

mailbox.send_emails(emails_to_send)

mailbox.print_mailbox()