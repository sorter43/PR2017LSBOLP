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
    filmi.append(row["anime_id"])


tabela = {}
tabelaUp = {}

for i in uporabniki:
    print("tabela uporabnikov gradnja")
    if i[0] not in tabelaUp:
        tabelaUp[i[0]] = {}
    if i[1] not in tabelaUp[i[0]]:
        tabelaUp[i[0]][i[1]] = i[2]

prvaV = ","
for i in range(1,73517):
    prvaV += str(i)+","

prvaV = prvaV[:-1]
prvaV += "\n"

print("Zapisovanje v datoteko")
f = open("oceneAnimeevdvaD.csv" ,"w")
f.write(prvaV)
vrstica = ""

for i in filmi:
    print("zapisovanje vrstice")
    vrstica = ""+i+","
    for y in range(0,73517):
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