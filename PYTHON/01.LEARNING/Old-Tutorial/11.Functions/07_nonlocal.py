def update_chai():
    chai_type= "Masala"
    def kitchen():
        nonlocal chai_type
        chai_type="Lemon"
        print(f"Inside function {chai_type}")
    kitchen()
    print(f"Outside function {chai_type}")

update_chai()