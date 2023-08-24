"""
This module contains a Caribou migration.

Migration Name: alter_orders 
Migration Version: 20230629134014
"""


def upgrade(connection):
    sql = """
        ALTER TABLE orders ADD COLUMN timestamp TEXT
    """
    try:
        connection.execute(sql)
        connection.commit()
    except:
        print("timestamop already in table orders")
    pass


def downgrade(connection):
    sql = """
    ALTER TABLE orders DROP COLUMN timestamp
    """
    connection.execute(sql)
    connection.commit()
    pass
