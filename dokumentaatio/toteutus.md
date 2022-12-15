# Toteutus

## Ohjelman yleisrakenne
- Ohjelma käynnitetään *kayttoliittyma.py* tiedoston avulla. Tiodostosta löytyy luokka *UserInterFace*, jolla kutsutaan *karttaruutu.py* tiedoston luokkaa *KarttaRuutu*.
- *Karttaruutu* alustaa näkymän ruudulle. Aluksi avautuu näkymä 5 painikkeella ja 4 syöttökentällä. Syöttökentälle voi asettaa arvoja, tai olla asettamatta.
   - Ohjelma asettaa itse puuttuvat arvot tai väärät arvot oletuskohtiin
- Karttaruutu kutsuu *algoritmit* kansiossa olevia algoritmeja. Myös *kartat* kansiosta haetaan käytettävät kartat sovellukselle.

Tänne joku rakennekaavio

## Saavutetut aikavaativuudet
Dijkstran algoritmin saavutetut aikavaativuudet:
- Algoritmi käy läpi ruudut ja niiden naapurit, eli solmut. Tämä tapahtuu ajassa O(n+m), jossa n on ruutujen määrä ja m solmujen
- Keosta saamme pienimmän alkion pois ajassa O(1). Poistaminen ja lisääminen vie aikaa O(log n)
- Näistä saamme kokonaisaikavaativuudeksi O(n+m log n)

IDA-* algoritmin saavutetut aikavaativuudet:
- Jotain
- muuta
- emt

# Suorituskykyvertailut

Suorituskykyvertailussa on tarkasteltu seuraavia algoritmeja:
- Dijkstran (itse rakennetulla kekorakenteella)
- IDA-*
- Dijkstran (pythonin omalla 'heapq' kekorakenteella)

Suorituskykyä on mitattu sekunneissa *4 desimaalin* tarkkuudella. Aika alkaa, kun kutsutaan algoritmiluokkia ja päättyy, kun kaikki toimenpiteet on saatu valmiiksi luokissa.

Kerätty taulukko, jossa on valittu 4 eri reittiä jokaisesta kartasta. Otettu **5 hakukerran keskiarvo** siitä, kuinka kauan algoritmilla kestänyt löytää reitti.

# Kartta1
Kartta1 on 10x10 kertaa ruudukko. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0    9,9    | 18            | 0,0017s            | 0,0013s            | 0,0015s            |
| 0,9    9,0    | 18            | 0,0017s            | 0,0015s            | 0,0015s            |
| 0,4    9,4    | 11            | 0,0017s            | 0,0012s            | 0,0014s            |
| 4,0    4,9    | 15            | 0,0016s            | 0,0015s            | 0,0016s            |

# Kartta2
Kartta2 on 15x15 kertaa ruudukko. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0   14,14   | 24            | 0,0028s            | 0,0019s            | 0,0026s            |
| 0,14  14,0    | 40            | 0,0027s            | 0,0090s            | 0,0025s            |
| 0,6   14,6    | 20            | 0,0029s            | 0,0021s            | 0,0026s            |
| 7,0    6,14   | 25            | 0,0028s            | 0,0028s            | 0,0026s            |

# Kartta3
Kartta3 on 20x20 kertaa ruudukko. Taulukossa tulokset:
| KOORDINAATIT  | REITIN PITUUS | DIJKSTRA (oma keko)| IDA-*              | DIJKSTRA (python)  |
| ------------- |:-------------:| :-----------------:| :-----------------:| :-----------------:|
| 0,0   19,19   | 40            | 0,0055s            | 0,0992s            | 0,0055s            |
| 0,19  19,0    | 42            | 0,0053s            | 0,1008s            | 0,0053s            |
| 0,9   19,9    | 27            | 0,0058s            | 0,0042s            | 0,0056s            |
| 9,0    9,19   | 39            | 0,0056s            | 0,3512s            | 0,0053s            |

## Huomioita taulukosta

IDA-* algoritmi toimii tehokkaasti tai tehokkaammin, kuin Dijkstran algoritmi, kun reitin pituus on noin 25 ruutua. Tähän vaikuttaa paljon myös kartan esteiden sijoittelu. Jouduin muokkaamaan erityiseti kartta3 paljon, jotta sain IDA-* algoritmia mitattua kunnolla. Reitin pituuden ollessa lähemmäs 50 ruutua oli IDA-* algorimi niin hidas, ettei sitä jaksanut jäädä odottelemaan.

Kuitenkin huomataan taulukoista reitit, jossa pituus on noin 40-ruuta on IDA-* algoritmi huomattavasti hitaampi.

Pythonin oma kekorakenne on keskimäärin 2 sekunnin tuhannesosaa nopeampi löytämään reitin, kuin oma tekemä kekorakenne. Tämä johtunee siitä, että kekorakenne on optimoitu hyvin tarkkaan.

# Puutteet ja parannusehdotukset
- Miten voisi hioa

# Lähteet
Tirakirja, wikipediat, IDA-* omat sivut
