select students.student, round(AVG(mark), 2) as average_mark
from marks
join students on students.id = marks.student_id
group by students.student
order by average_mark DESC
LIMIT 5;