from pension.model import member
from datetime import date
import pandas as pd

def load_csv(file_path):
    members_raw=pd.read_csv('resources/members.csv',';')
    members=[]
    for i, row in members_raw.iterrows():
        members.append(member.Member(
                row['name'],
                date.fromisoformat(row['birthdate']),
                date.fromisoformat(row['hire_date']),
                date.fromisoformat(row['membership_date']),
                date.fromisoformat(row['pensionable_service_date']),
                row['salary'],
                row['status']
            )
        )
    return members
