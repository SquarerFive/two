import os

context = ['Megascans', 'ThirdParty']
from shutil import copyfile
def for_context(context):
    for root, dirs, files in os.walk(f"../Content/{context}", topdown=False):
        for name in files:
            # Compare it with twoassets
            p = os.path.join(root, name)
            d= f"..\\twoassets\\{context}\\{name}"
            try:
                f1 =os.path.getctime(p) > os.path.getctime(d)
                if (f1):
                    print(f"[MODIFIED]: {p}")
                    copyfile(p,d)
            except:
                print(f"[NEW]: {p}")
                copyfile(p, d)
           
        
for c in context:
    for_context(c)
