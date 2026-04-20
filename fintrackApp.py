#fintracker functions

from fintrackFunc import ins_func, month_all, month_spend, del_func, curr_month, curr_id, vend_id, update_func

#fintracker app

def app_run():
    run = True

    while run is True:
        print("""
------------------------------------------------------------------------
Hello. Please select a choice below:
------------------------------------------------------------------------
Related to Month Spending:
    1. View all listed in given month
    2. View highest single expenditure in a given month
    3. View total spending in a given month
Related to editing data:
    4. Insert an input
    5. Delete an input
    6. Update an input
Other:
    Q. Quit
------------------------------------------------------------------------
------------------------------------------------------------------------
              """)
        action = input("Key in choice here: (in the form of the number/letter) ")
        
        if action == "1":
            month = input("For which month? (MM/YY) ")

            x = month_all(month)

            #in case of bad input

            if x == []:
                print("No records.")

            elif x == ["Data invalid."]:
                print(x[0])
            
            else:
                print("| Storename     | Cost           | Comment       |")
                for i in month_all(month):
                    print(f"| {i[1]:<14}| {i[2]:<14} | {i[3]:<14}|")

        elif action == "2":
            month = input("For which month? (MM/YY) ")

            x = month_spend(month)

            #in case of bad input
            if x == []:
                print("No records.")

            elif x == ["Data invalid."]:
                print(x[0])
            
            else:
                print("| Storename     | Cost           | Comment       |")
                for i in month_spend(month):
                    print(f"| {i[0]:<14}| {i[1]:<14} | {i[2]:<14}|")
                
        elif action == "3":
            month = input("For which month? (MM/YY) ")
            print(f"Current month spending is: ${curr_month(month)}")

        elif action == "4":
            #(date 0, vendid 1, vendname 2, spendid 3, cost 4, comments 5, class 6)
            dt = input("Which month? (MM/YY) ")
            vndn = input("Spent where? ")
            cst = input("How much spent? (XX.XX) ")
            cmt = input("Additional comments? ")
            clss = input("Class? (Food OR Apparel/Accessories OR Others) ")

            s_id = curr_id()
            v_id = vend_id(vndn)

            #print((dt, v_id, vndn, s_id, cst, cmt, clss))

            ins_func((dt, v_id, vndn, s_id, cst, cmt, clss))

        elif action == "5":
            month = input("Deleting from which month? (MM/YY) ")
            print("| ID | Storename     | Cost           | Comment       |")

            x = month_all(month)

            if x == []:
                print("No records.")

            elif x == ["Data invalid."]:
                print(x[0])

            else:
                for i in x:
                    print(f"|  {i[0]} | {i[1]:<14}| {i[2]:<14} | {i[3]:<14}|")
                
                d_id = input("Which ID to delete? ")
                
                del_func(d_id, month)
            

        elif action == "6":
            month = input("Updating from which month? (MM/YY) ")
            
            x = month_all(month)

            if x == []:
                print("No records.")

            elif x == ["Data invalid."]:
                print(x[0])
            
            else:
                print("| ID | Storename     | Cost           | Comment       |")
                for i in x:
                    print(f"|  {i[0]} | {i[1]:<14}| {i[2]:<14} | {i[3]:<14}|")

                u_id = input("Which ID to update? ")
                chng = input("Which value to change? ('SpendID', 'MonthYR', 'Cost', 'VendID', 'Comments'): ")
                new_v = input("Key in new value: ")

                #print(chng, new_v, u_id)
                if chng == "MonthYR" or chng == "Comments": 
                    update_func(chng, new_v, u_id, month)
                elif chng == "SpendID" or chng == "VendID":
                    update_func(chng, int(new_v), u_id, month)
                elif chng == "Cost":
                    update_func(chng, float(new_v), u_id, month)
                else:
                    print("No such column, try again.")

        elif action in "Qq":
            run = False

        else:
            print("Not an option. Try again!")
        print("\n\n")

app_run()