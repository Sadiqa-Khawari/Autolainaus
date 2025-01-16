# OLIONMUODOSTIN JA OLETUSARVOT
# =============================

class RasekoMember():
    """Creates a member of Raseko organisation"""
    def __init__(self, firstname, lastname, role="Student"):
        self.firstname = firstname
        self.lastname = lastname
        self.role = role

def palautaMerkkijono() -> str | int | bool:
    value = "Erkki"
    return value
    
if __name__ == "__main__":
    
    student = RasekoMember("Jonne", "Janttari")
    print(f"{student.firstname} rooli organisaatiossa {student.role}")

    teacher = RasekoMember("Mikko", "Mallikas", "Teacher")
    print(f"{teacher.firstname} rooli organisaatiossa {teacher.role}")

    print(palautaMerkkijono())