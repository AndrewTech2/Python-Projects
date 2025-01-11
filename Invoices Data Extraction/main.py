import sqlite3

conn = sqlite3.connect('data.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("""
SELECT CustomerId FROM invoices WHERE BillingCountry = 'Germany' AND Total > 2.0
 """)
values = cur.fetchall()
values = [dict(value) for value in values]
conn.close()
print(values)