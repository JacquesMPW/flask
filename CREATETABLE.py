import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("""
        CREATE TABLE Employee
        (
        EMPID INTEGER NOT NULL PRIMARY KEY,
        EmpName VARCHAT(20) NOT NULL,
        HireDate DATE,
        Salary CURRENCY
        )
""")
