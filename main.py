#main application 
from database import insert
from database.connection import get_conn
from mail import parser


def main():
    
    with get_conn() as conn:
        pass


if __name__ == '__main__':
    main()
