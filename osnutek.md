# **Opis seminarske naloge iz Podatkovnega rudarjenja**

## **Člani:**  
    63120115 | ls6358   | Leo Andrej Štimac  
    63140179 | bo2710   | Blaž Ocepek  
    63140196 | lp0599   | Lara Pirjevec  

## *Problem:*
 * Anime napoved za uporabnika - Kolikšna je možnost da bo uporabnik X dal animeju Y oceno nad 5/6/7/8?

## *Pod-problemi:*  
 * Ocenjevanje uspešnosti posameznega animeja: ratings + members + epizode  
 * Rangiranje animejev: porazdeljeno v podskupine (movie, TV, OVA, etc.) glede na uspešnost in žanro  
 * Povezovanje žanrov: kakšni žanri so si podobni, kakšne so ocene animejev z mešanimi žanri?  
 * Povezovanje animejev: katere anime so si najbolj podobne  
 * Povezovanje uporabnikov: kako podobni so si uporabniki, katere žanre so najbolj ocenjene, kater anime so skupne  
 * Povezovanje ocen: kaj imajo skupnega najslabše ocenjeni animeji, kaj najboljše ocenjeni  
 * Kako količina neocenjenih ratingov vpliva na povprečni rating animeja?

## *Bonus pod-problemi (ni zagotovljeno, da bo prišlo do implementacije):*
 * Dodajanje studia k posameznim animejih  
  * primerjava studijev  
  * možnost, da bo nov anime od tega studia uspešnica  
 * Dodajanje sočasnih statistik o priljubljenosti epizod  
  * primerjava popularnosti animejev skozi čas (obdelovanje podatkov z: http://graphtv.kevinformatics.com/)


## **Opis podatkovne baze:**

Pridobljeno z https://www.kaggle.com/CooperUnion/anime-recommendations-database

To so osnovni podatki, možna vpeljava dodatnih baz ali spremenljivk za izboljšanje natančnosti

### *Anime.csv:*  
anime_id - myanimelist.net's unique id identifying an anime  
name - full name of anime  
genre - comma separated list of genres for this anime  
type - movie, TV, OVA, etc.  
episodes - how many episodes in this show. (1 if movie)  
rating - average rating out of 10 for this anime  
members - number of community members that are in this anime's "group"

### *Rating.csv:*  
user_id - non identifiable randomly generated user id  
anime_id - the anime that this user has rated  
rating - rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating)
