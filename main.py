import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ

def create_vector():
    return np.arange(10)
    
   
def create_matrix():
    return np.random.rand(5,5)

def reshape_vector(vec):
    return vec.reshape(2,5)


def transpose_matrix(mat):
    return np.transpose(mat)
    

# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ

def vector_add(a, b):
    return a + b;


def scalar_multiply(vec, scalar):
    return vec*scalar


def elementwise_multiply(a, b):
    return a*b;


def dot_product(a, b):
    return np.dot(a, b)


# 3. МАТРИЧНЫЕ ОПЕРАЦИИ

def matrix_multiply(a, b):
    return np.matmul(a, b);


def matrix_determinant(a):
    return np.linalg.det(a)


def matrix_inverse(a):
    return np.linalg.inv(a)


def solve_linear_system(a, b):
    return np.linalg.solve(a, b)


# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ

def load_dataset(path="data/students_scores.csv"):
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data):
     return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "percentile_25": np.percentile(data, 25),
        "percentile_75": np.percentile(data, 75)
    }


def normalize_data(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized = (data - min_val) / (max_val - min_val)
    return normalized

# 5. ВИЗУАЛИЗАЦИЯ

def plot_histogram(data):
    plt.hist(data, bins='auto', alpha = 0.7)
    plt.title('Распределение оценок по математике')
    plt.xlabel('Оценки')
    plt.ylabel('Частота')
    plt.savefig('plots/histogram.png')
    pass


def plot_heatmap(matrix):
    """
    Построить тепловую карту корреляции предметов.

    Изучить:
    https://seaborn.pydata.org/generated/seaborn.heatmap.html
    
    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """

    plt.figure(figsize=(8, 6)) 
    sns.heatmap(matrix, 
                annot=True,           # Show values in cells
                cmap='coolwarm',      # Color map suitable for correlations (-1 to 1)
                center=0,             # Center the colormap at 0
                square=True,          # Make cells square
                cbar_kws={"shrink": 0.8}) # Shrink colorbar
    
    plt.title('Тепловая карта корреляции предметов', fontsize=14)
    plt.tight_layout()
    plt.savefig('plots/heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.clf()

    pass


def plot_line(x, y):
    """
    Построить график зависимости: студент -> оценка по математике.

    Изучить:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    
    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    # Подсказка: используйте plt.plot(), добавьте заголовок, подписи осей,
    # сохраните график
    os.makedirs('plots', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'bo-')
    plt.title('Зависимость оценок студентов по математике')
    plt.xlabel('Номер студента')
    plt.ylabel('Оценка')
    plt.grid(True)
    
    plt.savefig('plots/student_scores.png')
    plt.show()
    plt.close()


