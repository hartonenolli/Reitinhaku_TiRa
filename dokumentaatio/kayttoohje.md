# Käyttöohje

# Pikaisesti:

## Pelin asennus:
- poetry install

## Käynnistys
- poetry run invoke start

### Ohjeet:
- Sinulle avautuu ruutu, jossa voit asettaa 4 eri koordinaattia
  - Sinun ei ole pakko asettaa koordinaatteja. Tällöin sinulle asetetaan alkuruuduksi (*sininen*) vasen-ylä ruutu ja loppuruuduksi (*punainen*) oikea-ala ruutu
  - Jos valitset koordinaatiksi ruudun, jossa on seinä, niin se näytetään *harmaalla*
- Painamalla kartta painikkeita paaset katsomaan eri karttoja
  - Näitä on 3 eri kokoista: 10x10, 15x15 ja 20x20
  - Indeksoinnit alkaa 0, eli 10x10 kartalla voit valita koordinaatit 0-9 väliltä
- Painamalla algoritmipainikkeita aloitetaan reitin etsintä
  - Reitti näytetään *keltaisella* ja tarkastetut ruudut *vihreällä*
- Ohjelma näyttää visuaalisesti lyhimmän reitin, mikä sen pituus on ja kuinka nopeasti se löydettiin
  - Reitin pituus ja aika sen löytämiselle tulostetaan **Terminaalissa**
- Ohjelmasta voi poistua painamalla ruksia oikeassa yläkulmassa
