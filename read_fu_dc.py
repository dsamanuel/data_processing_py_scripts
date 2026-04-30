import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

def read_followup():
    date_columns = ['FOLLOWUP - Date of phone call']
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir.parent / "LF_Scripts" / "data"
    df8 = pd.read_excel(data_path / "FU.xls", parse_dates=date_columns)

    df_followup_dc = pd.DataFrame(df8)
    return df_followup_dc


df_fu = read_followup()








#
#df[['Was the dressing not removed?','The wound looks clean and healthy']]= df[['Was the dressing not removed?','The wound looks clean and healthy']].fillna('')


df_fu = df_fu.rename(columns={'Tracked entity instance':'tei'})


df1 = pd.DataFrame(df_fu,columns=['tei','FOLLOWUP - Date of phone call',
'FOLLOWUP - Patient status',
'Neonatal Death',
'FOLLOWUP - Did your wound open up?',
'FOLLOWUP - Is there drainage from the wound?',
'What kind of drainage?',
'FOLLOWUP - Have you visited a healthcare provider since discharge?',
'FOLLOWUP - If yes, where?',
'FOLLOWUP - Did you have a scheduled postoperative visit when you left the hospital?',
'FOLLOWUP - If yes, did you go to that visit?',
'FOLLOWUP - If no visit, why not?',
'Data Collectors Name (Outpatient)',
'Was a call successfully ?',
'Why was not successfully'])

column_name_join = ['Was a call successfully ?', 'Why was not successfully', 'FOLLOWUP - Patient status',
'FOLLOWUP - Have you visited a healthcare provider since discharge?', 'FOLLOWUP - If yes, where?',
'FOLLOWUP - If yes, did you go to that visit?','FOLLOWUP - If no visit, why not?','What kind of drainage?','Data Collectors Name (Outpatient)',
]


column_name_max = ['Neonatal Death', 'FOLLOWUP - Did your wound open up?', 'FOLLOWUP - Is there drainage from the wound?',
'FOLLOWUP - Did you have a scheduled postoperative visit when you']


column_name_dt = ['FOLLOWUP - Date of phone call']


column_name_01 = []

df_0 = pd.DataFrame(df_fu,columns=['tei', 'Event'])
df_0 = df_0.groupby(['tei']).agg({'Event':','.join})



for (columnName) in df1:
    cn = columnName
    if cn in column_name_join:
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
 

df_fu_dc = df_0

df_fu_dc.loc[df_fu_dc['Was a call successfully ?'].str.contains('Yes'), 'Was a call successfully -new'] = 'Yes'
df_fu_dc.loc[df_fu_dc['FOLLOWUP - Have you visited a healthcare provider since discharge?'].str.contains('Yes'), 'FOLLOWUP - Have you visited a healthcare provider since discharg-new'] = 'Yes'
df_fu_dc.loc[df_fu_dc['FOLLOWUP - If yes, did you go to that visit?'].str.contains('Yes'), 'FOLLOWUP - If yes, did you go to that visit?-new'] = 'No'


