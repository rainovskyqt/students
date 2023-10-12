from .models import Student, NewId
from database.db_manager import base_manager

ID = 0
SURNAME = 1
NAME = 2
GROUP_ID = 3


def get_students(group_id: int):
    res = base_manager.execute("SELECT S.id, S.surname, S.name, GS.group_id "
                               "FROM students S "
                               "INNER JOIN group_students GS ON GS.student_id = S.id "
                               "WHERE GS.group_id = ?", args=(group_id, ), many=True)
    students = []
    print(res)
    for student in res['data']:
        students.append(Student(id=student[ID], surname=student[SURNAME], name=student[NAME],
                                group_id=student[GROUP_ID]))
    return students


def add_new_student(new_student: Student, ):
    res = base_manager.execute("INSERT INTO students(surname, name) "
                               "VALUES (?, ?) "
                               "RETURNING id", args=(new_student.surname, new_student.name,))
    return NewId(code=res['code'], id=res['data'][0][0])


def update_student(student_id: int, student: Student):
    res = base_manager.execute("UPDATE students SET surname = ?, name = ? WHERE id = ?",
                               args=(student.surname, student.name))
    return NewId(code=res['code'], id=student_id)


def delete_student(student_id: int):
    res = base_manager.execute("DELETE FROM students WHERE id = ?",
                               args=(student_id,))
    return NewId(code=res['code'], id=student_id)