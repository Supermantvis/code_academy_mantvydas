-- INSERT INTO studentai (first_name, last_name, email);
-- VALUES ('Jonas', 'Jonaitis', 'mr_slick@gmail.com');
-- INSERT INTO studentai (first_name, last_name, email)
-- VALUES ('Geras', 'Gerulis', 'gerasbx@ruski.ru.notcom');
-- INSERT INTO studentai (first_name, last_name, email)
-- VALUES ('Belekoks', 'Belenkauskas', 'ciuvas@ktu.live.co.uk');
-- INSERT INTO studentai (first_name, last_name, email)
-- VALUES ('Ledine', 'Gerule', 'sexiukexx69@one.lt');

-- SELECT * FROM studentai WHERE id > 1;
-- SELECT * FROM studentai WHERE first_name = "Jonas";
-- SELECT * FROM studentai WHERE address IS NULL;
-- SELECT * FROM studentai WHERE NOT address IS NULL;

-- DELETE FROM studentai WHERE id > 1;
-- DELETE FROM studentai;


-- ********** UZDUOTYS **********
-- 1 UZDUOTIS: Sukurkite lentelę "mokytojai" su šiais stulpeliais: "id", "vardas", "pavarde", "specialybe" ir "patirtis_metais".
-- DROP TABLE mokytojai;
-- CREATE TABLE mokytojai (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     vardas VARCHAR(50) NOT NULL,
--     pavarde VARCHAR(50) NOT NULL,
--     specialybe VARCHAR(100),
--     patirtis_metais SMALLINT
-- );


-- 2 UZDUOTIS: Įterpkite šiuos įrašus į sukurtą lentelę "mokytojai":
-- INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_metais)
-- VALUES ('Petras', 'Petraitis', 'Matematika', 2013),
--        ('Ona', 'Onaitė', 'Fizika', 2012),
--        ('Marius', 'Marijus', 'Biologija', 2015),
--        ('Rasa', 'Rasaitė', 'Anglų kalba', 2011),
--        ('Aurimas', 'Aurimaitis', 'Lietuvių kalba', 2018),
--        ('Gintare', 'Gintarėlė', 'Istorija', 2020);


-- 3 UZDUOTIS: Parodykite visus įrašus iš lentelės "mokytojai", kurių specialybė yra "Matematika".
-- SELECT * FROM mokytojai WHERE specialybe = "Matematika";


-- 4 UZDUOTIS: Raskite visus mokytojus, kurių stažas yra ilgesnis nei 8 arba 9 metai, ir atvaizduokite tik jų vardą, pavardę bei specialybę.
-- SELECT vardas, pavarde, specialybe FROM mokytojai
-- WHERE (2023 - patirtis_metais) > 8 OR (2023 - patirtis_metais) > 9;


-- 5 UZDUOTIS: Pakeiskite mokytojos, vardu Rasa ir pavarde Rasaitė, pavardę į "Žolienė".
-- UPDATE mokytojai
-- SET pavarde = 'Žolienė'
-- WHERE vardas = 'Rasa' AND pavarde = 'Rasaitė';


-- 6 UZDUOTIS: Ištrinkite iš lentelės "mokytojai" mokytoją, kurio ID yra 4.
-- DELETE FROM mokytojai WHERE id = 4;