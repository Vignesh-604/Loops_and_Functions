i = 1
while i <= 1:
    i += 1
    print(i)
print("It's over.")

# A small guessing game using While loops and If statements.
passcode = 'Catt0'
guess = ""
chance = 0
chance_limit = 2
nope = False

while guess != passcode and not nope:
    if chance <= chance_limit:
        guess = input("Password:")
        chance += 1
    else:
        nope = True

if nope:
    print("Locked.")
else:
    print("You're in.")
