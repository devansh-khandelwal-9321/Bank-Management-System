import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank_db"
)

cursor = conn.cursor()



def create_account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    query = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
    values = (name, balance)

    cursor.execute(query, values)
    conn.commit()

    print("Account Created Successfully!")
    print("Account Number:", cursor.lastrowid)



def deposit():
    acc_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Deposit Amount: "))

    query = "UPDATE accounts SET balance = balance + %s WHERE account_no = %s"
    values = (amount, acc_no)

    cursor.execute(query, values)
    conn.commit()

    print("Deposit Successful!")



def withdraw():
    acc_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=%s",
        (acc_no,)
    )

    result = cursor.fetchone()

    if result:
        balance = float(result[0])

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= balance:
            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE account_no = %s",
                (amount, acc_no)
            )

            conn.commit()
            print("Withdrawal Successful!")

        else:
            print("Insufficient Balance!")

    else:
        print("Account Not Found!")



def check_balance():
    acc_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT * FROM accounts WHERE account_no=%s",
        (acc_no,)
    )

    result = cursor.fetchone()

    if result:
        print("\nAccount Number:", result[0])
        print("Name:", result[1])
        print("Balance:", result[2])

    else:
        print("Account Not Found!")



def view_accounts():
    cursor.execute("SELECT * FROM accounts")

    records = cursor.fetchall()

    print("\n--- All Accounts ---")

    for row in records:
        print(
            f"Acc No: {row[0]} | Name: {row[1]} | Balance: ₹{row[2]}"
        )



while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        view_accounts()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

conn.close()
