class MatrixIterator:
    def __init__(self, matrix, mode):
        self.matrix = matrix
        self.mode = mode
        self.row_index = 0  # Индекс для строк
        self.col_index = 0  # Индекс для столбцов
        self.total_rows = len(matrix)
        self.total_cols = len(matrix[0]) if matrix else 0

        if mode == "row":
            self.max_iterations = self.total_rows * self.total_cols
        elif mode == "column":
            self.max_iterations = self.total_rows * self.total_cols
        else:
            raise ValueError("Invalid mode. Mode should be 'row' or 'column'.")

        self.current_iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iteration >= self.max_iterations:
            raise StopIteration

        if self.mode == "row":
            row = self.row_index
            col = self.col_index
            value = self.matrix[row][col]
            self.col_index += 1
            if self.col_index == self.total_cols:
                self.col_index = 0
                self.row_index += 1
        elif self.mode == "column":
            row = self.row_index
            col = self.col_index
            value = self.matrix[row][col]
            self.row_index += 1
            if self.row_index == self.total_rows:
                self.row_index = 0
                self.col_index += 1
        else:
            raise ValueError("Invalid mode. Mode should be 'row' or 'column'.")

        self.current_iteration += 1
        return value


# Пример использования
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Итерация по строкам
row_iter = MatrixIterator(matrix, mode="row")
for item in row_iter:
    print(item,end=' ')  # 1, 2, 3, 4, 5, 6, 7, 8, 9

print()  # Пустая строка для разделения вывода

# Итерация по столбцам
col_iter = MatrixIterator(matrix, mode="column")
for item in col_iter:
    print(item,end=' ')  # 1, 4, 7, 2, 5, 8, 3, 6, 9
