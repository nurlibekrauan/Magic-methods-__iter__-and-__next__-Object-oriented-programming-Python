import os
os.chdir(r'D:\обучение\stepik 36')

class FileChunkIterator:
    def __init__(self, filename, chunk_size):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = open(self.filename, 'r')  # Открываем файл один раз при инициализации
    
    def __iter__(self):
        return self  # Возвращаем самого себя как итератор
    
    def __next__(self):
        chunk = self.file.read(self.chunk_size)  # Читаем очередной блок
        if not chunk:  # Если данных больше нет, закрываем файл и вызываем StopIteration
            self.file.close()
            raise StopIteration
        return chunk

# Пример использования
file_iter = FileChunkIterator("large_file.txt", chunk_size=135)

for i in file_iter:
    print(i)