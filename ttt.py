
# 1. Pasisveikinimas:
print("Sveiki atvykę į 0-X iššūkį! Linkime linksmo žaidimo.")

# 2. Paaiškinimas žaidėjui, kaip žymimos lentelės vietos, kad galėtų tinkamai pasirinkti:
zaidimas = ["Langelių, kuriuos galėsite pasirinkti, nr.:\n|1|2|3|\n|4|5|6|\n|7|8|9|"]
print(zaidimas[0])

# 3. Žaidimo pradžios paskelbimas:
print("Pradedame!")

# 4. Nustatau tuščią lentą, su kuria dirbsiu toliau programuojant (kintamasis),
ttt_lenta = ["| | | |\n| | | |\n| | | |"]
# print(ttt_lenta[0])

# 5. F-ja lentos pateikimui
def pateikti_lenta():
    print(ttt_lenta[0])

# # 6. F-ja, reikalinga tinkamų įrašų į lentą atlikimui, programai nurodant taškų koordinates
def atnaujinti_lenta(pazymima_vieta, zaidejo_simbolis):
    pazymimos_vietos = {
        "1": (1, 1), "2": (1, 2), "3": (1, 3),
        "4": (2, 1), "5": (2, 2), "6": (2, 3),
        "7": (3, 1), "8": (3, 2), "9": (3, 3)
    }
# Tikrinsime žaidėjo įvesto langelio nr. tinkamumą:
    if pazymima_vieta in pazymimos_vietos.keys():
        eilute, stulpelis = pazymimos_vietos[pazymima_vieta]
        if ttt_lenta[eilute][stulpelis] == " ":
           ttt_lenta[eilute][stulpelis] = zaidejo_simbolis
           return True
        else:
            print("Langelis užimtas, pasirinkite laisvą langelį")
            return False

    else:
        print("Įvestas netinkamas langelio numeris, turite įvesti laisvą langelį (1 - 9)")
        return False

    return True

# Tikriname laimėtoją (x ir y asiu atzvilgiu, istrizainiu atzvilgiu):

def patikrinti_laimetoja():
    for eilute in ttt_lenta:
        if eilute.count("X") == 3:
            return "X"
        elif eilute.count("O") == 3:
            return "O"

    for stulpelis in range(3):
        if ttt_lenta[0][stulpelis] == ttt_lenta[1][stulpelis] == ttt_lenta[2][stulpelis] != " ":
            return ttt_lenta[0][stulpelis]

    if ttt_lenta[0][0] == ttt_lenta[1][1] == ttt_lenta[2][2] != " ":
        return ttt_lenta[0][0]
    elif ttt_lenta[0][2] == ttt_lenta[1][1] == ttt_lenta[2][0] != " ":
        return ttt_lenta[0][2]

    return None

#  Žaidėjai įrašo skaičių, pagal kurio koordinate X arba O nukeliauja į lentą.
while True:
    pateikti_lenta()
    a = input("X žaidėjas - pasirinkite nepažymėto langelio Nr. (1-9): ")
    if a in "123456789":
        atnaujinti_lenta(a, "X")
        laimetojas = patikrinti_laimetoja()
        if laimetojas:
            print(f"Laimėjo {laimetojas}!")
            break
        else:
            continue
    else:
        print("Įvedėte neteisingą simbolį arba langelis jau pažymėtas")

    b = input("O žaidėjas - pasirinkite nepažymėto langelio Nr. (1-9): ")
    if b in "123456789":
        atnaujinti_lenta(b, "O")
        laimetojas = patikrinti_laimetoja()
        if laimetojas:
            print(f"Laimėjo {laimetojas}!")
            break
        else:
            continue
    else:
        print("Įvedėte neteisingą simbolį arba langelis jau pažymėtas")


