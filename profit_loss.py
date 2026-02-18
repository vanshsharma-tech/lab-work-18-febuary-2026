cost_price = float(input("Enter the cost price (In Rs.):"))

if cost_price < 0:
    print("Cost price must a positive value:")
    exit()
else:
    selling_price = float(input("Enter the selling price (In Rs.):"))
    if (selling_price > cost_price):
        profit_amount = selling_price - cost_price
        print("We got the profit on the item which is ", profit_amount, " Rs.")
    elif (selling_price < cost_price):
        loss_amount = selling_price - cost_price
        print("We got the profit on the item which is", loss_amount, " Rs.")
    else:
        print("There is no profit and no loss")
