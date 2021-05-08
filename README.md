# Parking

### Sovelluksen idea
Sovelluksessa näkyy vapaasti käyttäjien lisättyjä parkkipaikkoja ja niihin liittyvää tietoa. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
2. Käyttäjä voi lisätä ja poistaa parkkipaikkoja.
3. Käyttäjä voi varata parkkipaikan käyttöönsä.
4. Käyttäjä voi lisätä kuvan parkkipaikasta.
5. Käyttäjä voi arvioida parkkipaikkoja.
6. Käyttäjä voi hakea parkkipaikkoja sijainnilla (annetaan sanallisesti lisätessä).
7. Ylläpitäjällä on hallinta kaikkiin parkkipaikkoihin (voi poistaa).
8. Ylläpitäjä voi poistaa käyttäjän.
9. Käyttäjä voi muokata parkkipaikkaan liittyviä tietoja.
10. Ylläpitäjä voi muuttaa onko parkkipaikka jollakin käytössä.

### Sovelluksen tilanne

[Herokun linkki](https://tsoha-parking.herokuapp.com/)

- [x] Käyttäjä pystyy luomaan käyttäjätunnuksen ja kirjautumaan sisään.
- [x] Käyttäjä voi lisätä parkkipaikan ja poistaa oman parkkipaikan
- [x] Käyttäjä voi varata parkkipaikan käyttöön ja lopettaa käytön
- [x] Käyttäjä voi kommentoida parkkipaikkaa
- [x] Käyttäjä voi antaa tähtiä parkkipaikalle
- [x] Käyttäjä voi hakea parkkipaikkoja sijainnilla
- [x] Ylläpitäjän toiminnot
- [ ] Ulkoasun toteutus
- [ ] Tietoturva
- [ ] Koodin oikoluku ja siistiminen
- [ ] Heroku


### Ohjeet

- Luo virtuaaliympäristö

  `python3 -m venv venv`
  
- Käynnistä virtuaaliympäristö

  `source venv/bin/activate`
  
- Asenna kaikki tarvittavat riippuvuudet

  `pip install -r requirements.txt`
  
-  Luo tarvittavat taulut tietokantaan

   `psql < schema.sql`

- Käynnistä sovellus

  `flask run`
