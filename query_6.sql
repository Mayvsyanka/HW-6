select class.name, students.student from students
join class on class.id = students.groups_id
where class.id = 3
group by class.name, students.student;