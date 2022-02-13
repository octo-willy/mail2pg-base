#main application 
from database import func
from database.connection import get_conn
from mail.parser import Mail
from datetime import date

def main():
    
    #fetch data
    mail = Mail()
    mail_data = mail.parser(since_date=date(2022,2,12))

    #insert data
    with get_conn() as conn:
        ids = func.add_data(conn,mail_data)


if __name__ == '__main__':
    main()
