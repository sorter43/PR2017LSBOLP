# PR2017LSBOLP

Seminarska naloga za predmet Podatkovno rudarjenje na Fakuteti za računalništvo in informatiko
Maj 2017

## Avtorji

 * Leo Andrej Štimac
 * Blaž Ocepek
 * Lara Pirjevec

## Naloga

Za nalogo smo izbrali Kaggle izziv, da le iz uporabniških ratingov napoveš kakšno oceno bi uporabnik dal animeju. Torej za uporabnika ne smemo pričakovati ničesar drugega kot njegove ratinge.  
Za nalogo nameravamo napovedati, ali bo uporabniku všeč anime, ki ga še ni pogledal. Odvisno od povprečne uporabniške ocene smo si zastavili cilj da napovemo oceno uporabnika, po možnosti z največjo absolutno napako 1.  

## Podatki

Pri izzivu sta bili dani 2 podatkovni zbirki:
 * anime.csv - bazi z podatki o animejih samih
  *  anime_id - unikatni identifikator animeja; numeric
  *  name - ime animeja; string
  *  genre - vsi žanri, katerim je anime pripisan; string: posamezni žanri ločeni z ","
  *  type - vrsta medija; string [Movie, Music, ONA, OVA, Special, TV]
  *  episodes - število epizod; numeric
  *  rating - poveprečni rating; numeric
  *  members - število ljudi, ki je anime ocenilo; numeric
 * ratings.csv - baza ocen uporabnikov za posamezne pare uporabnik-anime
  *  user_id - unikatni identifikator za uporabnika (in edini način za razlikovanje med uporabniki); numeric
  *  anime_id - unikatni identifikator animeja; numeric
  *  rating - ocena, ki jo je uporabnik dal animeju; numeric

## Kriterij

Želimo dobiti boljši algoritem od pripisovanja povprečne ocene, ki je najbolj preprost algoritem, ki še daje sprejemljive rezultate.

## Začetna opažanja

 * Rating in število memberjev sta sorazmerno povezana.
 * Vrsta medija ima velik vpliv na konsitentnost in velikost ratingov
  *  TV ima najboljše ocene
  *  Movies ima najbolj neenotne ocene

## Razlike od baze pri domači nalogi (movies)

 * Nimamo na voljo časovne oznake, kdaj so uporabniki ocenili anime
 * Manj podatkov:
  *  ni igralcev
  *  ni producentov
  *  ni studia
 * Demografika je predvidoma drugačna kot pri MovieLens, tako da se lahko pričakuje drugačne ugotovitve pri uporabi istih metod
 
## Cilji

 * Boljša varianca od pripisovanja povprečne ocene
 * Preverjanje, če vpeljava novih zunanjih baz/spremenljivk izboljša ali poslabša rezultat
  *  Baza podatkov animejev skozi čas
  *  Vpliv studija na oceno
  
