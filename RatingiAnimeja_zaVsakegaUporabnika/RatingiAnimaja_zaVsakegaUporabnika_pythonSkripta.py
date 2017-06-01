from csv import *

reader = DictReader(open("rating.csv","rt", encoding = "utf-8"))
uporabniki = list();
filmi = list()

for row in reader:
    print("berem dat!")
    uporabniki.append([row["user_id"],row["anime_id"],row["rating"]])
    filmi.append(row["anime_id"])



reader = DictReader(open("anime.csv","rt", encoding = "utf-8"))
filmi = list()

for row in reader:
    print("berem dat!")
    if ("Sc-Fi" in row["genre"]) or ("Comedy" in row["genre"]) or ("Fantasy" in row["genre"]) or ("Shounen" in row["genre"]) or ("Action" in row["genre"]):
        filmi.append(row["anime_id"])


tabela = {}
tabelaUp = {}

for i in uporabniki:
    print("tabela uporabnikov gradnja")
    if i[0] not in tabelaUp:
        tabelaUp[i[0]] = {}
    if i[1] not in tabelaUp[i[0]]:
        tabelaUp[i[0]][i[1]] = i[2]

prvaV = "ID,"
for i in range(1,1000):
    prvaV += "user"+str(i)+","

prvaV = prvaV[:-1]
prvaV += "\n"

print("Zapisovanje v datoteko")
f = open("RatingiAnimaja_zaVsakegaUporabnika_tabela.csv" ,"w")
f.write(prvaV)
vrstica = ""

for i in filmi:
    print("zapisovanje vrstice")
    vrstica = ""+i+","
    for y in range(0,1000):
        y = str(y)
        if y in tabelaUp:
            if i in tabelaUp[y]:
                if tabelaUp[y][i] == "-1":
                    vrstica += "?,"
                else:
                    vrstica += str(tabelaUp[y][i]) + ","
            else:
                vrstica += "?,"
    vrstica = vrstica[:-1]
    vrstica+="\n"
    f.write(vrstica)