select students.student, subjects.subject from students
join marks on students.id = marks.student_id
join subjects on subjects.id = marks.subject_id
where students.id = 5
group by students.student, subjects.subject;