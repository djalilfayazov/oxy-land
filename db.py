'''create table users(id int, firstname text, username text, balance int, rank text, added text)'''


from config import Settings
db = Settings().db


from sqlite3 import *
from datetime import datetime as dt


class DB:
    def check_user(self, id:int):
        conn = connect(db)
        c = Cursor(conn)

        re = c.execute(
            f'''
                select * from users where id={id}
            '''
        )
        
        if len((*re,)) != 0:
            return True
        else:
            return False

        conn.commit()
        conn.close()
            

    def add_user(self, user):
        with connect(db) as c:
            c.execute(
                '''insert into users values({0}, "{1}", "{2}", {3}, "{4}", "{5}")'''.format(
                    user.id, user.first_name, user.username,
                    500, 'grey', dt.now()
                )
            )


    def get_data(self, id:int, field:str):
        with connect(db) as c:
            re = c.execute(
                '''select {0} from users where id={1}'''.format(
                    field, id
                )
            )

            return str(
                tuple(*re)[0]
            )


    def set_data(self, id:int, field:str, data):
        with connect(db) as c:
            if type(data) == int:
                c.execute(
                    '''update users set {0}={1} where id = {2}'''.format(
                        field, data, id
                    )
                )
            if type(data) == str:
                c.execute(
                    '''update users set {0}="{1}" where id = {2}'''.format(
                        field, data, id
                    )
                )
