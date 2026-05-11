-- Scrivi le query SQL per rispondere alle seguenti richieste:
SELECT *
FROM vendite;

-- Visualizza, per ogni categoria, il numero totale di vendite effettuate.
SELECT 
	categoria, 
	COUNT(DISTINCT(id)) AS tot_vendite
FROM vendite
GROUP BY categoria
ORDER BY tot_vendite DESC;

-- Mostra, per ogni categoria, il prezzo medio dei prodotti venduti.
SELECT 
	categoria, 
	ROUND(AVG(prezzo_unitario),2) AS avg_prezzo
FROM vendite
GROUP BY categoria
ORDER BY avg_prezzo DESC;

-- Mostra il totale delle quantità vendute (SUM) per ciascun prodotto.
SELECT 
	prodotto, 
	SUM(quantita) AS sum_vendite
FROM vendite
GROUP BY prodotto
ORDER BY sum_vendite DESC;

-- Mostra il prezzo massimo e il prezzo minimo tra tutti i prodotti venduti.
SELECT 
	ROUND(MAX(prezzo_unitario),2) AS prezzo_massimo,
	ROUND(MIN(prezzo_unitario),2) AS prezzo_minimo
FROM vendite;

-- Conta quante vendite sono state registrate nella tabella Vendite.
SELECT COUNT(id) AS conta_vendite
FROM vendite;

-- I 5 prodotti più costosi (in base al prezzo_unitario)
SELECT 
	prodotto,
	prezzo_unitario
FROM vendite
ORDER BY prezzo_unitario DESC
LIMIT 5;

-- Mostra i nomi dei 3 prodotti con la quantità totale più bassa venduta (usa SUM e LIMIT).
SELECT 
	prodotto,
	SUM(quantita) AS quantita_totale
FROM vendite
GROUP BY prodotto
ORDER BY quantita_totale ASC
LIMIT 3;