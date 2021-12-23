def gen_progres(dl):
    import random
    c = 0
    prog = []
    shag = random.randint(1,5)
    nach = random.randint(1,15)
    for i in range(dl):
        prog.append(nach + shag*i)
    hid = random.randint(1,dl)
    key = ".."
    prog[hid],key = key,prog[hid]
    return prog , key 
def game_prog(name):
    import random
    c = 0
    while c != 3:
        print("What number is missing in the progression?")    
        g = random.randint(5,10)
        qwest, k = gen_progres(g)
        print("Qwestion:",*qwest)
        ans = int(input("Your answer "))
        if ans == k :
            print("Correct!")
            c += 1
        else :
            print("Let's try again,",name)
            return 0
    if c == 3 :
        print("Congratulations,",name)
        return c