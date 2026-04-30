import pandas as pd
import numpy as np
from pathlib import Path


def read_inpatient():
    date_columns = ['Date of Surgery/Fecha de cirugía','Rounding date', 'Incident date','FOLLOWUP - Date of discharge']
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir.parent / "LF_Scripts" / "data"
    df = pd.read_excel(data_path / "Inpatient.xls", parse_dates=date_columns)
   
    df_inpatient = pd.DataFrame(df)

    return df_inpatient

df = read_inpatient()

#
#df[['Was the dressing not removed?','The wound looks clean and healthy']]= df[['Was the dressing not removed?','The wound looks clean and healthy']].fillna('')

df = df.rename(columns={ 'Tracked entity instance':'tei','FOLLOWUP - Date of discharge':'Date of discharge'})
df1 = pd.DataFrame(df,columns=['tei', 'Was the dressing not removed?', 'The wound looks clean and healthy', 'WARD_INSP - Were stitches removed or the surgeon opened the wound intentionally out of concern for infection?',
'WARD_INSP - Did a previously closed wound open up spontaneously because of infection?', 'WARD_INSP - Pus draining from the wound?',
'WARD_INSP - Does the patient have an abscess? (Clinically by swelling or radiographically?)','WARD_INSP - Is there redness extending around the wound?','WARD_INSP - Does the patient have Fever (≥ 38.5C)',
'WARD_ANTI - Is the patient prescribed antibiotics?','ABX - Ampicillin-sulbactam', 'ABX - Aztreonam', 'ABX - Cefazolin', 'ABX - Cefotetan', 'ABX - Cefoxitin',
'ABX - Ceftazidime','ABX - Ceftriaxone','ABX - Clindamycin', 'ABX - Ertapenem', 'ABX - Fluconazole', 'ABX - Gentamycin', 'ABX - Metronidazole',
'ABX - Other', 'ABX - Penicillin', 'ABX - Piperacillin-tazobactam', 'ABX - Vancomycin', 'WARD_COMP - Did the patient return to operating room?',
'ABXWHAT - Chorioamnionitis', 'ABXWHAT - Deep wound infection', 'ABXWHAT - Endometritis', 'ABXWHAT - Intraabdominal fluid collection',
'ABXWHAT - Meningitis', 'ABXWHAT - Organ space infection', 'ABXWHAT - Pneumonia', 'ABXWHAT - Postoperative prophylaxis','ABXWHAT - Superficial wound infection',
'ABXWHAT - Treatment Course for surgical diagnosis', 'ABXWHAT - Urinary tract infection', 'WARD_COMP - What operation was performed?',
'WARD_COMP - Did the patient develop any other complications?', 'WARD_COMP - Endometritis?','WARD_COMP - Other complication? (DVT, PE, etc.)',
'WARD_COMP - Please list the complication.', 'WARD_COMP - Pneumonia?', 'WARD_COMP - Urinary tract infection?','WARD_COMP - Was the patient discharged today?',
'WARD_COMP - What is the indication for antibiotics?', 'Death', 'Neonatal Death', 'Ward Encounter (Ward)','Date of discharge'])
df2 = pd.DataFrame(df,columns=['tei', 'Event'])
#df1 = df1.set_index('tei')

#df0 = df.groupby('tei').agg({'wdr': ',' .join, 'Event':','.join, 'The wound looks clean and healthy': ','.join})
column_name_join = ['Was the dressing not removed?', 'The wound looks clean and healthy', 'WARD_COMP - Please list the','WARD_COMP - What operation was performed?',
'Data Collectors Name (Ward)']

column_name_max = ['Ward Encounter (Ward)','Death','Neonatal Death']

column_name_dt = ['Date of discharge']


column_name_01 = ['WARD_INSP - Were stitches removed or the surgeon opened the wound intentionally out of concern for infection?','WARD_INSP - Did a previously closed wound open up spontaneously because of infection?',
'WARD_INSP - Pus draining from the wound?',
'WARD_INSP - Does the patient have an abscess? (Clinically by swelling or radiographically?)',
'WARD_INSP - Is there redness extending around the wound?',
'WARD_INSP - Does the patient have Fever (≥ 38.5C)',
'WARD_ANTI - Is the patient prescribed antibiotics?',
'ABX - Ampicillin-sulbactam',
'ABX - Aztreonam',
'ABX - Cefazolin',
'ABX - Cefotetan',
'ABX - Cefoxitin',
'ABX - Ceftazidime',
'ABX - Ceftriaxone',
'ABX - Clindamycin',
'ABX - Ertapenem',
'ABX - Fluconazole',
'ABX - Gentamycin',
'ABX - Metronidazole',
'ABX - Other',
'ABX - Penicillin',
'ABX - Piperacillin-tazobactam',
'ABX - Vancomycin',
'WARD_COMP - Did the patient return to operating room?',
'ABXWHAT - Chorioamnionitis',
'ABXWHAT - Deep wound infection',
'ABXWHAT - Endometritis',
'ABXWHAT - Intraabdominal fluid collection',
'ABXWHAT - Meningitis',
'ABXWHAT - Organ space infection',
'ABXWHAT - Pneumonia',
'ABXWHAT - Postoperative prophylaxis',
'ABXWHAT - Superficial wound infection',
'ABXWHAT - Treatment Course for surgical diagnosis',
'ABXWHAT - Urinary tract infection',
'WARD_COMP - Did the patient develop any other complications?',
'WARD_COMP - Endometritis?',
'WARD_COMP - Other complication? (DVT, PE, etc.)',
'WARD_COMP - Pneumonia?',
'WARD_COMP - Urinary tract infection?',
'WARD_COMP - Was the patient discharged today?',
'WARD_COMP - What is the indication for antibiotics?',
'Other Antibiotics - Indications']

df_0 = pd.DataFrame(df2,columns=['tei', 'Event'])
df_0 = df_0.groupby(['tei']).agg({'Event':','.join})

for (columnName) in df1:
    cn = columnName
    if cn in column_name_01:
          df1[cn]= df1[cn].fillna(0).astype(np.int64)
          df2 = df1.groupby(['tei'])[cn].sum()
          df_0 = df_0.join(df2)
    elif cn in column_name_join:
          df1[cn]= df1[cn].fillna('').astype(str)
          df2 = df1.groupby(['tei']).agg({cn: ','.join})
          df_0 = df_0.join(df2)
    elif cn in column_name_max:
          #df2 = df1.groupby(['tei']).agg({cn.max()})
          df1[cn]= df1[cn].fillna(0).astype(np.int64)
          df2 = df1.groupby(['tei'])[cn].max()
          df_0 = df_0.join(df2)
    elif cn in column_name_dt:
          df2 = df1.groupby(['tei'])[cn].max()
          df_0 = df_0.join(df2)
 

          #print(df[cn].info)
          
#for i in len(df1.columns):
  #  df_1 = df1.groupby([df1.iloc[:, [0, 0]]]).agg({[df1.iloc[:, [0, i]]]})

#df2 = df1.groupby(['tei']).agg({'wdr': ','.join})
#df3 = df1.groupby(['tei']).agg({'The wound looks clean and healthy': ','.join})
#
#df = df.astype({'Organisation unit name': 'string', 'Enrollment date':'date', 'Incident date':'date'})
#df['Enrollment date'] = df['Enrollment date'].astype('datetime64[ns]')

#df[['Enrollment date', 'Incident date']] = pd.to_datetime(df[['Enrollment date','Incident date']])

#df4 = pd.merge(df2, df3, how = 'left', on = 'tei')
#print(df4.dtypes)

df_ward = df_0

#df_ward['The wound looks clean and healthy', 'Was the dressing not removed?'].fillna('').astype(str)
#df1[cn]= df1[cn].fillna('').astype(str)
df_ward.loc[df_ward['Was the dressing not removed?'].str.contains('Yes|No'), 'Was the dressing not removed?-new'] = 'Yes'
df_ward.loc[df_ward['The wound looks clean and healthy'].str.contains('Yes|No'), 'The wound looks clean and healthy-new'] = 'Yes'
df_ward.loc[df_ward['Was the dressing not removed?'].str.contains('No'), 'Was the dressing not removed?-new'] = 'No'
df_ward.loc[df_ward['The wound looks clean and healthy'].str.contains('No'), 'The wound looks clean and healthy-new'] = 'No'



