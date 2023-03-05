import streamlit as st
import datetime
import numpy as np
import pandas as pd
import os
import json
from PIL import Image
import gspread
from google.oauth2.service_account import Credentials
gc=gspread.service_account(filename="credentials.json")
gccrop=gc.open_by_key("1dJNbU_GiTHQspDM__aUpR7LLiiAhS1zHBXWlriqWe5s")
gcclone=gc.open_by_key("1QRlw2aCIekYJ7O73CtvG46tsB1pOKhUDPNpV0mP0QRk")
gcoperator=gc.open_by_key("14iMHAexjiAQGiMDPJQmmuUfbf74lc2bxDwhCHT-plXI")
#cropdf= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/images/crop.xlsx")
#clonedf=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/images/Clones.xlsx")
#operatordf=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/images/operator.xlsx")
cropsheet = gccrop.get_worksheet(0)
cropdf = pd.DataFrame(data=cropsheet.get_all_records())
clonesheet=gcclone.get_worksheet(0)
clonedf = pd.DataFrame(data=clonesheet.get_all_records())
operatorsheet=gcoperator.get_worksheet(0)
operatordf=pd.DataFrame(data=operatorsheet.get_all_records())
img = Image.open("images/sreepadma_logo.jpg")
col1, col2, col3 = st.columns([4,6,1])
with col1:
 st.write("")
with col2:
 st.image(img,width=150)
with col3:
 st.write("")
st.title('Sreepadma AquaFlora Stock Details')
col1,col2=st.columns(2)
with col1:
 date_input=st.date_input('Date')
type_list = ['PIR Production', 'Export','Initiation','Import','Contamination','Greenhouse','Discard']
crop_list=['RANACULUS', 'MOSS', 'STAUROGYNE','CRYPTOCORYNE','SYNGONIUM','HYGROPHYLLA','ANUBIAS','BUCEPHALANDRA','AGLONEMA','ALTERNENDRA','CREPIDOMANES FERN','GLOSSOSTIGMA','LAGNENDRA','LUDWIGIA REPENS','ELEOCHARIS','MICRANTHEMUM','ROTALA','ECHINODORUS','RICCARDIA','HEMIANTHUS CUBA','LILAEOPSIS BRASILIENSIS','LIMNOPHILA','POGOSTEMON','AMMANNIA','LOBELIA CARDINALIS','MADAGASCAR LACE','GRATIOLA VISCIDULA','APONOGETON MADAGASCARIENSIS','TONINA FLUVIATILIS','HYDROCOTYLE TRIPATITA','UTRICULARIA GRAMINIFOLIA','PROSERPINACA PALUSTRIS','RICCIA FLUITANS','FISSIDENS CRISPULUS','EROCAULON BREVISCAPUM','MICROSORUM PTEROPUS','BACOPA SALZAMANNII','BOLBITIS']
with col2:
 type = st.multiselect("Type ", options=type_list)
 type = str(type)[2:-2]
col1,col2=st.columns(2)
with col1:
 #crop = st.multiselect("Crop", options=crop_list)
 crop=st.multiselect("Crop", options=cropdf)
 crop=str(crop)[2:-2]
with col2:
 clone=st.multiselect("Clone", options=clonedf)
 #clone = st.multiselect("Clone", options=['SR1','AS201H','CM1A','LK1','GE1A','HP81A','CR61A','ET41','CR41A','CR102A','EP1','ET1','CR81A','EP21','CR121E','LB1','CR22C','LR1','SR41','RR1','MC21','MU1','AS151K','BC41 Z','BC1Z','RN1', 'CR1','CR21','CR121A','CR21','CR21A','CR103','CR103A','CR141','CR161','CR181','CR201','CR221','CR221A','CR241','CR261','CR241A','CR181A',
#'CR21C','HP1','HP21','HP41','HP81','SR22','SGJ','AR1A','AG1', 'AG21','AGSRC','MC1','MS41','MS61','MS81','MS101','ASIE','AS1F','AS51F','AS51G','AS51I','AS51J','AS151A','AS151I','AS201A','AS201F','AS251D','AS251E','AS251F','AS251G','AS251H','AS251I','AS251K','AS401','AS401A','CR281','AS151L','CR241C','CR241D','CR261C','AS201J','BC101A','AS101D','AS51L','CR201D','CR201C','AS451A','RC1','AS101E','AS1I',
#'AS301','AS301E','AS301F','AS301I','AS301J','AS301K','AS301L','AS301M','AS301N','AS301O','AS351','AS351A','AS351C','BC61','BC1','BC21','BC41','CR121C','CR121D','CF1','AG21A','AG21C','GE1','AR1','CR22','CR22A','BC1 Z','BC41 Z', 'CR121','CR41','CR61','CR81','CR102','CR141A','BC81','BC101','CR261A','CM1','AS451','CR201A','CR201C','AS151J','AS101D','AS51M','AS201K','AS1K','AS1L','AS51N','BC101D','AS351D','AS1J','RF1','RB1','RL1','LA1','AS351E','CR181D','ET61','AS551','AS151L','LC1','AR21','CR181C','CR82','CR41C','AS601','AS651','AS252','AS252A','AS402','AS2','CR301','CR104','AS501','AS1M','AS701','AS1N','AS1"O"','CR391','CR321','PH1','AT1','MM1','ET81','AR101','CR361','AS751','AS201K','GV1','SR81','AS51','CR381','CR341','AR2','CR42','CR242','CR83','ET101','MU2','AM1','PH21','RD 1','RD 1 A','RD 1 C','RD 1 D','RD 1 E','ET 121','ET 121 A','ET 141','RF 1','RW 1','RL 21','HT 41','HT 21','RR 41','TF 1','AR 51''EP 81','PH 41','PH 2 D','UG 1','RM 1','RM 21','PP 1','RB 21','RB 41','HP 1 A','HP 1 C','HP 1 D','AM 21','SR 1 #D','SR 1 E','MS 82','MU 2 A','MU 2 C','MU 2 D','MU 2 E ','MU 2 F','MU 2 G','MU 2 I','MU 2 J','MC 22','MC 22 A','MC 22 C','MC 22 D','MC 22 E','MF 1','MF 1 A','EB 1','EB 21','EB 61','EB 81','EB 61 A', 'EB 1 A','EB 101','EB 61','ET 141 A','ET 161','LA 2','AG 1 A','PH 2','PH 2C','PH 2 A','GE 2','CM 1 C','CM 1 D','BS 1','BS 1 A','BF 1 ','FC 1','FC 1 A','CR 401','CR 401 A','CR 421','CR 441','CR 461','CR 122','CR 243','CR 202','CR 481','CR 501','CR 41 D','CR 21 D','CR 181 E','CR 82 A','CR 261 D','AS 351 C','AS 151 M','AS 151 L','AS 51 O','AS 601','AS 201 L','AS 351 F''AS 451 C','AS 251 L','AS 351 G','RN 2','LK 21','BC 121','ET 161','MC 22 E'])
 clone=str(clone)[2:-2]
col1,col2,col3,col4=st.columns(4)
with col1:
 used_LTD=st.multiselect("Used LTD", options=range(53))
 used_LTD=str(used_LTD)[1:-1]
with col2:
 used_stage = st.multiselect("Used stage",options= ("M", "M2", "S", "R", "INI","M3","MA","MN","MB"))
 used_stage=str(used_stage)[2:-2]
with col3:
 used_cultures=st.text_input("Used Cultures")
with col4:
 used_status=st.text_input("Used status")
col1,col2,col3,col4=st.columns(4)
with col1:
 produced_cultures=st.text_input("Produced cultures")
with col2:
 produced_stage=st.multiselect("Produced stage ",options= ("M","M2","S","R","INI","MA","MN","MB"))
 produced_stage = str(produced_stage)[2:-2]
with col3:
 operator=st.multiselect("Operator",options=operatordf)
 #operator=st.multiselect("Operator",options= ("NJK","SGS","ANJ","SKM","OMR","SST","ATH","SPS","SUM","SGN","AJN","ATH","ABA","BBA","CBA","DBA","EBA","FBA","GBA","HBA","JNI","SHN","IBA","JBA"))
 operator = str(operator)[2:-2]
with col4:
 produced_status=st.text_input("Produced status")
no_of_bottles=st.text_input("Number of bottles")
button1=st.button("Submit")
result_df= pd.DataFrame(data=[[date_input,type, crop, clone,used_LTD,used_stage,used_status,used_cultures,produced_cultures,produced_stage,produced_status,operator,no_of_bottles]],columns=["date","type", "crop", "clone","Used LTD","Used Stage","Used status","used cultures","produced cultures","produced stage","produced status","operator","no of bottles"])
result_df = result_df.astype(str)
gc=gc.open_by_key("13-Tdydp2MKEH8Fdcn65Q52pOJ9gRrMaCcjAu04MgU3Y")
sheet1 = gc.get_worksheet(0)
df = pd.DataFrame(data=sheet1.get_all_records())
if button1:
 sheet1.append_rows(values=result_df.values.tolist())
 st.write("Culture Details Entered Successfully")






