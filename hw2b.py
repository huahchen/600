test = 0
count = 0
highest = 0
canBuy = False

a = 0
b = 0
c = 0

for n in range(1,50):
    while 6*a + 9*b + 20*c  < n:

        while 6*a + 9*b + 20*c < n:

            while 6*a + 9*b + 20*c < n:
                a += 1
                if 6*a + 9*b + 20*c  == n:
                    canBuy = True
                    break
            
            a = 0
            b += 1
            if 6*a + 9*b + 20*c == n:
                canBuy = True
                break
        
        a = 0
        b = 0
        c += 1
        if 6*a + 9*b + 20*c == n:
            canBuy = True
            break
    
    a = 0
    b = 0
    c = 0

    if canBuy == False:
        highest = n
        print "highest =", highest
    
    canBuy = False
print "Largest number of McNuggets that cannot be bought in exact quantity:", highest
