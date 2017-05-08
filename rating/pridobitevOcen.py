from csv import *

filmi = list()

reader = DictReader(open("anime.csv","rt", encoding = "utf-8"))


for row in reader:
    filmi.append(row["rating"])


print("Zapisovanje v datoteko")
f = open("SamoOcene.csv" ,"w")
f.write("rating\n")
for k in filmi:
    f.write(str(k)+"\n")
print("done!!!!!!!!!!!!!!!!!!!!!!!!!")