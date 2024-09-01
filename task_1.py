# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории.Результаты обхода сохраните в
# файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import csv
import json
import os
import pickle
from pathlib import Path

import os
import json
import csv
import pickle


def get_size(directory):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(directory):
        for filename in file_name:
            filepath = os.path.join(dir_path, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def collection(files_path):
    data = []
    for dir_path, dir_name, file_name in os.walk(files_path):
        for name in dir_name:
            little_path = os.path.join(dir_path, name)
            size = get_size(little_path)
            data.append({
                'name': name,
                'type': 'directory',
                'parent_directory': dir_path,
                'size': size
            })
        for name in file_name:
            filepath = os.path.join(dir_path, name)
            size = os.path.getsize(filepath)
            data.append({
                'name': name,
                'type': 'file',
                'parent_directory': dir_path,
                'size': size
            })

    # Запись данных в файлы разных форматов
    with open('directory_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    with open('directory_data.csv', 'w', newline='') as csv_file:
        fieldnames = ['name', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    with open('directory_data.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

# Пример использования:
# collection('путь_к_вашему_каталогу')