chai_typ="plain"

def front_desk():
    def kitchen():
        global chai_typ
        chai_typ="Masala"
    kitchen()

front_desk()
print(chai_typ)