while True:

    print(
        "------------ ""\n"
        "1. Sudetis" "\n"
        "2. Atimtis" "\n"
        "3. Daugyba" "\n"
        "4. Dalyba" "\n"
        "5. Seka"   "\n"
        "q - Iseiti""\n"

        "---------------",
    )
    meniu_pasirinkimas = input(f"Pasirinkite jums norima funkcija \n >>>>")

    if meniu_pasirinkimas == "q":
        print("BYE BYE")
        break

    if meniu_pasirinkimas not in ("1", "2", "3", "4", "5"):
        print("Tokio pasirinkimo nėra")
        continue
        # naudojam float - skaičius su kableliu
    sk1 = float(input("Įveskite pirmąjį skaičių "))
    sk2 = float(input("Įveskite antrąjį skaičių "))

    if meniu_pasirinkimas == "1":
        res = f"{sk1} + {sk2} = {sk1 + sk2}"

    elif meniu_pasirinkimas == "2":
        res = f"{sk1} - {sk2} = {sk1 - sk2}"

    elif meniu_pasirinkimas == "3":
        res = f"{sk1} * {sk2} = {sk1 * sk2}"
