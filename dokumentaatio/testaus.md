# Testaus

## Testaustilanne

![coveragekuva](https://github.com/hartonenolli/Reitinhaku_TiRa/blob/master/dokumentaatio/kuvat/coverage_kuva.png)

# Testaus toteutus

Automaattisia testejä tehty algoritmeihin. Kekorakenne testaantuu dijkstran algoritmin testejen avulla. On pyritty saamaan poikkeavia syötteitä testeille.

Lisätty github action, jolla varmistettu testien toimivuus jokaisen pushauksen jälkeen.

kayttoliittyma.py, karttaruutu.py ja karttoja ei ole testattu automaattisesti. Käyttöliittymän ja karttaruudun automaattinen testaus ei onnistu, mutta manuaalista testausta on suoritettu. Manuaalisissa testeissä on pyritty mm. laittamaan mahdollisimman kummallisia syötteita, painelemaan nappuloita useasti
