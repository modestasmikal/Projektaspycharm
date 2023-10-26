counter = 0
PIN = "1234"
BLOCK = 4
LEFT = 4
while True:
    user = input("Iveskie seifo koda")

    if not user.isdigit():
        print("Ivedete ne skaiciu")
        print("--------")
        continue

    counter += 1
    LEFT -= 1
    if counter == BLOCK:
        print(f"Jus nebeturite {BLOCK} spejimu,jusu paskyra uzblokuota")
        break
    if user == PIN:
        print(f"seifas atsidare, is {counter} karto")
        break

    if not 4 < int(len(user)):
        print(f"Seifo kodo ilgis per trumpas.\nJums liko bandymu : {LEFT}")
        continue

    else:
        not 4 > int(len(user)):
            print(f"Seifo kodo per ilgas.\nJums liko bandymu: {LEFT}")
            continue


    print(f"Seifas buvo bandomas nulausti {counter } kartus")
print("--------")
print("Isejome is pakartojimo")