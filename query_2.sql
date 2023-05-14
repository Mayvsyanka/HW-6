select subjects.subject, students.student, round(AVG(mark), 2) as average_mark
from marks
join students on students.id = marks.student_id
join subjects on subjects.id = marks.subject_id
where subjects.id = 4
group by students.student
order by average_mark DESC
LIMIT 1;