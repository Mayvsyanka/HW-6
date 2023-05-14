select subjects.subject, class.name, round(AVG(mark), 2) as average_mark
from marks
join students on students.id = marks.student_id
join subjects on subjects.id = marks.subject_id
join class on class.id = students.groups_id
where subjects.id = 1
group by class.name, subjects.subject
order by average_mark DESC;