# Данный скрипт заимствован из ноутбука Соколова Павла

import os

edges_flag = True # True - по краям листа, False - по краям крайних полей
labels_path = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/labels/'
images_path = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/images/'

FIELDS = ["01 Receipt Number","04-01 Counterparty 1", "04-02 Counterparty 2",
        "05 Contract","06 Our Company BIN","07 Counterparty Bank BIC", "08 Counterparty Current Account IIC",
        "09 Counterparty Payment Purpose Code", "10 Items Table",
        "10-01 Item", "10-02 Unit","10-03 Quantity", "10-04 Price", "10-05 Amount" ]

def adjust_field_width(item_class, bbox_coordinates, edges_flag=False):
  # на входе: массив номеров классов, массив xyxy координат bb, ровняем по краям листа или нет
    item_class  = list(map(int,item_class))
    # print(item_class, len(item_class))
    if not edges_flag: # если ровняем по "09 Counterparty Payment Purpose Code", "10 Items Table", "04-01 Counterparty 1"
        try: # этих полей может не быть
            # поиск xmin и xmax
            x_mins = []
            x_maxs = []
            # print('До',bbox_coordinates)
            for i in range(len(item_class)): # делаем так, потому что может быть несколько полей одного класса
                if FIELDS[item_class[i]] in ["09 Counterparty Payment Purpose Code", "10 Items Table"]:
                    # print('max',FIELDS[i], bbox_coordinates[i][2])
                    x_maxs.append(bbox_coordinates[i][2])
                if FIELDS[item_class[i]] in ["04-01 Counterparty 1", "10 Items Table"]:
                    # print('min',FIELDS[i], bbox_coordinates[i][0])
                    x_mins.append(bbox_coordinates[i][0])
            x_min = min(x_mins)
            x_max = max(x_maxs)
        except:
            x_min = 0
            x_max = 1
    else: # если задаем изображение и ровняем по его краям (необходимо для определения правого края, нужна размерность)
        # img = cv2.imread(image_path)
        x_min = 0
        x_max = 1

    # ровняем нужные поля по x_min и x_max
    for i in range(len(item_class)):
        # print(i, item_class[i])
        if FIELDS[item_class[i]] in ["01 Receipt Number","04-02 Counterparty 2", "05 Contract","06 Our Company BIN"]:
            bbox_coordinates[i][0] = x_min
            bbox_coordinates[i][2] = x_max
    # print('После',bbox_coordinates)
    return bbox_coordinates # возращает новые скорректированные bbox для полей "01 Receipt Number","04-02 Counterparty 2", "05 Contract","06 Our Company BIN"

files_removed = [] # пустые файлы аннотаций
for label in sorted(os.listdir(labels_path)):
    print(label)
    label_path = os.path.join(labels_path, label)
    image_path = os.path.join(images_path, label[:-4] + '.png')

    with open(label_path, 'r') as f:
        class_coords_text = f.readlines()
    if class_coords_text:
        # считываем номера классов
        items_class = [line.split()[0] for line in class_coords_text]

        # считываем координаты xywh
        coords_xywh = [list(map(float,line.split()[1:])) for line in class_coords_text]

        # переводим xywh в xyxy
        coords_xyxy = [[x - w/2, y  - h/2, x + w/2, y  + h/2] for x,y,w,h in coords_xywh]

        # преобразовываем ширину нужных полей (по краям листа или по границам крайних полей) формат xyxy
        coords_xyxy_adj = adjust_field_width(items_class, coords_xyxy, edges_flag)

        # переводим преобразованные xyxy в xywh для дальнейшей подачи в yolo
        coords_xywh_adj = [[(x_max + x_min)/2, (y_max + y_min)/2, x_max - x_min, y_max - y_min] for x_min, y_min, x_max, y_max in  coords_xyxy_adj]

        # записываем в строки и далее в файл с аннотацией под тем же именем
        lines =''
        coords_xywh_adj_text = [list(map(str, coords)) for coords in coords_xywh_adj]
        for item_number in range(len(items_class)):
            lines += f'{items_class[item_number]} {" ".join(coords_xywh_adj_text[item_number])}\n'
        with open(label_path, 'w') as f:
            f.write(lines)
    else:
        os.remove(label_path)
        files_removed.append(label_path)
for label_path in files_removed:
    print(f'Файл {label_path} - пустой (удален)')