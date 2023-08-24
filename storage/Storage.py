import sqlite3
import tempfile

import caribou
from datetime import date, datetime


class Storage(object):
    con = None
    cur = None

    db_path = "pyadina.db"  # todo create path to tmp folder
    migrations_path = '/home/pi/pyadina/migrations'  # todo check if works with py2app and pyinstaller

    def __init__(self):
        print('applying db migrations if any')
        caribou.upgrade(self.db_path, self.migrations_path)
        self.con = sqlite3.connect("pyadina.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.get_current_order()
        print(tempfile.gettempdir())

    def add_order(self, order):
        sql = 'insert into orders (day_order_num, p0, p1, p2, json, timestamp, date) values (:1, :2,:3,:4,:5,:6,:7)'
        self.cur.execute(sql, order)
        self.con.commit()

    def get_current_order(self):
        today = date.today()
        d = today.strftime("%d.%m.%Y")
        sql = "select day_order_num from orders where date = :1 order by id DESC LIMIT 1"
        res = self.cur.execute(sql, [d])
        val = res.fetchone()
        if val is None:
            return 0
        else:
            print(val)
            return val[0]
