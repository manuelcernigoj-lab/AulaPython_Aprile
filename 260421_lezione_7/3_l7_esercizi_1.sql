--  CLIENTS TABLE
SELECT *
FROM gestioneordini.clienti;
-- ORDERS TABLE
SELECT *
FROM gestioneordini.ordini;

/*
1. INNER JOIN:
   Visualizza l’elenco dei clienti che hanno effettuato almeno un ordine.
   Per ciascuno, mostra: nome del cliente, data dell’ordine e importo
*/
SELECT 
	c.nome							AS Cliente,
    o.data_ordine					AS DataOrdine,
    o.importo						AS Importo
FROM gestioneordini.clienti			AS c
INNER JOIN gestioneordini.ordini	AS o
ON c.id = o.id_cliente;

/*
2. LEFT JOIN:
   Visualizza tutti i clienti, inclusi quelli che non hanno mai effettuato ordini.
   Mostra per ciascuno: nome del cliente, data dell’ordine (se presente) e importo (se presente).
*/
SELECT 
	c.nome							AS Cliente,
    o.data_ordine					AS DataOrdine,
    o.importo						AS Importo
FROM gestioneordini.clienti			AS c
LEFT JOIN gestioneordini.ordini		AS o
ON c.id = o.id_cliente;

/*
3. RIGHT JOIN:
   Visualizza tutti gli ordini, anche quelli che non hanno un cliente associato (caso anomalo).
   Mostra per ciascuno: nome del cliente (se esiste), data dell’ordine e importo.
*/
SELECT
	c.nome							AS Cliente,
    o.data_ordine					AS DataOrdine,
    o.importo						AS Importo
FROM gestioneordini.clienti			AS c
RIGHT JOIN gestioneordini.ordini	AS o
ON c.id = o.id_cliente;

