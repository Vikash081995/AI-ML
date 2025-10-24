def serve_chai():
    chai_type="Masala"#local variable
    print(f"Inside function {chai_type}")
    
chai_type ="Lemon"
serve_chai()
print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "lemon" #enclosing scope
    def print_order():
        chai_order = "Masala" #local variable
        print(f"Your chai is {chai_order}")
    print_order()
    print(f"Your chai is {chai_order}")  

chai_counter()