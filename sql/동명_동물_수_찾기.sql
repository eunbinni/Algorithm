select name, count(name)
from animal_ins
where name is not null
group by name
having count(name) >= 2
order by name;

/*
where과 having의 차이
- where : 전체 테이블에서 조건을 걸 때 사용
- having : group by와 함께 쓰이며, group한 새로운 테이블에서 조건을 걸 때 사용
*/