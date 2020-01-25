from datetime import date
from dateutil.relativedelta import relativedelta

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
        self.pensionable_service_date = pensionable_service_date
        self.salary = salary
        self.status = status

    def __str__(self):
        return self.name + ' (' + self.birthdate.isoformat() + ')'
    
    def month_salary(self):
        return self.salary/12

    def nra(self):
        return 65
    
    def valuation_date(self):
        return date(2019,12,31)
        
    def normal_retirement_date(self):
        return date(self.birthdate.year+self.nra(), self.birthdate.month, self.birthdate.day)
    
    def age_at_valuation_date(self):
        return relativedelta(self.valuation_date(),self.birthdate)
    
    def pensionable_service(self):
        return relativedelta(self.valuation_date(),self.pensionable_service_date)
    
    def future_service(self):
        return relativedelta(self.normal_retirement_date(),self.valuation_date())
    
    def total_service(self):
        return relativedelta(self.normal_retirement_date(),self.pensionable_service_date)
