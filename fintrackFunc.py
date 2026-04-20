#background functions

import sqlite3

def ins_func(s_det):
    #assume s_det takes format of (date 0, vendid 1, vendname 2, spendid 3, cost 4, comments 5, class 6)
    conn = sqlite3.connect("finrec_.db")
    
    #print(s_det)

    curs = conn.cursor()

    #data validation
    run = True
    
    if len(s_det[0]) == 5 and s_det[0][0:2].isnumeric() == True and s_det[0][3:5].isnumeric() == True:
        pass
    else:
        run = False

    try:
        float(s_det[4])
        #print(float(s_det[4]))
    except ValueError:
        run = False
        #print("ValueError")

    if s_det[6] not in ["Food", "Apparel/Accessories", "Others"]:
        run = False

    #check if vendor already exists
    vendcheck = conn.cursor()

    vendcheck.execute("""
                SELECT VendID
                FROM Vendor
                WHERE VendName = ?
                 """, (s_det[2],))

    vendid = vendcheck.fetchone()

    if run == True:
        #insert spending data into the 2 tables established via initiation.py
        #ID not actually needed to insert, given autoincrement
        curs.execute("INSERT INTO 'Spending'('SpendID', 'MonthYR', 'Cost', 'VendID', 'Comments') VALUES(?, ?, ?, ?, ?)", (s_det[3], s_det[0], float(s_det[4]), s_det[1], s_det[5], ))
        
        if vendid == None:
            curs.execute("INSERT INTO 'Vendor'('VendID', 'VendName', 'Class') VALUES(?, ?, ?)", (s_det[1], s_det[2], s_det[6], ))
    else:
        print("Data is invalid.\n")

    conn.commit()
    conn.close()

def month_all(inpMonthYr):
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()

    #data validation 
    if len(inpMonthYr) == 5 and inpMonthYr[0:2].isnumeric() == True and inpMonthYr[3:5].isnumeric() == True:
    
        curs.execute("""
                    SELECT 'Spending'.'SpendID', 'Vendor'.'VendName', 'Spending'.'Cost', 'Spending'.'Comments'
                    FROM 'Spending', 'Vendor' 
                    WHERE 'Spending'.'VendID' = 'Vendor'.'VendID'
                    AND 'Spending'.'MonthYR' = ?
                    """, (inpMonthYr, ))

        lst_all = curs.fetchall() #as multiple events might be the same expense
        #print(lst_all, "TEST")

    else:
        
        return ["Data invalid."]
    
    conn.commit()
    conn.close()

    return lst_all

def month_spend(inpMonthYr): #to showcase highest expenditure in a month
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()
    
    #data validation
    if len(inpMonthYr) == 5 and inpMonthYr[0:2].isnumeric() == True and inpMonthYr[3:5].isnumeric() == True:

        curs.execute("""
                    SELECT 'Vendor'.'VendName', 'Spending'.'Cost', 'Spending'.'Comments'
                    FROM 'Spending', 'Vendor' 
                    WHERE 'Spending'.'VendID' = 'Vendor'.'VendID'
                    AND 'Spending'.'Cost' =
                    (SELECT MAX('Spending'.'Cost')
                    FROM 'Spending', 'Vendor' 
                    WHERE 'Spending'.'VendID' = 'Vendor'.'VendID'
                    AND 'Spending'.'MonthYR' = ?)
                    AND 'Spending'.'MonthYr' = ?
                    """, (inpMonthYr, inpMonthYr, ))

        lst_max = curs.fetchall() #as multiple events might be the same expense
    #print(lst_max, "TEST")
    
    else:

        return ["Data invalid."]

    conn.commit()
    conn.close()

    return lst_max

def id_finder(inpMonthYr): #list ids in a month

    conn = sqlite3.connect("finrec_.db")
        
    curs = conn.cursor()

    curs.execute("""
                SELECT 'Spending'.'SpendID'
                FROM 'Spending'
                WHERE 'Spending'.'MonthYR' = ?
                """, (inpMonthYr, ))

    lst_ids = curs.fetchall()

    ids = [id for id, in lst_ids]

    conn.commit()
    conn.close()

    return ids

def del_func(del_inp, inpMonthYr): #removal of a spending record
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()
    
    #data validation 
    if del_inp.isnumeric() == True:
        int_inp = int(del_inp)

        if int_inp in id_finder(inpMonthYr): 
            curs.execute("""
                        DELETE FROM 'Spending' WHERE 'Spending'.'SpendID' = ?
                        """, (int_inp, ))
        else:
            print("Not a valid ID.\n")
        
    else:
        print("Data invalid.\n")

    conn.commit()
    conn.close()

def curr_month(inpMonthYr): #to showcase total spending in a month 
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()

    #data validation 
    if len(inpMonthYr) == 5 and inpMonthYr[0:2].isnumeric() == True and inpMonthYr[3:5].isnumeric() == True:

        curs.execute("""
                    SELECT SUM(Cost) AS 'Total'
                    FROM Spending 
                    WHERE MonthYR = ?
                    """, (inpMonthYr,))

        total = curs.fetchone()
        #print(total[0], "TEST")
    
    else:
        return "Data invalid."

    conn.commit()
    conn.close()
    
    if total[0] is not None:
        return float(total[0])
    
    else:
        return 0

def curr_id(): #pick out current max ID
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()

    curs.execute("""
                SELECT MAX(SpendID)
                FROM Spending
                 """)

    currid = curs.fetchone()
    #print(currid[0], "TEST")
    
    conn.commit()
    conn.close()

    return int(currid[0]) + 1

def vend_id(vendn): #find vendor id
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()

    curs.execute("""
                SELECT VendID
                FROM Vendor
                WHERE VendName = ?
                 """, (vendn,))

    vendid = curs.fetchone()
    #print(currid[0], "TEST")

    if vendid == None: #if not already in the database
    
        curs = conn.cursor()

        curs.execute("""
                    SELECT MAX(VendID)
                    FROM Vendor
                    """)

        vendid = curs.fetchone()
        #print(currid[0], "TEST")
        
        conn.commit()
        conn.close()

        return int(vendid[0]) + 1
    
    conn.commit()
    conn.close()

    return int(vendid[0])

def update_func(value, new_val, id_, inpMonthYr): #update a spending record
    conn = sqlite3.connect("finrec_.db")
    
    curs = conn.cursor()

    #data validation 
    
    if value == "SpendID" or value == "MonthYR" or value == "Cost" or value == "VendID" or value == "Comments":
        if id_ in id_finder(inpMonthYr): 
            
            curs.execute(f"""
                        UPDATE Spending
                        SET {value} = '{new_val}'
                        WHERE SpendID = ?
                        """, (int(id_), ))
        else:
            print("Not a valid ID\n")

    else:
        print("Data invalid.\n")

    conn.commit()
    conn.close()