import os
import random
import shutil

# Путь к папке с исходными файлами. Если вы на Windows необходимо экранировать слэши в пути к папке. 
source_folder = 'E:\\Coding\\NU\\Stazhirovka_Qazaq\\data\\Scans'

# Путь к папке назначения для 200 случайно выбранных файлов
destination_folder = 'E:\\Coding\\NU\\Stazhirovka_Qazaq\\data\\random_200'

# Создаём список всех файлов из исходной папки
files = os.listdir(source_folder)

# Перемешаем случайным образом файлы в исходном списке
random.shuffle(files)

# Выбираем первые 200 файлов из перемешанного списка
selected_files = files[:200]

# Циклом проходим по каждому из выбранных файлов и сохраняем их в папку назначения
for file in selected_files:
    source_file = os.path.join(source_folder, file)
    destination_file = os.path.join(destination_folder, file)
    shutil.copy2(source_file, destination_file)

print("Файлы успешно скопированы.")
