import pandas as pd
import matplotlib.pyplot as plt

# Пути к файлам 'results.csv' модели каждого размера (нано, маленькая, средняя)
path_n = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/train24/nano_results.csv'
path_s = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/train25/results.csv'
path_m = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/train26/results.csv'


# Файлы CSV считываются в датафреймы
df1 = pd.read_csv(path_n)
df2 = pd.read_csv(path_s)
df3 = pd.read_csv(path_m)

# При условии, что названия столбцов во всех датафреймах одинаковые, переичисляем столбцы для графиков
columns_to_plot = ['   metrics/precision(B)', '      metrics/recall(B)', '       metrics/mAP50(B)', '    metrics/mAP50-95(B)']
# Для корректного перечисления названий столбцов выводим их точные написания через df.columns
# Index(['                  epoch', '         train/box_loss',
#        '         train/cls_loss', '         train/dfl_loss',
#        '   metrics/precesion(B)', '      metrics/recall(B)',
#        '       metrics/mAP50(B)', '    metrics/mAP50-95(B)',
#        '           val/box_loss', '           val/cls_loss',
#        '           val/dfl_loss', '                 lr/pg0',
#        '                 lr/pg1', '                 lr/pg2'],

# Создаются сравнительные графики для каждой модели по вышеперечисленным метрикам (столбца)
for column in columns_to_plot:
    plt.figure(figsize=(10, 6))
    plt.plot(df1[column], label='Nano')
    plt.plot(df2[column], label='Small')
    plt.plot(df3[column], label='Medium')
   
    plt.title(f'Comparative Analysis of {column}')
    plt.xlabel('Epochs')
    plt.ylabel('%%')

    plt.legend()
    plt.show()
