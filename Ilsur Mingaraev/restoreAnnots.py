# from google.colab import drive
# drive.mount('/content/drive')

import os, shutil
import json


#  создать каталог, если он не существует
def checkDirExists(path):
    if not os.path.exists(path):
            # print("mk:",path)
            os.mkdir(path)

def points2yolo( points):
    dx = points[2] - points[0] 
    dy = points[3] - points[1] 
    
    xmin, ymin = points[0] + dx/2 , points[1] + dy/2
    return xmin, ymin, dx, dy

# get this 2 params from  args?
JSON_SRC  = "data/back.orig/annotations.json"   # json file from backup 
DEST_PATH = "obj_train_data"
START_NUM = 700
# TODO get real width and height for EACH frame (they msay be different!) 
WIDTH=2480
HEIGHT =3508

FIELDS = ["01 Receipt Number","04-01 Counterparty 1", "04-02 Counterparty 2",
        "05 Contract","06 Our Company BIN","07 Counterparty Bank BIC", "08 Counterparty Current Account IIC",
        "09 Counterparty Payment Purpose Code", "10 Items Table",
        "10-01 Item", "10-02 Unit","10-03 Quantity", "10-04 Price", "10-05 Amount" ]

Changes = { "03 Counterparty BIN" :"04-01 Counterparty 1",
            "04 Counterparty Name":"04-02 Counterparty 2"          
          }
if not os.path.exists(JSON_SRC):
  print(f'Input file {JSON_SRC} is not exists')
  quit(-2)

checkDirExists(DEST_PATH)

fin = open(JSON_SRC)
 
# returns JSON object as 
data = json.load(fin)
fin.close()
 
# Iterating through the json
# list
# print (type(data))
# print (data[0])
data = data[0]   #there was only one item = is it always?
# print (len(data['shapes'])) #1388  - about 14*100 -not all labels are exist on each frame
curFrame =-1
for shape in data['shapes']:
  # if(shape.frame )
  frm = int(shape.get("frame"))
  if(frm != curFrame):
    if(curFrame != -1):
      of.close
    of=open(DEST_PATH+'/0'+ str(START_NUM +frm)+'.txt', 'wt', encoding='utf-8') # open new annotation file
    curFrame =frm
    
  lbl = shape.get('label')
  if(Changes.__contains__(lbl)):
    lbl = Changes[lbl]
  indx = FIELDS.index(lbl)
  if(indx < 0):
    print(curFrame,"unknown label:", lbl)  
    continue
  pnts = shape.get('points')
  print (type(pnts), pnts)
  xmin, ymin, dx, dy = points2yolo(pnts)
  xmin/=WIDTH
  dx /= WIDTH
  ymin /= HEIGHT
  dy   /= HEIGHT
  #of.write(str(indx))
  # print("Меня зовут %s. Мне %d лет." % (name, age))
# >>> Меня зовут Дмитрий. Мне 25 лет.
  outs = '%d %f %f %f %f\n'%(indx, xmin, ymin,  dx, dy)
  # of.write (format('{indx}  {xmin} {ymin}  {dx} {dy}\n'))
  of.write (outs)
  
# Closing file
of.close()

