#mail parser
from imapclient import IMAPClient
import email
from contextlib import contextmanager
from datetime import date
import os
from datetime import timezone,timedelta

class Mail:
    IMAP_SERVER = "outlook.office365.com"
    IMAP_PORT = 993
    IMAP_TLS = True

    def __init__(self) -> None:
        pass

    @contextmanager
    def session(self):
        try:
            server = IMAPClient(self.IMAP_SERVER,use_uid=True)
            response = server.login(os.getenv("MAIL_USER"), os.getenv("MAIL_SECRET"))
            if response:
                print(f"--Session started:{response.decode('utf-8')}\n")
                yield server
        except Exception as e:
            print(f"Error while connecting to IMAP server: {e}")
        finally:
            response = server.logout()
            print(f"\n--Session ended:{response.decode('utf-8')}")

    def parser(self,since_date):
        with self.session() as s:
            inbox = s.select_folder("INBOX", readonly = True)

            #filters
            messages = s.search(["SINCE",since_date])
            # messages = s.search(["SUBJECT","Hoe"])

            response = s.fetch(messages, ['ENVELOPE','BODY','RFC822'])

            for msgid,data in response.items():
                envelope = data[b'ENVELOPE']
                mail_subject = envelope.subject.decode()
                mail_date = envelope.date

                #get attachments
                # mail_object = email.message_from_bytes(data[b'RFC822'])
                # print(mail_object.get_payload(1))
      
    


