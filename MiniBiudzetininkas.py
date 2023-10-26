pajamos = []
islaidos = []
pilnos_pajamos = 0
pilnos_islaidos = 0
while True:
    print("----------------------------------")
    print("Sveiki i progaram - MiniBiudžetas")

    print("-------------------------""\n"
          "1 . Įvesti pajamas""\n"
          "2 . Įvesti išlaidas""\n"
          "3 . Atspausdinti pajamų eilutes""\n"
          "4 . Atspausdinti išlaidų eilutes""\n"
          "5 . Atspausdinti statistiką""\n"
          "6 . Atspausdinti isklotine""\n"
          "q - Išeiti""\n"
        "--- --------------------------")
    pasirinkimas = input(">>>")

    if pasirinkimas == "q":
        print("BYE BYE")
        break

    if pasirinkimas not in ("1", "2", "3", "4", "5", "6"):
        print(("Tokio pasirinkimo nera"))
        continue

    if pasirinkimas == "1":
        duomenys = ["", "", 0, "Pajamos" ]
        duomenys[0] = int(input("Iveskite mėnesį: "))
        duomenys[1] = input("Iveskite pajamų pavadinimą")
        duomenys[2] = int(input("Iveskite sumą"))
        pajamos.append(duomenys)
        pilnos_pajamos += duomenys[2]

    elif pasirinkimas == "2":
        duomenys = ["", "",-0,"Islaidos"]
        duomenys[0] = int(input("Iveskite mėnesį: "))
        duomenys[1] = input("Iveskite Islaidu pavadinimą")
        duomenys[2] = int(input("Iveskite sumą"))
        islaidos.append(duomenys)
        pilnos_islaidos += duomenys[2]

    elif pasirinkimas == "3":
        for l in pajamos:
            print(*l)

    elif pasirinkimas == "4":
        for l in islaidos:
            menuo, pavadinimas, suma =l[0], l[1], l[2]
            print(f"{menuo} {pavadinimas}: -{suma}")

    if pasirinkimas =="5":
        for l in pajamos:
            print("Suvestu pajamu sarasas")
            print(*l)
        for l in islaidos:
            print("Suvestu islaidu sarasas")
            print(*l)
        print(f"Bendro pajamos  {pilnos_pajamos}")
        print(f"Bendros Islaidos -{pilnos_islaidos}")
        print(f"Balansas {pilnos_pajamos - pilnos_islaidos}")

    if pasirinkimas == "6":
        suvestine = pajamos + islaidos
        paeiliui =sorted(suvestine, key=lambda x: x[0])
        for l in paeiliui:
            print(*l)







