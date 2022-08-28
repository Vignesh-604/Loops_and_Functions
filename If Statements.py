# If satements with boolean values.
is_wild = True
is_huge = True
is_sunfy = True

if is_wild and is_huge:                                 # For 'and', both conitions must satisfy.
    print("Bear is a wild or smart.")

elif is_huge or not is_furry:
    print("Bear is huge but not furry.")

elif is_huge or is_furry:                                # For 'or', atleast one of the conditions must satisfy.
    print("Bear is huge and furry.")

else: print("Bear is neither of the three.")
  
# If statements in a function.
def Func(num1, num2, num3):

    if num1 >= num3 and num1 + num3 == num2:
        return "Both conitions are satisfied."

    elif num2 == num1 or num2 != num3:
        return "One of the conditions is satisfied."

print(Func(9, 10, 6))
