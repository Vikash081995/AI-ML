staff = [("amit",16),("rahul",20),("sneha",15),("anita",22)]

for name,age in staff:
    if age<18:
        print(f"{name} is underaged. Cannot assign night shift.")
        break
else:
    print("All staff members are eligible for night shift assignment.")