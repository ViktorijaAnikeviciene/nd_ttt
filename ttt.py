# 1. Pasisveikinimas:
print("Sveiki atvykę į 0-X iššūkį! Linkime linksmo žaidimo.")

# 2. Paaiškinimas žaidėjui, kaip žymimos lentelės vietos, kad galėtų tinkamai pasirinkti:
zaidimas = ["Langelių, kuriuos galėsite pasirinkti, nr.:\n|1|2|3|\n|4|5|6|\n|7|8|9|"]
print(zaidimas[0])

# 3. Žaidimo pradžios paskelbimas:
print("Pradedame!")

# 4. Nustatau tuščią lentą, su kuria dirbsiu toliau programuojant (kintamasis), sąrašas saraše,
ttt_lenta = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# 5. F-ja lentos pateikimui (lenta būtų su šoniniais rėmais, kad žaidėjui būtų lengviau susigaudyti)
def pateikti_lenta():
    for eilute in ttt_lenta:
        print("|" + "|".join(eilute) + "|")

# 6. F-ja, reikalinga tinkamų įrašų į lentą atlikimui, programai nurodant taškų koordinates
def atnaujinti_lenta(pazymima_vieta, zaidejo_simbolis):
    pazymimos_vietos = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2)
    }
    # 7. Tikrinsime žaidėjo įvesto langelio nr. tinkamumą:
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

# 8. Tikriname laimėtoją (x ir y asiu atzvilgiu, istrizainiu atzvilgiu). Man tai buvo sunkiausia dalis, ieškojau pagalbos internete.
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


#  9. Žaidėjai įrašo skaičių, pagal kurio koordinate X arba O nukeliauja į lentą. Pradedame nuo X žaidėjo.
esamas_zaidejas = "X"

while True:
    pateikti_lenta()
    langelio_nr = input(f"{esamas_zaidejas} žaidėjas - pasirinkite nepažymėto langelio Nr. (1-9): ")
    if langelio_nr in "123456789":
        if atnaujinti_lenta(langelio_nr, esamas_zaidejas):
            laimetojas = patikrinti_laimetoja()
            if laimetojas:
                print(f"Laimėjo {laimetojas}!")
                break
            else:
                esamas_zaidejas = "O" if esamas_zaidejas == "X" else "X"
        else:
            continue
    else:
        print("Įvedėte neteisingą simbolį arba langelis jau pažymėtas")
