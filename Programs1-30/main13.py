items={"Laptop": 1200,"Smartphone": 900,"Headphones": 1200,"Tablet": 700}
maxPrice=max(items.values())
highest=[]
for item, price in items.items():
    if price == maxPrice:
        highest.append(item)
print("Highest Value is: ",maxPrice,"For this items",highest)