/*
Si consideri un database che contiene informazioni su una libreria. Nel database è presente una tabella chiamata Libri con la seguente struttura:
Libri (
	id INT PRIMARY KEY,
	titolo VARCHAR(100),
	autore VARCHAR(100),
	genere VARCHAR(50),
	prezzo DECIMAL(5,2),
	anno_pubblicazione INT
	)
*/
CREATE TABLE `Libri` (
`id` 					INT PRIMARY KEY,
`titolo` 				VARCHAR(100),
`autore` 				VARCHAR(100),
`genere` 				VARCHAR(50),
`prezzo` 				DECIMAL(5,2),
`anno_pubblicazione`	INT
);

/*
1) Inserimento Dati (INSERT INTO)
Inserire almeno 6 nuovi libri nella tabella Libri usando il comando SQL INSERT INTO.
I libri devono appartenere a generi e autori diversi, ed essere pubblicati in anni differenti.
 */
INSERT INTO Libri (id, titolo, autore, genere, prezzo, anno_pubblicazione)
VALUES
    (01, 'Il Grande Gatsby', 'F. Scott Fitzgerald', 'Narrativa Classica', 11.00, 1925),
    (02, '1984', 'George Orwell', 'Distopia', 14.00, 1949),
    (03, 'Io uccido', 'Giorgio Faletti', 'Thriller', 15.00, 2002),
    (04, 'Sapiens. Da animali a dei', 'Yuval Noah Harari', 'Saggistica', 18.00, 2011),
    (05, 'L''analfabeta che sapeva contare', 'Jonas Jonasson', 'Umoristico', 12.00, 2013),
    (06, 'Il problema dei tre corpi', 'Liu Cixin', 'Fantascienza', 16.00, 2008);

-- Inserimento libri extra per esercizio 2
INSERT INTO Libri 
	(id, titolo, autore, genere, prezzo, anno_pubblicazione)
VALUES
    (07, 'Tenera è la notte', 'F. Scott Fitzgerald', 'Narrativa Classica', 13.00, 1934),
    (08, 'La fattoria degli animali', 'George Orwell', 'Distopia', 10.50, 1945),
    (09, 'La foresta dei segreti', 'Liu Cixin', 'Fantascienza', 17.50, 2008),
    (10, 'Appunti di un venditore di donne', 'Giorgio Faletti', 'Thriller', 14.00, 2010),
    (11, 'Homo Deus. Breve storia del futuro', 'Yuval Noah Harari', 'Saggistica', 20.00, 2015),
    (12, 'Il buio oltre la siepe', 'Harper Lee', 'Narrativa Classica', 12.50, 1960),
    (13, 'Fahrenheit 451', 'Ray Bradbury', 'Distopia', 13.00, 1953),
    (14, 'Il suggeritore', 'Donato Carrisi', 'Thriller', 15.50, 2009),
    (15, 'Fondazione', 'Isaac Asimov', 'Fantascienza', 16.00, 1951),
    (16, 'Armi, acciaio e malattie', 'Jared Diamond', 'Saggistica', 19.00, 1997),
    (17, 'Brave New World', 'Aldous Huxley', 'Distopia', 12.00, 1932),
    (18, 'Il centenario che saltò dalla finestra e scomparve', 'Jonas Jonasson', 'Umoristico', 14.50, 2009);
    
/*
2) Aggregazone e raggruppamento (GROUP BY)
Scrivere una query che, usando il comando GROUP BY, mostri per ogni genere:
- il numero totale di libri presenti;
- il prezzo medio dei libri appartenenti a quel genere.
La query dovrà restituire il risultato ordinato alfabeticamente per genere.
*/
SELECT 
	genere,
    COUNT(id) 				AS tot_libri,
    ROUND(AVG(prezzo),2) 	AS avg_prezzo
FROM Libri
GROUP BY genere
ORDER BY genere ASC;

/*
3) Ordinamento risultati (ORDER BY)
Scrivere una query che elenchi tutti i libri pubblicati dopo l’anno 2010 ordinati in modo 
decrescente per anno di pubblicazione e, in caso di anno uguale, in ordine crescente per prezzo.
*/
SELECT 
	titolo, 
    anno_pubblicazione,
    prezzo
FROM Libri
WHERE anno_pubblicazione > 2005
ORDER BY
	anno_pubblicazione DESC,
    prezzo ASC;