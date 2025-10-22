value=13

# remainder = value % 3

if remainder := value%3:
    print(f"{value} is not divisible by 3, remainder is {remainder}")
    
    
available_sizes =["S","M","L","XL","XXL"]

if (requested_size :=input("Enter your preferred size (S,M,L,XL,XXL): ")) in available_sizes:
    print(f"Size {requested_size} is available.")
else:
    print(f"Size {requested_size} is not available.")