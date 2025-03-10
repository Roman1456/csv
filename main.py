def create():
    open()
    cursor.execute('''PRAGMA foreing_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY,
            name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY,
                question VARCHAR,
                answer VARCHAR,
                wrong1 VARCHAR,
                wrong2 VARCHAR,
                wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id) )''')

    close()