def korok_lista():
    kor=[]
    for i in range(5):
        a = int(input("kérem adjon meg egy kort:"))
        if a<0 or a>120:
            while(a<0 or a>120):
                a=int(input("kérem adjon meg egy kort"))
        kor.append(a)
    print("II/A, B, C:\n\n\t ",)
    for i in range(len(kor)-1):
        print(kor[i], end=":")
    print(kor[len(kor)-1] ,end="")

    return kor
def elso_idos(kor):
    for i in range(len(kor)):
        x=kor[i]
        if x>70:
            return i

def konzolra_ir ( i):

    print(f"\n\nII/D, E:\n\n\t Első idős ember korának helye a listában:" ,i)
    return i
def fajl_ir(x):
    a=x
    f = open("oreg.txt", "w")
    f.write(f"\n\nII/D, E:\n\n\t Első idős ember korának helye a listában:")
    f.write( x, end="")