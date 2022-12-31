# Määrittely

## Olen käyttänyt dokumentaatioon ja ohjelmointiin suomen kieltä

Ohjelmani on kahden eri algoritmin vertailu. Algoritmit etsivät lyhyimmät reitit eri kartoilta. Olen valinnut ohjelmani etsivän lyhyimmät reitit liikkumalla "kaupunkimaisessa" ympäristössä, eli reitti voi kulkea vain vaaka- tai pystysuunnassa. Valitsin tähän toteutavakksi seuraavat algoritmit:

- Dijkstran algoritmi
- IDA*-algoritmi

Toteutan myös dijkstran algoritmille oman kekorakenteen. Vertailen sen tehokkuutta pythonin omaan *heapq* tarjoamaan kekoon.

Valitsin kyseiset algoritmit siksi, koska dijkstran algoritmi oli ennestään tuttu tietorakenteet ja algoritmit kurssilta. Siellä oli puhetta siitä kuinka se toimii hyvin monissa verkoissa, koska se ei tarvitse etukäteen tietoa maaliruudusta. IDA* algoritmi tarvitsee tiedon etukäteen myös maaliruudusta ja algoritmi ei vaadi tilavaativuutta samalla tavalla, kuin dijkstran algoritmi. Minua kiinnosti miten tälläinen algoritmi saadaan toteutettua ja onko se tosiaan tehokas tapa löytää lyhyin reitti kahden pisteen välillä.

En myöskään ollut ikinä toteuttanut omaa kekorakennetta. Halusin kokeilla sen toteuttamista myös.

## Ohjelman rakenne

En ollut ikinä käyttänyt *tkinteriä* missään. Sillä on mahdollissuus tehdä ikkuna, jonka avulla sovelluksen käyttäjä voi painaa nappuloita valiten eri algoritmeja käyttöönsä. Halusin tutustua tkinterin käyttöön samalla kun työstin eri algoritmeja ja kekorakennettani.

Ohjelmassa on graafinen käyttöliittymä totetettu tkinterillä. Käyttöliittymän avulla pystytään näyttämään verkkomaiset rakenteet ja reitin etsiminen kartalla.

Algoritmeille, keolle ja kartoille on omat luokkansa.

Kun reittiä halutaan etsiä kutsutaan karttaruudusta valitun algoritmin luokkaa.

Karttana toimii lista, jossa on str-muodossa kirjaimia. Kirjain kertoo mitä ruudulle halutaan piirtää.
- Eri vaihtoehtoja on: käytävä, seinä, alku, loppu, reitti, tarkastettu tai huono valinta

Algoritmien tehokkuutta verrataan suoritusajalla.
- Ajan ja reitin tulostus tapahtuu terminaalissa.

## Tavoitteeni

### Dijkstran algoritmi ja keko
Algoritmi on mahdollista toteuttaa [tirakirjan s.125](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/) mukaan aikavaativuuteen: O(n + m log n)

Tähän vaikuttaa kekorakenteen tehokkuus. Keon järjestämisen voi suorittaa ajassa: O(log n)

Tilavaativuutena pyrin: O(n + m), koska algoritmin pitää pitää yllä tietoa käydyistä ruuduista ja naapureista.

### IDA* algoritmi
Tavoitellun aikavaativuuden etsiminen oli haastavapaa IDA* algoritmille, mutta [stackoverflow sivustolta](https://stackoverflow.com/questions/54490981/artificial-intelligence-time-complexity-of-ida-search) löytämäni tiedon mukaan se olisi mahdollista toteuttaa aikavaativuuteen: O(b^d). Tässä b on haarautuvuuden määrä ja d lyhyimmän polun pituus.

Tilavaativuus on mahdollista toteuttaa: O(d), joka on lyhyimmän polun pituus.


## Opintoohjelmani:
- Tietojenkäsittelytieteen kandidaatti (TKT)

## Ohjelmointikieli:
- Python ja tätä kieltä hallitsen

## Lähteitä

[Tirakirja](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)

[Dijkstran algoritmi](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[Dijkstran algoritmi 2](https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html)

[IDA-* algoritmi](https://en.wikipedia.org/wiki/Iterative_deepening_A*)

[IDA-* algoritmi 2](https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/)

[IDA-* aikavaativuus](https://stackoverflow.com/questions/54490981/artificial-intelligence-time-complexity-of-ida-search)
