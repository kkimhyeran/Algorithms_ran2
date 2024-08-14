-- 코드를 입력하세요
-- WITH T1 AS (
--             SELECT CAR_ID
--             FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
--             WHERE TO_CHAR(START_DATE, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
--             GROUP BY CAR_ID
--             HAVING COUNT(*) >= 5
--             )
            
-- SELECT EXTRACT(MONTH FROM START_DATE) AS "MONTH"
--      , CAR_ID
--      , COUNT(*) AS "RECORDS"
-- FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- WHERE TO_CHAR(START_DATE, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
-- AND CAR_ID IN (SELECT CAR_ID FROM T1)
-- GROUP BY EXTRACT(MONTH FROM START_DATE), CAR_ID
-- HAVING COUNT(*) > 0
-- ORDER BY "MONTH" ASC, CAR_ID DESC;

SELECT TO_NUMBER(TO_CHAR(START_DATE, 'MM')) as month
     , car_id
     , count(*) as RECORDS
FROM car_rental_company_rental_history
WHERE car_id IN (
                SELECT car_id
                FROM car_rental_company_rental_history
                WHERE TO_CHAR(START_DATE, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
                GROUP BY car_id
                HAVING count(*) >= 5)
AND TO_CHAR(START_DATE, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
GROUP BY TO_CHAR(START_DATE, 'MM'), CAR_ID
HAVING count(*) <> 0 
ORDER BY month asc, car_id desc;