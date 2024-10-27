class MultiGeneratorIterator:
    def __init__(self, generators: list):
        self.generators = generators
        self.current_gen = 0  # индекс текущего генератора

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_gen < len(self.generators):
            try:
                # Попытка извлечь следующий элемент из текущего генератора
                return next(self.generators[self.current_gen])
            except StopIteration:
                # Если генератор исчерпан, переходим к следующему
                self.current_gen += 1
                continue
        # Если все генераторы исчерпаны, завершаем итерацию
        raise StopIteration("All generators have been exhausted.")


# Пример использования
gen1 = (x for x in range(0, 9))
gen2 = (x for x in range(-3, 6))
multi_gen_iter = MultiGeneratorIterator([gen1, gen2])

for item in multi_gen_iter:
    print(item)  # 0, 1, 2, 3, 4, 5
