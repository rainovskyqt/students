INSERT INTO posts(name)
VALUES('Администратор'), ('Преподаватель'), ('Студент');

INSERT INTO users(login, password, post_id)
VALUES ('admin', 'admin', 1);

INSERT INTO groups(name)
VALUES ('3ИСПк-1'), ('3ИСПк-2'), ('4ИСПк-1'), ('4ИСПк-2');

INSERT INTO students(id, surname, name)
VALUES(1, 'Иванов', 'Иван'), (2, 'Петров', 'Петр'), (3, 'Сидоров', 'Сидр');

INSERT INTO group_students(group_id, student_id)
VALUES(1, 1), (2, 2), (2, 3);