# I do: Select file type (Received_or_Disclosure) and modify date of a target zip folder for unzipped files
###################################################################
# partner = 'Kansas HIN'
# OID = '2.16.840.1.113883.3.432.0.16.500'
# Received_or_Disclosure = "Received"; # type Received or Disclosure
# month="06";day="01";year="2022"; # Select month, day, and year

# output_path = r"Z:\CDW\Team-Member\Aziz-Work-Folder\HIMSS Data\ICA\Kansas HIN XML"
###################################################################


from datetime import datetime
start=datetime.now()
# USENT do:
import pandas as pd;import numpy as np;import glob;import os;import zipfile; import re
#Received_or_Disclosure = "Received"; # type Received or Disclosure
#month="01";day="06";year="2022"; # Select month, day, and year
pd.options.display.max_colwidth = 100; R_D=Received_or_Disclosure
date=year+month+day; ym=year+month; f_type=" sample files" ; 
CDW_path = "Z:/CDW/";loinc = "34133-9"; 
target_path=CDW_path+date+ f_type;
unzip_folder = "UnzipFolder_"+R_D+"/"
# output_path =CDW_path+unzip_folder+ym+"-"+loinc+" "+R_D+"/"+ date +"_" +loinc + "_Mann"
csvpath="*Patient"+R_D+"CCDA.csv";z_path = "*Patient"+R_D+"CCDA.zip"
zip_path=glob.glob(os.path.join(CDW_path,target_path, z_path))

# zip_path
dz=pd.DataFrame(zip_path);dz.columns=["path"];dz.reset_index(inplace=True)
# dz
# dz['index']=dz['index'].astype(str)
path0=(dz.iloc[0,].to_string(index=False))[2:] if 0 in dz.index else []
path1=(dz.iloc[1,].to_string(index=False))[2:] if 1 in dz.index else []
path2=(dz.iloc[2,].to_string(index=False))[2:] if 2 in dz.index else []
path3=(dz.iloc[3,].to_string(index=False))[2:] if 3 in dz.index else []
path4=(dz.iloc[4,].to_string(index=False))[2:] if 4 in dz.index else []
path5=(dz.iloc[5,].to_string(index=False))[2:] if 5 in dz.index else []

# print(path0)

pattern = ".*" + "\n"

path0 = re.sub(pattern, '', path0.strip())
path1 = re.sub(pattern, '', path1.strip())
path2 = re.sub(pattern, '', path2.strip())
path3 = re.sub(pattern, '', path3.strip())
path4 = re.sub(pattern, '', path4.strip())
path5 = re.sub(pattern, '', path5.strip())
# print(path0)

# USENT do:
all_data=pd.DataFrame()
df=[]
for f in glob.glob(os.path.join(target_path, csvpath)):
    df_z=pd.read_csv(f,  error_bad_lines=False)
    df.append(df_z)
df=pd.concat(df,ignore_index=True)
# df1=df[(df["Document_LOINC_Code"]=='34133-9') & (df.Sending_Organization.str.contains(parntner, case=False, na=False))]
# df1.shape
df1=df[(df["Document_LOINC_Code"]=='34133-9') & (df.Source_ID.str.contains(OID, case=False, na=False))]
# df1=df[(df["Document_LOINC_Code"]=='34133-9')]
df1.shape



nd=pd.DataFrame(df1, columns=['CCDA_File_Name']).drop_duplicates( keep='first')
nd.shape
c_list=np.array(nd['CCDA_File_Name'].unique()).tolist()
len(c_list)

csv_list = [i for i in c_list if i in c_list]
len(csv_list)
percent= np.round( len(csv_list)/len(df) *100, decimals=2)
percent


print("")
print("(1) ", R_D,"CDW xml files: ",target_path)
print("")
print("(2) ","Output Path",output_path)
print("")
print("(3) ","Total # of xml_files = {:,}" .format(len(df))) 
print("")
print("(4) ","Total # of Summary of Episode Note files = {:,}" .format(len(csv_list)))
print("")
print("")
print("(5) ","Percent of Summary of Episode Note files in the folder/path =", percent, "%")
print("")
print("")


with zipfile.ZipFile(path0) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
with zipfile.ZipFile(path1) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
with zipfile.ZipFile(path2) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
with zipfile.ZipFile(path3) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
with zipfile.ZipFile(path4) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
with zipfile.ZipFile(path5) as z:
    for item in (f for f in z.filelist if f.filename in set(csv_list)):
        z.extract(item.filename, output_path)
        
print ("run time: hour:min:sec= ", datetime.now() - start)  

