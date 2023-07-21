amount_due = 50
change_owed = 0
while amount_due != 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due = amount_due - coin
        if amount_due <=  0:
            change_owed = change_owed - amount_due
            print("Change Owed:", change_owed)
            break