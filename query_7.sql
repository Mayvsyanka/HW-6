select class.name, subjects.subject, marks.mark from marks
join students on students.id = marks.student_id
join subjects on subjects.id = marks.subject_id
join class on class.id = students.groups_id
where class.id = 3
group by class.name, subjects.subject, marks.mark
order by subjects.subject DESC;