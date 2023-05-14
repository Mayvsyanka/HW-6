select subjects.subject, teachers.name from subjects
join teachers on subjects.teacher_id = teachers.id
group by subjects.subject, teachers.name