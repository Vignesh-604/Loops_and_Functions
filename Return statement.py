def POLO(num, pup):
    return num+pup
print(POLO(9, 6))

def ROLO(Var1, Var2):
    return f"Variable no.1 is {Var1} and Variable no.2 is {Var2}"
print(ROLO("Cat", "Dog"))

def HOLO(cat, dog):
    return cat or dog                        # 'Or' shows the smaller number.
print(HOLO(5, 7))

def GOLO(rat, bat):
    return rat and bat                       # 'And' shows the bigger number.
print(GOLO(4, 8))

def YOLO():
    return print("This is a return statement.")
  
print(YOLO())                                # If the function has a 'print' statement in return, then printing it again
                                             # will give out a "NONE" along with the statement.

YOLO()                                       # To get just the sentence, just type out the function name.
