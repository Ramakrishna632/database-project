import sqlite3 as sql
from datetime import datetime, date
import random
import string
import time
con = sql.connect('Ram')
cur = con.cursor()
cur.execute("SELECT * FROM medplus")
all_items = cur.fetchall()
print("Available Medicines:")
print("----------------------------")
for item in all_items:
    print("\t".join(str(x) for x in item))
print("----------------------------")
ch = 'y'
while ch == 'y':
    order_list = []
    while True:
        mname = input("Enter Product Name: ").strip()
        quantity = int(input("Enter Quantity: "))
        cur.execute("SELECT mid, mname, pcost, availability, purchesed FROM medplus WHERE mname = ?", (mname,))
        item = cur.fetchone()
        if item:
            mid, name, cost, availability, purchesed = item
            if availability >= quantity:
                new_availability = availability - quantity
                new_purchesed = quantity
                cur.execute("UPDATE medplus SET availability = ?, purchesed = ? WHERE mname = ?",
                            (new_availability, new_purchesed, mname))
                order_list.append((mid, name, cost, quantity, cost * quantity))

            else:
                print(f"Only {availability} items available for {name}.")
        else:
            print("Item not found.")

        more = input("Do you want to add more items (y/n): ").strip().lower()
        if more != 'y':
            print("stock not available")
            break

    # Generate and print bill
    if order_list:
        total = sum(item[4] for item in order_list)
        gst = total * 0.30
        final_total = total + gst
        bill_no = random.randint(1000, 9999)
        current_time = datetime.now().strftime("%H:%M:%S")

        #print("\n\n--------- Final Bill ---------")
        print("  Kundavai Chettinadu Restaurant")
        print("  Ramamurthy Nagar Main Road")
        print("  Bangalore - 560016")
        print("------------------------------")
        print("Date:", date.today(), "  Time:", current_time)
        print("Bill No:", bill_no)
        print("------------------------------")
        print("Item\tQty \tRate \tTotal")
        print("------------------------------")
        for item in order_list:
            print(f"{item[1]}\t{item[3]}\t{item[2]}  \t{item[4]}")
        print("------------------------------")
        print(f"Subtotal:\t\t\t{total}")
        print(f"GST (30%):\t\t\t{int(gst)}")
        print(f"Total Amount:\t\t{int(final_total)}")
        print("------------------------------")
    ch = input("       Visit Agai").strip().lower()


    con.commit()
else:
        print("________________________________")
con.close()