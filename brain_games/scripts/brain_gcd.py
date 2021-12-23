def findNOD(zn1,zn2) :
    max = 1
    if zn1 > zn2 :
        zn2,zn1 = zn1,zn2
    for i in range(1,zn2+1):
        if zn2 % i == 0 and zn1 % i == 0:
            max = i 
    return max
def nod(name) :
    import random
    c = 0 
    print("Find the greatest common divisor of given numbers.")
    while c != 3 :
        a = random.randint(1,100)
        b = random.randint(1,100)
        ff = findNOD(a,b)
        print("Question:",a,b)
        ans = int(input("Your answer: "))
        if ans == ff :
            print("Correct!")
            c += 1
        else :
            print("'",ans,"' is wrong answer ;(. Correct answer was '",ff,"'.",sep="")
            print("Let's try again,",name)
            return 0
    if c == 3 :
        print("Congratulations,",name)
        return c
