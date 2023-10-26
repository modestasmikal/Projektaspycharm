metai = ("jeigu zmogui nera 22 metai negali i eiti i kazino")

kazino = int(input("Prasome patvirtinti savo amziu"))
metai = 22

if kazino > metai:
    print("Sveiki atvyke i kazino")

if kazino < metai:
    print("Atleiskite mes negalime i leisti jum nera 22 metai")

metai= 14
if metai < 22:
    print("Jus galite i eiti")
else:
    print("ju  negalite i eiti")

metai = 16
if metai >= 22:
    print("jus galite eiti i kazino")
else:
    print("Jus negalite eiti i kazino")


kazino = int(input("Prasome patvirtinti savo amziu"))
metai = 22

if kazino >= metai:
    print("Sveiki atvyke i kazino")
else:
    print("Jus negalite i eiti i kazino")

kazino = int(input("Prasome patvirtinti savo amziu"))
metai = 22

if kazino > metai:
    print("Sveiki atvyke i kazino")
elif kazino == metai:
    print("-" * 30)
    print("Sveikiname jus turite lygiai",kazino ,"metu.",)
    print("-"* 30)
else:
    print("-" * 30)
    print("Jus negalite i eiti i kazino")
    print("-" * 30)
    print(f"Uz {metai - kazino}m. Jus galesite patekti i kazino")
    print(" ----> Iki susitikimo! <----")
if(kazino % 10) == 0:
    print("Sveikiname jus su", kazino,"metu", "jubiliejum!",)

