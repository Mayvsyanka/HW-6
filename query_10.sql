select students.student, teachers.name, subjects.subject from students
join marks on students.id = marks.student_id
join subjects on subjects.id = marks.subject_id
join teachers on teachers.id = subjects.teacher_id
where students.id = 5 and teachers.id = 1
group by students.student, subjects.subject, teachers.name;