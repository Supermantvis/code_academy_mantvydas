-- 1. Išrinkite darbuotojų vardus ir pavardes kartu su projekto pavadinimu, kuriame jie dirba.
-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS
-- FROM DARBUOTOJAS
-- JOIN PROJEKTAS
-- ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID;

-- 2. Išsirinkite darbuotojų dirbančių projekte Galerija vardus, pavardes ir projekto pavadinimą.
-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS
-- FROM DARBUOTOJAS
-- JOIN PROJEKTAS
-- ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- WHERE PAVADINIMAS = 'Galerija';

-- 3. Išrinkite visus projekto Projektų valdymas vykdytojus dirbančius Pardavimų skyriuje.
-- SELECT * FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
-- WHERE PROJEKTAS.PAVADINIMAS = "Projektų valdymas"
-- AND SKYRIUS.PAVADINIMAS = "Pardavimų";

-- 4. Išrinkite visas moteris, dirbančias projekte Projektų valdymas ir išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.
-- SELECT VARDAS, PAVARDĖ, PROJEKTAS.PAVADINIMAS FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
-- WHERE PROJEKTAS.PAVADINIMAS = "Projektų valdymas"
-- AND ASMENS_KODAS LIKE "4%" OR ASMENS_KODAS LIKE "6%";

-- 5. Išrinkite skyrių pavadinimus su juose dirbančių darbuotojų skaičiumi.
-- SELECT SKYRIUS.PAVADINIMAS, COUNT() AS darbuotojų_skaicius FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
-- GROUP BY SKYRIUS.PAVADINIMAS;

-- 6. Apribokite #5 užklausos rezultatą taip, kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.
-- SELECT SKYRIUS.PAVADINIMAS, COUNT() AS darbuotojų_skaicius FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
-- GROUP BY SKYRIUS.PAVADINIMAS
-- HAVING darbuotojų_skaicius >= 5;

-- 7. Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių, kuriuose jie dirba pavadinimais, tačiau nesančius tų skyrių vadovais.
-- SELECT VARDAS, PAVARDĖ, PAREIGOS, SKYRIUS.PAVADINIMAS FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
-- WHERE PAREIGOS IS NOT "Vadovas"
-- ORDER BY SKYRIUS.PAVADINIMAS;

-- 8. Sukurkite naują įrašą lentelėje “DARBUOTOJAS” (asmens kodas: 38807117896, vardas: Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).
-- INSERT INTO DARBUOTOJAS 
-- 	(ASMENS_KODAS, VARDAS, PAVARDĖ, DIRBA_NUO)
-- VALUES
-- 	(38807117896, "Pranas", "Logis", "2009-11-12");

-- 9. Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą. Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje (skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).
-- SELECT VARDAS, PAVARDĖ, PAREIGOS, SKYRIUS.PAVADINIMAS AS skyriaus_pavadinimas FROM DARBUOTOJAS
-- LEFT JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID;

-- 10. 1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus ir projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.
-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS, COUNT()
-- FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- GROUP BY PAVADINIMAS
-- HAVING COUNT() > 4;

-- 11. Naujame stulpeyje parodyti kiekvieno darbuotojo bazinio atlyginimo ir priedų sumą.
-- SELECT VARDAS, PAVARDĖ, BAZINIS_ATLYGINIMAS + PRIEDAI AS SUMA
-- FROM DARBUOTOJAS;

-- 12. Parodyti bendrą atlyginimų, priedų sumą, vidutinį, maksimalų, minimalų atlyginimą.
-- SELECT
--     SUM(BAZINIS_ATLYGINIMAS) AS atlyginimu_suma,
--     SUM(PRIEDAI) AS priedu_suma,
--     AVG(BAZINIS_ATLYGINIMAS) AS vidutinis_atlyginimas,
--     MAX(BAZINIS_ATLYGINIMAS) AS maksimalus_atlyginimas,
--     MIN(BAZINIS_ATLYGINIMAS) AS minimalus_atlyginimas
-- FROM DARBUOTOJAS;