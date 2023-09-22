"""
The purpose of this program is to calculate one-sided and two-sided 95% confidence interval.
The input of this program is the magnitude datas extracted from `gunnar_farnerback.py`.
The output of this program is a print out result of these confidence interval result.
"""

import scipy.stats as st
import numpy as np

file_path = 'magnitude_videos.txt'
column_index = 2

column_values = []

with open(file_path, 'r') as file:
    for line in file:
        columns = line.strip().split(',')

        if 0 <= column_index < len(columns):
            column_values.append(columns[column_index])

data = list(map(float, column_values[1:]))

confidence_level = 0.95
n = len(data)
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
margin_of_error = st.t.ppf((1 + confidence_level) / 2, n - 1) * (std_dev / np.sqrt(n))

lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

# Two-sided confidence interval
print(f'95% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})')

# One-sided confidence interval
std_error = st.sem(data)
upper_ci_bound = st.t.ppf(confidence_level, len(data) - 1) * std_error + mean
print("Upper Confidence Interval Bound:", upper_ci_bound)
lower_ci_bound = st.t.ppf(1 - confidence_level, len(data) - 1) * std_error + mean
print("Lower Confidence Interval Bound:", lower_ci_bound)

