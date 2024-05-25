import numpy as np
from scipy.stats import ttest_ind

chat_id = 886180056  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:  # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    statistic, p_value = ttest_ind(x, y)
    alpha = 0.09
    return p_value < alpha
