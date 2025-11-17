-- 코드를 입력하세요
SELECT year, month, gender, count(DISTINCT user_id) as users
FROM (
    
    SELECT 
        TO_CHAR(a.SALES_DATE,'YYYY') AS YEAR
        , TO_NUMBER(TO_CHAR(a.SALES_DATE,'MM')) AS MONTH
        , a.user_id
        , a.online_sale_id
        , b.gender
    FROM online_sale a
    LEFT JOIN user_info b
    ON a.user_id = b.user_id
) 
WHERE  year IS NOT NULL
   AND  month IS NOT NULL
   AND  gender IS NOT NULL
GROUP BY year, month, gender
ORDER BY year, month, gender