-- 프로그래머스 SQL 고득점 KIT (JOIN)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59043

SELECT AI.NAME, AI.DATETIME
FROM ANIMAL_INS AS AI
    LEFT JOIN ANIMAL_OUTS AS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AO.ANIMAL_ID IS NULL
ORDER BY AI.DATETIME
LIMIT 3;