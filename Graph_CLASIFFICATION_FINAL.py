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
data_get_dead = filter_data(result_dead, column_get)
data_get_alive = filter_data(result_alive, column_get)
data1 = data_get_dead['CLASIFFICATION_FINAL']
data2 = data_get_alive['CLASIFFICATION_FINAL']
total = len(data_dead) + len(data_alive)
print(total)
print(data1)
print(data2)
merged_data = {}
for key in data1:
    if key not in data2:
        data2[key] = 0
    merged_data[key] = (data1[key], data2[key])
print(merged_data)
values1 = [value[0] / total for value in merged_data.values()]
values2 = [value[1] / total for value in merged_data.values()]
print(values1)
print(values2)
fig, ax = plt.subplots()
bar_width = 0.4
opacity = 0.8
index = range(len(merged_data))
keys = list(merged_data.keys())
rects1_1 = plt.bar(index, values1, bar_width, alpha=opacity, color='b', label='dead')
rects2_1 = plt.bar([i + bar_width for i in index], values2, bar_width, alpha=opacity, color='g', label='alive')
plt.xlabel('CLASIFFICATION_FINAL Group')
plt.ylabel('Proportion')
plt.title('Bar chart of CLASIFFICATION_FINAL impacting on death')
plt.xticks([i + bar_width / 2 for i in index], keys, rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig('./CLASIFFICATION_FINAL.png', dpi=200)
plt.show()