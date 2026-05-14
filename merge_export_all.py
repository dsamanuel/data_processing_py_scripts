import pandas as pd
from datetime import datetime
import read_profile
import read_intraop
import read_ward
import read_fu_dc
import read_fu_audit
from pathlib import Path

# This script merges all the datasets (profile, intraop, ward, fu_dc, fu_audit) into a single dataframe and exports it as a CSV file with a timestamp in the filename.
df_p = read_profile.df_profile_nd
df_i = read_intraop.df_intraop_nd
df_w = read_ward.df_ward
df_f = read_fu_dc.df_fu_dc
df_f_a = read_fu_audit.df_fu_audit






result = df_p.merge(df_i, on='tei', how='left',suffixes=('','_INTRAOP'))
result = result.join(df_w, on='tei', how='left', rsuffix='_WARD')

final = result.merge(df_f, on='tei', how='left', suffixes=('','_DC'))
final_1 = final.merge(df_f_a, on='tei', how='left', suffixes =('','_AUDIT'))

current_dateTime = datetime.now().strftime('%Y-%m-%d-%H-%M')

#print(final_1)

current_dir = Path(__file__).resolve().parent
data_path = current_dir.parent / "LF_Scripts" / "Output"
final_1.to_csv(data_path / f'final_dataset-{current_dateTime}.csv')