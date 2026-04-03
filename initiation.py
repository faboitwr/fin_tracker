import sqlite3

conn = sqlite3.connect("finrec_.db")
conn.execute("""
CREATE TABLE "Vendor" (
	"VendID"	INTEGER NOT NULL,
	"VendName"	TEXT NOT NULL,
	"Class"	TEXT NOT NULL CHECK("Class" = 'Food' OR "Class" = 'Apparel/Accessories' OR "Class" = 'Others'),
	PRIMARY KEY("VendID" AUTOINCREMENT)
);
             """)
conn.execute("""
CREATE TABLE "Spending" (
	"SpendID"	INTEGER NOT NULL,
	"MonthYR"	TEXT NOT NULL,
	"Cost"	REAL NOT NULL,
	"VendID"	INTEGER NOT NULL,
	"Comments"	TEXT,
	PRIMARY KEY("SpendID","MonthYR"),
	FOREIGN KEY("VendID") REFERENCES "Vendor"("VendID")
);
             """)

conn.commit()
conn.close()