-- https://github.com/robotautas/kursas/blob/master/DB/db4/uzduotis.md
-- 1. Sukurkite duomenų bazę pagal tokią diagramą: (uzduotis.png)
-- 2. Užpildykite duomenimis - bent 3 klientai, bent 5 užsakymai, kiekviename jų po 1-3 pozicijas, keletas produktų, keletas užsakymo statusų (pvz, patvirtintas, vykdomas, įvykdytas, atmestas).
-- 3. suformuokite keletą užklausų: 
    -- 3.1 Kad rezultate matytųsi užsakymo id, pozicijos su kiekiais, kainomis ir bendra pozicijos suma: (query2.png)
    -- 3.2 Kad rezultate matytųsi užsakymo id, užsakovo pavardė, data, bendra užsakymo suma: (query1_real.png)
    -- 3.3 Pirmos užklausos pagrindu sukurkite užklausą, kurioje matytųsi, kiek ir kokio produkto buvo užsakyta: (query3.png)

DROP TABLE customer;
DROP TABLE order_;
CREATE TABLE customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE order_ (
    id INTEGER PRIMARY KEY,
	customer_id INTEGER NOT NULL,
    date_ TEXT(50) NOT NULL,
    status_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (id) REFERENCES product_order (order_id),
    FOREIGN KEY (status_id) REFERENCES status (id)
);

CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES order_ (status_id),
);