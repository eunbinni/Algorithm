SELECT count(distinct(name))
from animal_ins
where name is not null;

/*
 distinct(name)으로 중복 제거 후 개수 count하기
 */