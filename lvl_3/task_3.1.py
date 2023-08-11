# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:

  def __init__(self, n, m):
    self.matrix = [[1 for j in range(m)] for i in range(n)]

  def setValues(self, n, m, arrs):
    for i in range(n):
      for j in range(m):
        self.matrix[i][j]=arrs[i][j]

  def __str__(self):
    strings = []
    for row in self.matrix:
        strings.append(str(row))
    return '\n'.join(strings)  
  
  def getElement(self, i, j):
    return self.matrix[i-1][j-1]
    
  def setElement(self, i, j, element):
    self.matrix[i-1][j-1] = element

  def getMatrixSize(self):
    n = len(self.matrix)
    m = len(self.matrix[0])
    return 'Размерность матрицы: '+str(n)+'*'+str(m)

  def addRow(self, row):
    self.matrix.append(row)

  def addColumn(self, column):
    for i in range(len(self.matrix)):
      self.matrix[i].append(column[i])

m2 = Matrix(2,3)
print(m2)  
m2.setValues(2,3,[[1,2,3],[4,5,6]])
print(m2)

m1 = Matrix(2,3)
print(m1)
print(m1.getElement(2,2))
m1.setElement(2,2,-10)
print(m1)
print(m1.getMatrixSize())
m1.addRow([2,3,4])
print(m1)
print(m1.getMatrixSize())
m1.addColumn([5,6,7])
print(m1)
print(m1.getMatrixSize())