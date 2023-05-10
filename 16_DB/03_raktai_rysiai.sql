-- 1. Išrinkite visus duomenis iš lentelės “DARBUOTOJAI”.
-- DELETE FROM DARBUOTOJAI;
-- 2. Išrinkite visus duomenis iš stulpelio “GIMIMO_DATA” - lentelėje “DARBUOTOJAI”.
-- ALTER TABLE DARBUOTOJAI
-- DROP COLUMN GIMIMO_DATA;????????
-- 3. Išrinkite visus duomenis iš stulpelių “VARDAS”,”PAVARDĖ”, “PAREIGOS” - lentelėje “DARBUOTOJAI”.
-- 4. Išrinkite unikalias reikšmes iš stulpelio SKYRIUS_PAVADINIMAS - lentelėje “DARBUOTOJAI”.
-- 5. Išrinkite visus duomenis apie darbuotojus, kurie dirba Gamybos skyriuje.
-- 6. Išrinkite duomenis, kokias pareigas užima Giedrius
-- 7. Išrinkite visus duomenis apie darbuotojus, kurių gimimo data - 1986-09-19
-- 8. Išrinkite darbuotojų vardus, kurių pavardės yra Sabutis
-- 9. Išrinkite duomenis (vardą ir pavardę) apie programuotojus iš Gamybos skyriaus


-- 10. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami visus reikiamus laukus (vardą, pavardę, gimimo metus, pareigas, skyriaus pavadinimą).
-- INSERT INTO DARBUOTOJAI (
-- 	VARDAS,
-- 	PAVARDĖ,
--     GIMIMO_DATA,
--     PAREIGOS,
--     SKYRIUS_PAVADINIMAS
--     )
-- VALUES ('duxas', 'duhelis', '1998', 'programeris', 'IT');

-- 11. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami tik laukus (vardą, pavardę, gimimo metus). Pareigas ir skyriaus pavadinimą palikite neužpildytus.
-- INSERT INTO DARBUOTOJAI (
-- 	VARDAS,
-- 	PAVARDĖ,
    -- GIMIMO_DATA
--     )
-- VALUES ('Petras', 'Petraitis', '1991');

-- 12. Užpildykite likusius tuščius laukus “DARBUOTOJAI” lentelėje, jūsų prieš tai įterptame įraše. Priskirkite darbuotojui pareigas ir skyrių.
-- UPDATE DARBUOTOJAI
-- SET PAREIGOS = "Vairuotojas", SKYRIUS_PAVADINIMAS = "Gamybos"
-- WHERE PAREIGOS IS NULL;

-- 13. Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte.
-- DELETE FROM DARBUOTOJAI WHERE GIMIMO_DATA = "1998";

-- 14. Įterpkite, du darbuotojus, pavarde Antanaitis kurių pareigos būtų “Programuotojas”.
-- INSERT INTO DARBUOTOJAI (
-- 	VARDAS,
-- 	PAVARDĖ,
--     GIMIMO_DATA,
--     PAREIGOS
--     )
-- VALUES ('Petras', 'Antanaitis', '1991', 'Programuotojas'),
--     ('Antanas', 'Antanaitis', '1991', 'Programuotojas');

-- 15. Pakeiskite, abiejų Antanaičių pareigas į “Testuotojas” vienu sakiniu.
-- UPDATE DARBUOTOJAI
-- SET PAREIGOS = "Testuotojas"
-- WHERE PAREIGOS = 'Programuotojas';

-- 16. Suskaičiuokite, kiek įmonėje dirba Testuotojų.
-- SELECT COUNT() FROM DARBUOTOJAI WHERE PAREIGOS = 'Testuotojas';