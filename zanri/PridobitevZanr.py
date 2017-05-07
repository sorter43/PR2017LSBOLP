from csv import *

filmi = list()

reader = DictReader(open("anime.csv","rt", encoding = "utf-8"))


for row in reader:
    filmi.append(row["genre"])

vseZanre = {}
for zanre in filmi:
    zanr = zanre.split(",")
    for z in zanr:
        z = z.strip()
        if z in vseZanre:
            vseZanre[z] = vseZanre[z]+1
        else:
            vseZanre[z] = 1

print("Zapisovanje v datoteko")
f = open("statistikaZanrov.csv" ,"w")
f.write("zanr,statistikaZanra\n")
for k in vseZanre:
    f.write(str(k)+","+str(vseZanre[k])+"\n")
print("done!!!!!!!!!!!!!!!!!!!!!!!!!")