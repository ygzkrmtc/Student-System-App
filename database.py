# SQL database codes

def create_student_table(self):
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(name TEXT, surname TEXT, identity TEXT, password TEXT"
                   ",credit INT, lectures LIST )")

def add_student_to_table(self, name, surname, identity, credit, password):
    cursor.execute("INSERT INTO ogrenciler(name, surname, identity, password, credit)"
                   "VALUES(?,?,?,?,?)", (name, surname, identity, password, credit))
    con.commit()

def remove_student_from_table(self, name, surname, identity, credit, password):
    cursor.execute("DELETE FROM ogrenciler VALUES(name, surname, identity, credit, password)"
                   "VALUES(?,?,?,?,?,?)", (name, surname, identity, credit, password))
    con.commit()
