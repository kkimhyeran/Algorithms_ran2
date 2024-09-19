-- 코드를 입력하세요
SELECT substr(product_code,1, 2) as category
     , count(*) as products
FROM PRODUCT
GROUP BY substr(product_code,1, 2)
ORDER BY category asc
