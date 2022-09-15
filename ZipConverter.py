import os
import zipfile
import time
from pathlib import Path

source = Path(os.getcwd()) #путь к конвертируемой папке
copy_path = 'C:\\Users\\ukeuk\Desktop\\' + time.strftime('%d.%m') + '\\' #путь где будет хранится zip файл

files = list(map(str,[file for file in source.rglob("*")])) #добавили в список все пути к файлам

files = [i.rpartition("\\")[-1] for i in files] #обрезали до названия

if not os.path.exists(copy_path): #проверяем существует ли такой путь,если нет,создаём
        os.mkdir(copy_path)
        print('Каталог создан: ', copy_path)

for file in files: #создаём zip-копию файла
        with zipfile.ZipFile(copy_path + time.strftime('%d.%m') + '.zip', mode='a', \
                                compression=zipfile.ZIP_DEFLATED) as zf:
                zf.write(file)
print('КОПИЯ СОЗДАНА УСПЕШНО',copy_path)


