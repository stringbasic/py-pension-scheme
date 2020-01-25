class Member:
    def __init__(
        self,
        name,
        birthdate,
        hire_date,
        membership_date,
        pensionable_service_date,
        salary,
        status
    ):
        self.name = name
        self.birthdate = birthdate
        self.hire_date = hire_date
        self.membership_date = membership_date
        self.pensinoable_service_date = pensionable_service_date
        self.salary = salary
        self.status = status

    def __str__(self):
        return self.name + ' (' + self.birthdate.isoformat() + ')'
