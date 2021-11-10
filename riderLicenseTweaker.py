import os
import admin
if not admin.isUserAdmin():
    admin.runAsAdmin()
    sys.exit(0)
rider_dir=os.path.join(os.environ["appdata"],"JetBrains")
rider_path=None
for i in os.listdir(rider_dir):
    if "Rider" in i:
        rider_path=os.path.join(rider_dir,i)
        break

a=open(os.path.join(rider_path,"options","other.xml"))
b=a.readlines()
c=[]
for i in b:
    if '<property name="evl' not in i:
        c.append(i)
a=open(os.path.join(rider_path,"options","other.xml"),"w")
a.write("".join(c))
try:
    os.system("rmdir /S /Q "+os.path.join(rider_path,"eval"))
except Exception as e:print(repr(e))
os.system(r"reg delete Computer\HKEY_CURRENT_USER\SOFTWARE\JavaSoft\Prefs\jetbrains\rider")
