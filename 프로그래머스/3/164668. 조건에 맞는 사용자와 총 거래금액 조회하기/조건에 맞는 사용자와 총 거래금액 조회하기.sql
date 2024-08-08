-- 코드를 입력하세요

/*
<테이블>
- USED_GOODS_BOARD: 중고 거래 게시판 정보 테이블
- USED_GOODS_USER : 중고 거래 게시판 사용자 정보

<문제>
완료된 중고 거래의 총 금액이 70만원 이상인 사람의 회원id, 총 거래금액 출력
*/

SELECT b.writer_id
     , u.nickname
     , sum(b.price) as total_sales
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_USER u
ON b.WRITER_ID = u.USER_ID
AND b.STATUS = 'DONE'
GROUP BY b.writer_id, u.nickname
HAVING sum(b.price) >= 700000
ORDER BY total_sales asc


