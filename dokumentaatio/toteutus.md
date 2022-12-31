# Toteutus

## Ohjelman yleisrakenne
- Ohjelma käynnitetään *kayttoliittyma.py* tiedoston avulla. Tiodostosta löytyy luokka *UserInterFace*, jolla kutsutaan *karttaruutu.py* tiedoston luokkaa *KarttaRuutu*.
- *Karttaruutu* alustaa näkymän ruudulle. Aluksi avautuu näkymä 5 painikkeella ja 4 syöttökentällä. Syöttökentälle voi asettaa arvoja, tai olla asettamatta.
   - Ohjelma asettaa itse puuttuvat arvot tai väärät arvot oletuskohtiin
- Karttaruutu kutsuu *algoritmit* kansiossa olevia algoritmeja. Myös *kartat* kansiosta haetaan käytettävät kartat sovellukselle.

# Ohjelman rakenne:

      .
      ├── dokumentaatio
      ├── README.md
      ├── src
      │   ├── algoritmit
      │   │   ├── dijkstra.py
      │   │   └── ida_star.py
      │   ├── kartat
      │   │   └── kartta1.py
      │   ├── karttaruutu.py
      │   ├── kayttoliittyma.py
      │   ├── kekokansio
      │   │   └── keko.py
      │   └── tests
      │       ├── dijkstra_test.py
      │       ├── ida_test.py
      │       └── test_assets
      │           └── d_assets.py
      └── tasks.py

## Saavutetut aika- ja tilavaativuudet
Dijkstran algoritmin saavutetut aikavaativuudet:
- Algoritmi käy läpi ruudut ja niiden naapurit, eli solmut. Tämä tapahtuu ajassa O(n+m), jossa n on ruutujen määrä ja m solmujen
- Keosta saamme pienimmän alkion pois ajassa O(1). Poistamisen jälkeinen järjestäminen ja lisääminen vie aikaa O(log n)
- Näistä saamme kokonaisaikavaativuudeksi O(n+m log n)

Dijkstran algoritmin tilavaativuus on O(n+m). Algoritmi ylläpitää muistissa ruutuja, jotka lisätään listaan. Pahimmassa tapauksessa kaikki ruudut joudutaan lisäämään muistiin.

IDA-* algoritmin saavutetut aikavaativuudet:
- Aikavaativuus on riippuvainen asia ruutujen naapureiden määrästä, esteistä reitillä ja heurestisen arvon laskemisesta. Aikavaativuutta on yleiseti pidetty olevan O(b^d), jossa b on haarautuvuuden määrä (kuinka monta naapuria ruudulla on) ja d on ensimmäisen löytyneen polun pituus.
- Heurestinen arvon laskutapa aiheuttaa IDA-* algoritmille vaikeuksia oikealta vasemmalle liikkumisessa. Esimerkkinä tästä reitti, jonka pituus on 45 ruutua kartta3, jossa on koordinaatit alulle 0,6 ja lopulle 14,17 löytyy ajassa 3,45s. Jos koordinaatit laittaa alulle ja lopulle toisin päin, niin reitti löytyy ajassa 46,42s.

IDA-* algoritmin tilavaativuus on O(d), jossa d on lyhyimmän polun etäisyys alkuruudusta loppuruutuun.

# Suorituskykyvertailut

Suorituskykyvertailussa on tarkasteltu seuraavia algoritmeja:
- Dijkstran (itse rakennetulla kekorakenteella)
- IDA-*
- Dijkstran (pythonin omalla 'heapq' kekorakenteella)

Suorituskykyä on mitattu sekunneissa *4 desimaalin* tarkkuudella. Aika alkaa, kun kutsutaan algoritmiluokkia ja päättyy, kun kaikki toimenpiteet on saatu valmiiksi luokissa.

Kerätty taulukko, jossa on valittu 4 eri reittiä jokaisesta kartasta. Otettu **20 hakukerran keskiarvo** siitä, kuinka kauan algoritmilla kestänyt löytää reitti.

# Kartta1
Kartta1 on 10x10 kertaa ruudukko. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0    9,9    | 18            | 0,0018s            | 0,0013s            | 0,0015s            |
| 0,9    9,0    | 18            | 0,0017s            | 0,0015s            | 0,0014s            |
| 0,4    9,4    | 11            | 0,0017s            | 0,0013s            | 0,0014s            |
| 4,0    4,9    | 15            | 0,0017s            | 0,0015s            | 0,0016s            |

# Kartta2
Kartta2 on 15x15 kertaa ruudukko. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0   14,14   | 24            | 0,0028s            | 0,0019s            | 0,0026s            |
| 0,14  14,0    | 40            | 0,0029s            | 0,0090s            | 0,0024s            |
| 0,6   14,6    | 20            | 0,0029s            | 0,0021s            | 0,0025s            |
| 7,0    6,14   | 25            | 0,0028s            | 0,0028s            | 0,0026s            |

# Kartta3
Kartta3 on 20x20 kertaa ruudukko. Kaksi viimeistä riviä näyttää IDA-* algoritmin vaikeudet isoissa reiteissä ja vasemmalta oikealle mentävissä hauissa. Tähän vaikuttaa myös esteiden sijoittelu. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0   19,19   | 40            | 0,0057s            | 0,0992s            | 0,0053s            |
| 0,19  19,0    | 42            | 0,0055s            | 0,1008s            | 0,0052s            |
| 0,9   19,9    | 27            | 0,0058s            | 0,0042s            | 0,0055s            |
| 9,0    9,19   | 39            | 0,0056s            | 0,3512s            | 0,0053s            |
| 0,6   14,17   | 45            | 0,0059s            | 3,4609s            | 0,0055s            |
| 14,17  0,6    | 45            | 0,0059s            | 46,3356s           | 0,0057s            |

## Johtopäätökset testeistä

IDA-* algoritmi toimii tehokkaasti tai tehokkaammin, kuin Dijkstran algoritmi, kun reitin pituus on noin 25 ruutua. Tähän vaikuttaa paljon myös kartan esteiden sijoittelu. Kartta 1 ja 2 IDA-* toimii oikein tehokkaasti poislukien vasemmasta alakulmasta oikeaan yläkulmaan etsitty reitti. Tähän on vaikuttanut reitin pituus ja kastan esteiden sijoittelu. Jouduin muokkaamaan erityiseti kartta3 paljon, jotta sain IDA-* algoritmia mitattua kunnolla. Reitin pituuden ollessa lähemmäs 50 ruutua oli IDA-* algorimi niin hidas, ettei sitä jaksanut jäädä odottelemaan. Erityinen huomio kartta3 etsityt reitit taulukon kahdella viimeisellä rivillä. Alla kuva kartasta:

![Kartta3](https://github.com/hartonenolli/Reitinhaku_TiRa/blob/master/dokumentaatio/kuvat/kartta3_kuva.png)

Reitin hakuun sinisestä ruudusta punaiseen meni IDA-* algoritmilla 46s. Toisin päin hakuun menee vain 3,4s. Tämä johtuu pääsääntöisesti esteiden sijoittelusta kartalla. Kuvassa näkyy pitkä seinä maalin vieressä. Luulen tämän aiheuttavan niin suuren eron reitin haun tehokkuudessa.

Taulukoista näkee IDA-* algoritmin olevan hitaampi, kun reitin pituus on noin 40-ruuta.

Pythonin oma kekorakenne on noin 15-20% nopeampi löytämään reitin, kuin oma tekemä kekorakenne. Tämä johtunee siitä, että kekorakenne on optimoitu hyvin tarkkaan.

# Puutteet ja parannusehdotukset
- Käyttöliittymää voisi tehdä paremmaksi. Se on nyt ihan toimiva, mutta tällä hetkellä reitin löytymiseen liittyvät tiedot (pituus ja aika) tulostetaan terminaalissa. Ihan toimiva tapa, mutta kaikki tieto käyttöliittymässä olisi tietydti mieluisampaa..
- Ohjelmassa on oletusarvona, että reitti on aina olemassa
- Koska valitsin että reitinhaku tapahtuisi "kaupunkimaisessa" ympäristössä, niin lyhin reitti on löydetty kulkemalla vain vaaka- ja pystysuunnassa. Tätä voisi toki kehittää, että reitillä voisi kulkea myös vinottain.

# Lähteet
[Tirakirja](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)

[Dijkstran algoritmi](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[Dijkstran algoritmi 2](https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html)

[IDA-* algoritmi](https://en.wikipedia.org/wiki/Iterative_deepening_A*)

[IDA-* algoritmi 2](https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/)

[IDA-* aikavaativuus](https://stackoverflow.com/questions/54490981/artificial-intelligence-time-complexity-of-ida-search)
