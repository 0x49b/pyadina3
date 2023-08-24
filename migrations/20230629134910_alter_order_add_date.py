"""
This module contains a Caribou migration.

Migration Name: alter_order_add_date 
Migration Version: 20230629134910
"""

def upgrade(connection):
    sql = """
        ALTER TABLE orders ADD COLUMN date TEXT
    """
    try:
        connection.execute(sql)
        connection.commit()
    except:
        print("date already in table orders")
    pass


def downgrade(connection):
    sql = """
    ALTER TABLE orders DROP COLUMN date
    """
    connection.execute(sql)
    connection.commit()
    pass
