# Testaus

## Testaustilanne

![coveragekuva](https://github.com/hartonenolli/Reitinhaku_TiRa/blob/master/dokumentaatio/kuvat/coverage_kuva.png)

# Testaus toteutus
Algoritmeille ja kekorakenteelle on tehty automaattisia testejä, jolla varmistettu ohjelman jatkuva toiminta. Lisätty myös github actions, jolla varmistettu testien läpimeno jokaisen uuden pushauksen aikaka.

Automaattiisissa testeissä Algoritmeille on annettu mahdollisimman erilaisia syötteitä. Annoin syötteinä karttoja, naapureita ja ruutuja, joissa oli pyritty saamaan erilaisia tilanteita aikaan. Näitä on ollut esim: kartat, joilla on kaikki naapurit tai ei yhtään naapuria.

Kekorakenteen automatisoitu testaus on varmistanut lisäyksen, poiston ja keon järjestämisen jatkuvan toiminnan. Näissä myös on pyritty antamaan syötteitä jotka poikkeavat toisistaan paljon. Kekorakenne testaantuu myös paljon jo pelkästään dijkstran testien avulla, koska dijkstran algoritmi kutsuu kekorakennetta. Kekoluokka tarvitsi silti omat testinsä, jotta laaja testikattavuus saavutettaisiin.

Käyttöliittymää ja karttaruutua ei ole automaattisin testein testattu. Niihin on suoritettu manuaalista testausta. manuaalisissa testeissä on varmistettu, että eri painikkeet toimivat halutulla tavalla, koordinaatit asettuu ruudulle niin kuin on tarkoitus, virheellisissä syötteissa annetaan oikeanlainen ilmoitus käyttäjälle, reitin tulostus tapahtuu oikein yms.

Testatessa on pyritty tekemään myös poikkeuksellisia asioita, mitä normaalisti käyttäjän ei tarvitsisi tehdä. Näihin on kuulunut painikkeiden rämpytys, kummallisten syötteiden antaminen, päällekkäisten tai virheellisten ruutujen valinta yms.

## Testien hyödyt
Automaattiset testit antoivat varmuuden ohjelman perustoiminnon jatkuvasta toiminnasta.

Manuaalisesta testauksesta oli usein hyötyä. Sen ansiosta löysin ohjelmasta bugin, jossa dijkstran algoritmi ei löytänytkään lyhintä reittiä etsiessä oikealta vasemmalle. Sain selvitettyä vian olevan kekorakenteessa uuden alkion lisäyksessä.

