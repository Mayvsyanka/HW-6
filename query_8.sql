select subjects.subject, teachers.name, round(avg(mark)) as avg_mark
from teachers
join marks on marks.subject_id = teachers.id
join subjects on subjects.teacher_id = teachers.id
where teachers.name = "Manuel Fisher"
group by teachers.name, subjects.subject;