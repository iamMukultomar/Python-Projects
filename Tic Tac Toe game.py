b = "TIC TAC TOE"
print(b.center(32, "*"))
print("---------------------------------")
print("Any of the person can start the game.")
a = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
print("Enter the place of your character accordingly.")
print("you can choose b/w \"x\" or \"o\"")

checker = 0
m = True

print(a[0] + "|" + a[1] + "|" + a[2]+"              1|2|3")
print(a[3] + "|" + a[4] + "|" + a[5]+"   ->         4|5|6")
print(a[6] + "|" + a[7] + "|" + a[8]+"              6|7|8")


def board():
    print(a[0] + "|" + a[1] + "|" + a[2])
    print(a[3] + "|" + a[4] + "|" + a[5])
    print(a[6] + "|" + a[7] + "|" + a[8])


def insert(f):
    if a[f-1] != "x" and a[f-1] != "o":
        a[f - 1] = c
        return "1"
    else:
        return "0"


def checkdraw():
    if a[0] == a[1] and a[1] == a[2]:
        if a[0] == "x":
            return "x is the winner"
        elif a[0] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[3] == a[4] and a[4] == a[5]:
        if a[3] == "x":
            return "x is the winner"
        elif a[3] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[6] == a[7] and a[7] == a[8]:
        if a[6] == "x":
            return "x is the winner"
        elif a[6] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[0] == a[3] and a[3] == a[6]:
        if a[0] == "x":
            return "x is the winner"
        elif a[0] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[1] == a[4] and a[4] == a[7]:
        if a[1] == "x":
            return "x is the winner"
        elif a[1] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[2] == a[5] and a[5] == a[8]:
        if a[2] == "x":
            return "x is the winner"
        elif a[2] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[0] == a[4] and a[4] == a[8]:
        if a[0] == "x":
            return "x is the winner"
        elif a[0] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"

    elif a[2] == a[4] and a[4] == a[6]:
        if a[2] == "x":
            return "x is the winner"
        elif a[2] == "o":
            return "o is the winner"
        else:
            return "winner not yet decided"
    else:
        return "Winner not yet decided"


def draw(q):
    if "-" in a:
        q = True
    else:
        q = False
        print("Draw")


while m:
    c = input("Enter the character you want to put:")
    c = c.lower()

    if checker == c:
        print("Invalid input Try again")
        continue
    else:
        checker = c

    if c == "x":
        e = int(input("Enter the place of x: "))

        if e in range(1, 10):
            z = insert(e)
            if z == "1":
                board()
            else:
                print("invalid input try again")
                continue
            p = checkdraw()
            if p == "x is the winner":
                print(p)
                break
            print(p)
        else:
            print("Invalid input try again.")
            continue
        draw(m)
    
    elif c == "o":
        e = int(input("Enter the place of o: "))
        if e in range(1, 10):
            z = insert(e)
            if z == "1":
                board()
            else:
                print("invalid input try again")
                continue
            p = checkdraw()
            if p == "o is the winner":
                print(p)
                break
            print(p)
        else:
            print("Invalid input try again.")
            continue
        draw(m)
    
    else:
        print("Invalid input restart the Game.")
        i = 10
        break
print("Have a nice day,BYE")
