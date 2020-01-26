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
        status,
        gender
    ):
        self.name = name
        self.birthdate = birthdate
        self.hire_date = hire_date
        self.membership_date = membership_date
        self.pensionable_service_date = pensionable_service_date
        self.salary = salary
        self.status = status
        self.gender = gender

    def __str__(self):
        return self.name + ' (' + self.birthdate.isoformat() + ')'
    
    def month_salary(self):
        return self.salary/12
       
    def normal_retirement_date(self, nra):
        return date(self.birthdate.year+nra, self.birthdate.month, self.birthdate.day)
    
    def age_at_valuation_date(self, valuation_date):
        return relativedelta(valuation_date,self.birthdate)
    
    def pensionable_service(self, valuation_date):
        return relativedelta(valuation_date,self.pensionable_service_date)
    
    def prospective_service(self, nra, valuation_date):
        return relativedelta(self.normal_retirement_date(nra),valuation_date)
    
    def total_service(self, nra):
        return relativedelta(self.normal_retirement_date(nra),self.pensionable_service_date)

# Following a recent review, the government has announced plans to bring this timetable forward. 
# The State Pension age would therefore increase to 68 between 2037 and 2039
# Date of birthday on or before 5 April 1970 is 60 for female and 65 for male
# Date of birthday between 6 April 1970 and 5 april 1978 State pension age is currently 67. it would increase to between 67 yeras and 1 month, and 68, depending on date of birth
# Date of birthday after 6 April 1978 The state Pension age remains 68                  

    def state_pension_age (self):
        if self.birthdate<=date(1948, 4, 5) and self.gender=="F":
            state_pension_age=60
        elif self.birthdate<=date(1948, 4, 5) and self.gender=="M":
            state_pension_age=65
        elif self.birthdate>date(1970, 4, 6) and self.birthdate<date(1978, 4, 5):
            state_pension_age=67
        elif self.birthdate>date(1978, 4, 6):
            state_pension_age=68
        return state_pension_age
            
    