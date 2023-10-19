import ciklusok

a: int = int(input("Kérek egy számot: "))
b: int = int(input("Kérek mégegy számot: "))
""" A felhasználó csak olyan b-t tudjon megadni, ami nagyobb, mint az a """

while a >= b:
    print("B-nek nagyobbnak kell lennie A-nál!")
    b: int = int(input(f"Adj {a}-nál/nél nagyobbat! "))

ciklusok.szamok(a,b)

