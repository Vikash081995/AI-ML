# chai ="Giner chai"

# def prepare_chai(order):
#     print("Preparing",order)
    
# prepare_chai(chai)

chai=[1,2,4,3]

def edit_chai(cup):
    cup[1]=42

edit_chai(chai)
print(chai)

def make_chai(tea,milk,sugar):
    print(f"Making chai with {tea} tea, {milk} milk and {sugar} sugar")

make_chai(tea="green",milk="yes",sugar="No")


def special_chai(*ingredients, **extras):
    print("Ingredients",ingredients)
    print("Extras",extras)
    
special_chai("Cinnamom","Cardamom",sweetener="Honey",foam="yes")