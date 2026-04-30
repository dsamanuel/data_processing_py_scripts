import pandas as pd
import os
import numpy as np
from datetime import datetime
from pathlib import Path


def read_profile():
    date_columns = ['Intraop Date','Last updated on','Date of Surgery/Fecha de cirugía','Incident date']
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir.parent / "LF_Scripts" / "data"
    df = pd.read_excel(data_path / "PatientProfile.xls", parse_dates=date_columns)
    



    df_profile = pd.DataFrame(df)
    df_profile['Enrollment date'] = df_profile['Date of Surgery/Fecha de cirugía']
    df_profile = df_profile[['Tracked entity instance','Enrollment date','Organisation unit name','Organisation unit','Data Collectors Name','Card/Medical Record Number','Patient First Name','Patient Last Name','Date of Birth','Patient Age (For system use)','Sex','Contact name - Phone number 1','Contact name - Phone number 2','Contact name - Phone number 3','Phone Number 1','Phone Number 2','Phone Number 3','ASA Classification?','Does the patient currently smoke cigarettes?','Does the patient have Anemia ?','Does the patient have a diagnosis of hypertension?','Does the patient have diabetes?','Is the patient HIV+?','Is the patient admitted to the ICU?','Is the patient hypothermic? (T<35C)','Is the patient malnourished? (BMI<18)','Is the patient obese? (BMI>30)','Is the patient on steroid medication?','Location of Surgery'
]]
   
    return df_profile

df_profile = read_profile()
df_profile = df_profile.rename(columns={'Tracked entity instance':'tei'})

df_new = df_profile.drop_duplicates(subset=['tei'], keep='first')


df_profile_nd = df_new

