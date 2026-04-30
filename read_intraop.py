import pandas as pd
import numpy as np
from datetime import datetime
import os
from pathlib import Path

def read_intraop():
    date_columns = date_columns = ['Intraop Date','Last updated on','Date of Surgery/Fecha de cirugía','Incident date']
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir.parent / "LF_Scripts" / "data"

    df = pd.read_excel(data_path / "Enrollment.xls", parse_dates=date_columns)
    



    df_intraop = pd.DataFrame(df)
    df_intraop['Enrollment date'] = df_intraop['Date of Surgery/Fecha de cirugía']
   

    return df_intraop

df_intraop = read_intraop()







#
#df[['Was the dressing not removed?','The wound looks clean and healthy']]= df[['Was the dressing not removed?','The wound looks clean and healthy']].fillna('')

df_intraop = df_intraop.rename(columns={'Tracked entity instance':'tei'})

df_intaop = pd.DataFrame(df_intraop,columns=['tei','Event','Enrollment date', 'Incident date', 'Geometry', 'Longitude', 'Latitude', 'Organisation unit name', 'Organisation unit code', 'Organisation unit', 'Card/Medical Record Number', 'Patient First Name',
'Patient Last Name',
'Sex',
'Date of Birth',
'Patient Age (For system use)',
'ASA Classification?',
'Anemia',
'Does the patient currently smoke cigarettes?',
'Does the patient have a diagnosis of hypertension?',
'Does the patient have diabetes?',
'HIV',
'Is the patient admitted to the ICU?',
'Is the patient hypothermic? (T<35C)',
'Is the patient malnourished? (BMI<18)',
'Is the patient obese? (BMI>30)',
'Is the patient on steroid medication?',
'Location of Surgery',
'Preoperative Diagnosis',
'PREOPDIA - Breast',
'PREOPDIA - Foregut/ Hepatobiliary',
'PREOPDIA - Gynecologic',
'PREOPDIA - Head & Neck',
'PREOPDIA - Hernia',
'PREOPDIA - Neurosurgical',
'PREOPDIA - Obstetric',
'PREOPDIA - Orthopedic',
'PREOPDIA - Skin/Soft Tissue',
'PREOPDIA - Small Bowel & Colorectal',
'PREOPDIA - Thoracic',
'PREOPDIA - Trauma',
'PREOPDIA - Urologic/Renal/Adrenal',
'Para',
'Gravida',
'Gestational Age (weeks)',
'What indication for Cesarean Section?',
'Was the sign-in read aloud?',
'Was the sign-in completed prior to anesthesia induction?',
'Sterility indicator inside the instrument tray?',
'Did the indicator change color?',
'Inside of instrument tray wet prior to start of operation?',
'Was the tray replaced?',
'Gauze count performed at beginning of case?',
'Total number of gauze counted?',
'Did surgeon scrub hands (enter OT with wet hands) prior to gowning?',
'What was available for handwashing at scrub sinks?',
'Did surgeon apply alcohol solution to hands in OT prior to gowning?',
'Were new surgical gloves used?',
'Sterility indicator inside the gown/drape pack?',
'Were the gowns or drapes wet prior to start of operation?',
'Did the gown indicator change color?',
'Was the gown/drape pack replaced?',
'Were the wet gowns replaced?',
'Were there holes in any of the gowns?',
'Were the torn gowns replaced?',
'Were there holes in any of the drapes?',
'Was the drape replaced or covered by another drape?',
'How was the patient surgical site prepared?',
'Vaginal Prep',
'Were antibiotics given?',
'INT-ABX - Ampicillin-sulbactam',
'INT-ABX - Aztreonam',
'INT-ABX - Cefazolin',
'INT-ABX - Cefotetan',
'INT-ABX - Cefoxitin',
'INT-ABX - Ceftazidime',
'INT-ABX - Ceftriaxone',
'INT-ABX - Clindamycin',
'INT-ABX - Ertapenem',
'INT-ABX - Fluconazole',
'INT-ABX - Gentamycin',
'INT-ABX - Metronidazole',
'INT-ABX - Penicillin',
'INT-ABX - Piperacillin-tazobactam',
'INT-ABX - Vancomycin',
'INT-ABX - Other',
'Where were the antibiotics administered?',
'What time were antibiotics given?',
'Is the patient on scheduled antibiotics?',
'Was Time Out read aloud?',
'Did the team announce the type of operation?',
'Was estimated blood loss announced before surgery?',
'What was estimated blood loss?',
'Time of incision (24 hour)',
'Gauze count performed at end of case?',
'Procedure - Total number of gauze counted?',
'Time dressing applied to wound (24 hour)',
'Procedure performed',
'PROC  - Head & Neck',
'PROC  - Neurosurgical',
'PROC - Breast',
'PROC - Foregut/ Hepatobiliary',
'PROC - Gynecologic',
'PROC - Hernia',
'PROC - Obstetric',
'PROC - Orthopedic',
'PROC - Skin/Soft Tissue',
'PROC - Small Bowel & Colorectal',
'PROC - Thoracic',
'PROC - Trauma',
'PROC - Urologic/Renal/Adrenal',
'Ruptured Membranes?',
'Were membranes ruptured at time of surgery?',
'Wound classification',
'Was the case elective or emergency?',
'Was the sign-out read aloud?',
'Was sign-out done in the operating theatre?',
'Unplanned intubation or reintubation?',
'Urgent tracheostomy or cricothyroidotomy?',
'Urgent need for central venous or direct arterial access?',
'Did any other crisis occur?',
'What was the crisis?',
'Death',
'Fetal death'])






df_intraop = df_intraop[['tei','Preoperative Diagnosis',

'Para',
'Gravida',
'Gestational Age (weeks)',
'What indication for Cesarean Section?',
'Was the sign-in read aloud?',
'Was the sign-in completed prior to anesthesia induction?',
'Sterility indicator inside the instrument tray?',
'Did the indicator change color?',
'Inside of instrument tray wet prior to start of operation?',
'Was the tray replaced?',
'Gauze count performed at beginning of case?',
'Total number of gauze counted?',
'Did surgeon scrub hands (enter OT with wet hands) prior to gowning?',
'What was available for handwashing at scrub sinks?',
'Did surgeon apply alcohol solution to hands in OT prior to gowning?',
'Were new surgical gloves used?',
'Sterility indicator inside the gown/drape pack?',
'Were the gowns or drapes wet prior to start of operation?',
'Did the gown indicator change color?',
'Was the gown/drape pack replaced?',
'Were the wet gowns replaced?',
'Were there holes in any of the gowns?',
'Were the torn gowns replaced?',
'Were there holes in any of the drapes?',
'Was the drape replaced or covered by another drape?',
'How was the patient surgical site prepared?',
'Vaginal Prep',
'PREOPDIA - Obstetric',
'PROC - Obstetric',
'Were antibiotics given?',
'INT-ABX - Ampicillin-sulbactam',
'INT-ABX - Aztreonam',
'INT-ABX - Cefazolin',
'INT-ABX - Cefotetan',
'INT-ABX - Cefoxitin',
'INT-ABX - Ceftazidime',
'INT-ABX - Ceftriaxone',
'INT-ABX - Clindamycin',
'INT-ABX - Ertapenem',
'INT-ABX - Fluconazole',
'INT-ABX - Gentamycin',
'INT-ABX - Metronidazole',
'INT-ABX - Penicillin',
'INT-ABX - Piperacillin-tazobactam',
'INT-ABX - Vancomycin',
'INT-ABX - Other',
'Where were the antibiotics administered?',
'What time were antibiotics given?',
'Is the patient on scheduled antibiotics?',
'Was Time Out read aloud?',
'Did the team announce the type of operation?',
'Was estimated blood loss announced before surgery?',
'What was estimated blood loss?',
'Time of incision (24 hour)',
'Gauze count performed at end of case?',
'Procedure - Total number of gauze counted?',
'Time dressing applied to wound (24 hour)',

'Ruptured Membranes?',
'Were membranes ruptured at time of surgery?',
'Wound classification',
'Was the case elective or emergency?',
'Was the sign-out read aloud?',
'Was sign-out done in the operating theatre?',
'Unplanned intubation or reintubation?',
'Urgent tracheostomy or cricothyroidotomy?',
'Urgent need for central venous or direct arterial access?',
'Did any other crisis occur?',
'What was the crisis?',
'Death',
'Fetal death']]



df_new = df_intraop.drop_duplicates(subset=['tei'], keep='first')


df_intraop_nd = df_new



