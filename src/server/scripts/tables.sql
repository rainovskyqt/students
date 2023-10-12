CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE groups(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname VARCHAR(100),
    name VARCHAR(100)
);

CREATE TABLE group_students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY(group_id)
        REFERENCES groups(id)
            ON DELETE NO ACTION,
    FOREIGN KEY(student_id)
        REFERENCES students(id)
            ON DELETE NO ACTION
);

