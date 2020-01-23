from pension.model import member
import pandas as pd

def load_members(file_path):
    members_raw=pd.read_csv('resources/members.csv',';')
    members=[]
    for i, row in members_raw.iterrows():
        members.append(member.Member(
                row['name'],
                row['birthdate'],
                row['hire_date'],
                row['membership_date'],
                row['pensioable_service_date'],
                row['salary'],
                row['status']
            )
        )
    return members    

