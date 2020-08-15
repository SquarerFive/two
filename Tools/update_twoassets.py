import os

context = ['Megascans', 'ThirdParty']
from shutil import copyfile
def for_context(context):
    for root, dirs, files in os.walk(f"../Content/{context}", topdown=False):
        for name in files:
            # Compare it with twoassets
            p = os.path.join(root, name)
            newPath = p.split("/")[2].split("\\")[1:]
            newPath = '/'.join(newPath)
            print(newPath)
            #newPath = p.strip(f"../Content/{context}")
            #print(newPath)

            d= f"..\\twoassets\\{context}\\{newPath}"
            try:
                f1 =os.path.getctime(p) > os.path.getctime(d)
                if (f1):
                    os.makedirs(os.path.dirname(d), exist_ok=True)
                    print(f"[MODIFIED]: {p}", "New Path:", d)
                    copyfile(p,d)
            except:
                os.makedirs(os.path.dirname(d), exist_ok=True)
                print(f"[NEW]: {p}", d)
                copyfile(p, d)
           
        
for c in context:
    for_context(c)
