"""
This module contains a Caribou migration.

Migration Name: init 
Migration Version: 20230629115240
"""


def upgrade(connection):
    sql = """
        create table if not exists orders
        ( id            INTEGER primary key autoincrement ,
          day_order_num INTEGER ,
          p0            INTEGER ,
          p1            INTEGER , 
          p2            INTEGER ,
          json          TEXT 
        ) """
    connection.execute(sql)
    connection.commit()
    pass


def downgrade(connection):
    connection.execute("DROP TABLE orders")
    pass
