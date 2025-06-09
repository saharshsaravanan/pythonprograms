class Teacher:
    def __init__(self,name,salary,gender):
        self.name = name
        self.salary = salary
        self.gender= gender

    def __str__(self):
        return (f"name:{self.name}: "
                f"salary:${self.salary}: "
                f"gender:{self.gender}")

