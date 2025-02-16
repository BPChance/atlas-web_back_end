-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    (IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE SUBSTRING_INDEX(style, ',', 1) = 'Glam rock'
ORDER BY lifespan DESC;
