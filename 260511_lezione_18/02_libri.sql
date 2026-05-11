select * from vendite;
select * from libri;

/*
Esercizio 1 – INNER JOIN + WHERE + LIKE
	- Visualizzare l’elenco dei libri venduti in almeno un negozio, mostrando:
		- titolo del libro, autore, data_vendita, negozio.
	- Includere solo i libri il cui autore contiene la stringa “King” (indipendentemente da maiuscole/minuscole).
*/
SELECT
	l.titolo,
    l.autore,
    v.data_vendita,
    v.negozio
FROM		librerie.libri 		AS l
INNER JOIN	librerie.vendite 	AS v	ON l.id = v.id_libro
WHERE l.autore LIKE "%King%"
ORDER BY v.data_vendita DESC;

/*
Esercizio 2 – LEFT JOIN + WHERE + BETWEEN
	- Visualizzare tutti i libri, anche quelli che non hanno ancora vendite registrate, mostrando per ciascuno:
		- titolo, anno_pubblicazione, prezzo, data_vendita (se presente).
	- Filtrare i risultati per anno_pubblicazione compreso tra 2000 e 2010.
*/
SELECT
	l.titolo,
    l.anno_pubblicazione,
    l.prezzo,
    v.data_vendita
FROM		librerie.libri 		AS l
LEFT JOIN	librerie.vendite 	AS v	ON l.id = v.id_libro
WHERE l.anno_pubblicazione BETWEEN 2000 AND 2010;

/*
Esercizio 3 – INNER JOIN + WHERE + IN
	- Visualizzare i dati dei libri venduti nei negozi appartenenti a una lista specifica:
		- ("9 Oriole Lane", "98558 Milwaukee Point", "98016 Esch Trail").
	- Mostrare titolo, negozio, quantita, prezzo totale (quantita * prezzo).
*/
SELECT
	l.titolo,
    v.negozio,
    v.quantita,
    v.quantita * l.prezzo	AS prezzo_totale
FROM		librerie.libri 		AS l
LEFT JOIN	librerie.vendite 	AS v	ON l.id = v.id_libro
WHERE v.negozio IN ("9 Oriole Lane",
					"98558 Milwaukee Point", 
                    "98016 Esch Trail");

/*
Esercizio 4 – RIGHT JOIN + WHERE + LIKE + BETWEEN
	- Mostrare tutti i record di vendita, anche quelli che fanno riferimento a libri non più presenti nella tabella Libri (caso anomalo).
		- Mostrare: titolo (se esiste), data_vendita, prezzo, quantita.
		- Includere solo le vendite:
			- avvenute tra il 2020-01-01 e il 2022-12-31
			- presso negozi il cui nome contiene la parola “Drive” (case-insensitive).
*/
SELECT
	l.titolo,
    v.data_vendita,
    l.prezzo,
    v.quantita
FROM		librerie.libri 		AS l
RIGHT JOIN	librerie.vendite 	AS v	ON l.id = v.id_libro
WHERE 	v.data_vendita 	BETWEEN "2020-01-01" AND "2022-12-31" 
AND 	v.negozio 		LIKE 	"%Drive%";

/*
Esercizio 5 – INNER JOIN + WHERE combinato
	- Mostrare titolo, autore, prezzo e data_vendita dei libri:
		- con genere IN (‘Fantasy’, ‘Horror’, ‘Drama’) (ignora i libri con >1 genere)
		- pubblicati dopo il 2015,
		- venduti in negozi il cui nome contiene ‘Plaza’,
		- ordinati dal più recente al più vecchio.
*/
SELECT
	l.titolo,
    l.autore,
    l.prezzo,
	v.data_vendita
FROM		librerie.libri 		AS l
RIGHT JOIN 	librerie.vendite 	AS v	ON l.id = v.id_libro
WHERE	l.genere	IN	("Fantasy", "Horror", "Drama")
AND		v.negozio	LIKE "%Plaza%"
ORDER BY v.data_vendita DESC;