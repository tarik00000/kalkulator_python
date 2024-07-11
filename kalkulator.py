play_again = True
while play_again:
    try:
        a = int(input("Unesi 1 broj za kalkulaciju: "))
        b = int(input("Unesi 2 broj za kalkulaciju: "))
        c = input("Unesi neki od ovih izabrnaih (-,+,/,*) : ")
        match c:
            case '-':
                rezultat=a-b
                print(a, "-", b, "=" , rezultat)    
            case '+':
                rezultat=a+b
                print(a, "+", b, "=" , rezultat)
            case '/':
                rezultat=a/b
                print(a, "/", b, "=" , rezultat)
            case '*':
                 rezultat=a*b   
                 print(a, "*", b, "=" , rezultat)

        play_again_input = input("Da li hocete da pokusate ponovo? (y/n) ")
        if play_again_input.lower() != "y":
            play_again = False
    except:
        ValueError("Niste unjeli broj pokusaj te ponovo")
        continue
    
