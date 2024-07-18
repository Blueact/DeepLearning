from matplotlib import pyplot as plt
import pandas as pd


def count_elements_in_columns(df):
    # 读取CSV文件

    # 创建一个字典来存储每个列的元素计数
    column_counts = {}

    # 遍历每一列
    for column in df.columns:
        # 使用value_counts()函数统计每个元素的出现次数
        counts = df[column].value_counts().sort_index().to_dict()
        column_counts[column] = counts

    return column_counts


def filter_data(data, column_to_get):
    keys_to_delete = []
    for key in data:
        if key not in column_to_get:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del data[key]
    return data


def get_column(data):
    column_to_get = []
    index = 0
    for key in data:
        if 150 > len(data[key]) > 2:
            column_to_get.append([index, key])
        index += 1
    print(column_to_get)
    return column_to_get


def age_sort(data):
    result = {}
    for age, count in data.items():
        if age < 0:
            key = 0
        elif age <= 10:
            key = 10
        elif age <= 20:
            key = 20
        elif age <= 30:
            key = 30
        elif age <= 40:
            key = 40
        elif age <= 50:
            key = 50
        elif age <= 60:
            key = 60
        elif age <= 70:
            key = 70
        elif age <= 80:
            key = 80
        elif age <= 90:
            key = 90
        elif age <= 100:
            key = 100
        elif age <= 110:
            key = 110
        else:
            key = 120
        if key not in result:
            result[key] = 0
        result[key] += count

    return result


data_dead = pd.read_csv('filtered_data_dead.csv')
data_alive = pd.read_csv('filtered_data_alive.csv')
result_dead = count_elements_in_columns(data_dead)
result_alive = count_elements_in_columns(data_alive)
column = list([i, j] for i, j in zip(range(len(data_dead.columns)), data_dead.columns))
for i in column:
    print(i)
column_filtered = get_column(result_alive)
column_get = []
for i in range(len(column_filtered)):
    column_get.append(column_filtered[i][1])
print(column_get)
data_get_dead = filter_data(result_alive, column_get)
data_get_alive = filter_data(result_dead, column_get)
dead_age_sorted = age_sort(data_get_dead['AGE'])
alive_age_sorted = age_sort(data_get_alive['AGE'])
print(dead_age_sorted)
print(alive_age_sorted)
total = len(data_dead) + len(data_alive)
print(total)
# 年龄数据
data1 = {key: value / total for key, value in dead_age_sorted.items()}
data2 = {key: value / total for key, value in alive_age_sorted.items()}
print(data1)
merged_data = {}
for key in data1:
    if key not in data2:
        data2[key] = 0
    merged_data[key] = (data1[key], data2[key])
print(merged_data)
values1 = [value[0] for value in merged_data.values()]
values2 = [value[1] for value in merged_data.values()]
print(values1)
print(values2)
fig, ax = plt.subplots()
bar_width = 1
opacity = 0.8
index = range(len(merged_data))
keys = list(merged_data.keys())
rects1_1 = plt.bar(index, values1, bar_width, alpha=opacity, color='b', label='dead')
rects1_2 = plt.bar(index, values2, bar_width, alpha=opacity, color='red', label='alive', bottom=values1)
plt.xlabel('AGE Group')
plt.ylabel('Proportion')
plt.title('Bar chart of Age impacting on death')
plt.xticks([i + bar_width / 2 for i in index], keys, rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig('./Age.png', dpi=200)
plt.show()