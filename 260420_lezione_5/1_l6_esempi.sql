-- SELECT
SELECT *
FROM world.country;

-- SELECT DISTINCT
SELECT DISTINCT Continent
FROM world.country;

-- WHERE
SELECT *
FROM world.country
WHERE Region = 'Antartica';

-- ORDER BY
SELECT Region, SurfaceArea
FROM world.country
ORDER BY Region, SurfaceArea;

-- GROUP BY
SELECT Region, COUNT(Region)
FROM world.country
GROUP BY Region
ORDER BY Region;

-- INSERT INTO
INSERT INTO world.country(Code, Name, IndepYear)
VALUES('QBC', 'NomePaese', '2022');

-- UPDATE
UPDATE world.country
SET Name = 'NuovoNome', Population = 432000
WHERE Code = 'QBC';

-- DELETE
DELETE
FROM world.country
WHERE Code = 'QBC';