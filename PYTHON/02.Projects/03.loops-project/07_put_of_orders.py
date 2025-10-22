flavours =["Masala Tea","Ginger Tea","Lemon Tea","Green Tea","Black Tea"]

for flavour in flavours:
    if flavour== "Green Tea":
        print("Green Tea is out of stock. Skipping this order.")
        continue
    print(f"Preparing {flavour}...")
print("All possible tea orders have been processed.")