import random

def general():
    a=random.randint(1,50)
    return a
def kiiras(szam):
    a=szam
    print(f"I/A:\n\n\tA generált szám:", szam)
    if (szam % 5 )== 0:
        print(f"\nI/B:\n\n\tA szám öttel osztható!")
    elif (szam % 3) == 0:
        print(f"\nI/B:\n\n\tA szám hárommal  osztható!" )
    elif (szam % 5 == 0) and (szam % 3 == 0):
        print(f"\nI/B:\n\n\tA szám öttel és hárommal is osztható!")
    else :

        print(f"\nI/B:\n\n\tA szám sem 5 el sem 3 mal nem osztható" )


