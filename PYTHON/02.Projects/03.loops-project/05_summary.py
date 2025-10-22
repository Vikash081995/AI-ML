names =["hitesh","vaibhav","ankit","parth","yash","dhruv"]
bills=[100,150,200,250,300,350]

for name,amount in zip(names,bills):
    print(f"Generating bill of Rs.{amount} for {name}")