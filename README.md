# PR2017LSBOLP

Seminarska naloga za predmet Podatkovno rudarjenje na Fakuteti za računalništvo in informatiko
Junij 2017

## Avtorji

 * Leo Andrej Štimac
 * Blaž Ocepek

## Naloga

Za nalogo smo izbrali Kaggle izziv, da le iz uporabniških ratingov napoveš kakšno oceno bi uporabnik dal animeju. Torej za uporabnika ne smemo pričakovati ničesar drugega kot njegove ratinge.  
Za nalogo nameravamo napovedati, ali bo uporabniku všeč anime, ki ga še ni pogledal. Odvisno od povprečne uporabniške ocene smo si zastavili cilj da napovemo oceno uporabnika, po možnosti z največjo absolutno napako 1.  

## Podatki

Pri izzivu sta bili dani 2 podatkovni zbirki:
* anime.csv - bazi z podatki o animejih samih
 * * anime_id - unikatni identifikator animeja; numeric
 * * name - ime animeja; string
 * * genre - vsi žanri, katerim je anime pripisan; string: posamezni žanri ločeni z ","
 * * type - vrsta medija; string [Movie, Music, ONA, OVA, Special, TV]
 * * episodes - število epizod; numeric
 * * rating - poveprečni rating; numeric
 * * members - število ljudi, ki je anime ocenilo; numeric
* ratings.csv - baza ocen uporabnikov za posamezne pare uporabnik-anime
 * *  user_id - unikatni identifikator za uporabnika (in edini način za razlikovanje med uporabniki); numeric
 * *  anime_id - unikatni identifikator animeja; numeric
 * *  rating - ocena, ki jo je uporabnik dal animeju; numeric

## Kriterij

Želimo dobiti boljši algoritem od pripisovanja povprečne ocene, ki je najbolj preprost algoritem, ki še daje sprejemljive rezultate.

Po izračunu smo dobili MSAE ~1.8038.

## Začetna opažanja

 * Rating in število memberjev sta sorazmerno povezana.
 * Vrsta medija ima velik vpliv na konsitentnost in velikost ratingov
 * *  TV ima najboljše ocene
 * *  Movies ima najbolj neenotne ocene

## Razlike od baze pri domači nalogi (movies)

 * Nimamo na voljo časovne oznake, kdaj so uporabniki ocenili anime
 * Manj podatkov:
 * *  ni igralcev
 * *  ni producentov
 * *  ni studia
 * Demografika je predvidoma drugačna kot pri MovieLens, tako da se lahko pričakuje drugačne ugotovitve pri uporabi istih metod
 
## Cilji

 * Boljša varianca od pripisovanja povprečne ocene
 * Preverjanje, če vpeljava novih zunanjih baz/spremenljivk izboljša ali poslabša rezultat
 * *  Baza podatkov animejev skozi čas
 * *  Vpliv studija na oceno
 
# Osnovni podatki

## Obdelava  rating.csv
Koda in vizualizacija v OsnovniPodatki.ipynb
 * Ratinge sem naložil kot numpy array
 * Zaradi časovne zahtevnosti in omejitve velikosti na GitHubu podatke okrajšal na 3*10<sup>5</sup> vnosov, kar je prineslo 22MB ratingSAMPLE datoteko. Originalna datoteka je bila 108MB z čez 7*10<sup>6</sup> vnosi.
 * Da sem očistil podatke sem uproabil 
     data[data[:,2]!=-1,2]
 da se znebim neocenjenih ocen. 
 * Na koncu nismo pogledali vpliva neocenjenih ratingov na oceno filma.
### Statistika ratingSAMPLE.csv
Koda in vizualizacija v OsnovniPodatki.ipynb
 * Vse skupaj 3*10<sup>5</sup> vrstic. V vzorcu je bilo 238592 neocenjenih animejev in 61407 ocenjenih.
 * Povprečna ocena, kjer je bilo ocenjeno, je bila 7.869
 * Standardni odklon: 1.5287193824702126
 * Varianca: 2.3369829503401078
 * Pri minimumu in maksimumu ni bilo presenečenja, najniižji rating je bil najnižji možen, največji pa največji možen
 * Največ ljudi je dalo oceno 8, z 9 in 7 takoj zadaj
### Statistika anime.csv
Koda in vizualizacija v BaseClass/OsnovniPodatki.ipynb
 * Vrednosti sem naložil v vgnezdeni dict, kjer je ID animeja primarni ključ, in ime žanra sekundarni, ki kaže na boolean vrednost, ki pove ali film v primarnem ključu pripada temu žanru
 * Žanre sem nato preštel, tako da je vsak žanr v filmu inkrementiral števec za svojo kategorijo. Številke so izpisane v OsnovniPodatki.ipynb
 * Žanre sem nato noramliziral, s tem da sem prej dobljeni imenik delil z številom unikatnih filmov
 ** Komedija je najpogosteje se ponaljajoči žanr, z čez 35%
 * Nazadnje sem še seštel vse dobljene normalizirane številke, da dobim povprečno število žanrov na anime
 ** Informacija ni bila uporabljena, ampak je bila zanimiva
## Porazdelitev vrednosti
Večina podatkov je v BaseClass/Porazdelitve.ipynb, z izjemo beta porazdelitve, ki je v BaseClass/Napovednik.ipynb
 * Zaradi naslednjih točk sem se odločil uporabiti beta porazdelitev:
 ** Vrednosti lahko zasedejo vnaprej določen končni interval od 1 do 10
 ** Zaradi necentriranosti pri mediani in neuravnovešene porazdelitve se ne da uporabiti Gaussove krivulje
 * Ko sem po parih vrednostih dobil da je najboljše prileganje pri a=8 in b=2 (pri n=10000)
 ** Poskusil sem najti boljšo rešitev z vpeljavo makismumov in minimumov, ampak se je a=8 in b=2 bolje prilegalo
 *** Razlog mi ni povsem jasen
# Napovednik
Koda in vizualizacije so v BaseClass/Napovednik.ipynb
 * Vse prej izpeljane baze sem vpeljal, ampak uspelo mi je uporabiti le surov rating na uporaben način
 ** Nujno je potrebno od straniti neocenjene ratinge, sicer se MSE povsem pokvari zaradi -1 vrednosti omenjenih ratingov
## Učna in testna množica
 * Razdelil 3 tipe, da vidim ali je bolje z manj ali z več podatki:
 ** Vse je bilo shranjeno v dict, kjer so črke predstavljale (relativno) velikost učne množice
 *** S: small
 *** M: medium
 *** L: large
 
## Kontrolni razred
 * Pripis povprečne ocene vseh animejev vsem animejem
 * Dobljeni povprečni ratingi so se razlikovali za >0.05, tako da nisem se trudil vpeljati v nadaljnje teste
### Statistike
 * Povprečni rating so bili:
 ** 7.83203125
 ** 7.87683576985
 ** 7.86392013127
 * MSE:
 ** 2.29892939184
 ** 2.31259267875
 ** 2.3503440939
## Gaussian Naive Bayes
 * Model nisem bil prepričan, če je najboljši, zaradi prej omenjene negaussove distribucije
 * Rezultati so pa vendarle bili presumljivo dobri, ampak nisem našel napake
### Statistika
 * MSE - samo pri "S" množici je bil neničelen, kar mi je tudi vrglo dvom na to, da je nek hud hrošč v programu
 ** 0.00466067596567
 ** 0.0
 ** 0.0
## Beta fitting
 * Lepo prileganje pri a=8 in b=2
 ** a in b sem izbral glede na to, kje je lokalni maksimum (pri 8/10)
 ** Vsi poskusi izboljšati so se izkazali za manj natančne
