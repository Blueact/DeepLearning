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


def filter_long_data(data):
    keys_to_delete = []
    for key in data:
        if  len(data[key]) ==2:
            print(key)
            for inner_key in data[key]:
                print(inner_key, data[key][inner_key])
        else:
            keys_to_delete.append(key)
        print('\n')
    for key in keys_to_delete:
        del data[key]
    return data


data_dead = pd.read_csv('filtered_data_dead.csv')
data_alive = pd.read_csv('filtered_data_alive.csv')
column = list([i, j] for i, j in zip(range(len(data_dead.columns)), data_dead.columns))
for i in column:
    print(i)
result_dead = count_elements_in_columns(data_dead)
result_alive = count_elements_in_columns(data_alive)
result_dead = filter_long_data(result_dead)
result_alive = filter_long_data(result_alive)
l_ = 0
for key in result_dead:
    l_ += len(result_dead[key])
print(l_)
l_ = 0
for key in result_dead:
    l_ += len(result_alive[key])
print(l_)
name = []
for key in result_dead:
    name.append(key)
print(name)
print(len(name))
data1 = {
    'USMER': [323473, 622742],
    'SEX': [482915, 463300],
    'PATIENT_TYPE': [823623, 122592],
    'INTUBED': [830675, 115540],
    'PNEUMONIA': [84295, 861920],
    'PREGNANT': [471048, 475167],
    'DIABETES': [94356, 851859],
    'COPD': [10446, 935769],
    'ASTHMA': [28940, 917275],
    'INMSUPR': [11046, 935169],
    'HIPERTENSION': [127632, 818583],
    'OTHER_DISEASE': [22623, 923592],
    'CARDIOVASCULAR': [15755, 930460],
    'OBESITY': [139572, 806643],
    'RENAL_CHRONIC': [12734, 933481],
    'TOBACCO': [76023, 870192],
    'ICU': [832088, 114127]
}
total_1 = 323473 + 622742
data1 = {key: [value / total_1 for value in values] for key, values in data1.items()}
data2 = {
    'USMER': [41065, 32245],
    'SEX': [26074, 47236],
    'PATIENT_TYPE': [6672, 66638],
    'INTUBED': [32555, 40755],
    'PNEUMONIA': [52087, 21223],
    'PREGNANT': [47316, 25994],
    'DIABETES': [27150, 46160],
    'COPD': [3797, 69513],
    'ASTHMA': [1389, 71921],
    'INMSUPR': [2472, 70838],
    'HIPERTENSION': [30779, 42531],
    'OTHER_DISEASE': [4361, 68949],
    'CARDIOVASCULAR': [4219, 69091],
    'OBESITY': [16474, 56836],
    'RENAL_CHRONIC': [5481, 67829],
    'TOBACCO': [6325, 66985],
    'ICU': [14613, 58697]
}
total_2 = 41065 + 32245
data2 = {key: [value / total_2 for value in values] for key, values in data2.items()}
print(data1)
print(data2)
merged_data = {}
for key in data1:
    merged_data[key] = (data1[key], data2[key])
print(merged_data)
values1 = [value[0] for value in merged_data.values()]
values2 = [value[1] for value in merged_data.values()]
print(values1)
print(values2)
values1_1 = [values1[i][0] for i in range(len(values1))]
values1_2 = [values1[i][1] for i in range(len(values1))]
values2_1 = [values2[i][0] for i in range(len(values2))]
values2_2 = [values2[i][1] for i in range(len(values2))]
print(values1_1)
print(values1_2)
fig, ax = plt.subplots()
bar_width = 0.35
opacity = 0.8
index = range(len(merged_data))
keys = list(merged_data.keys())
rects1_1 = plt.bar(index, values1_1, bar_width, alpha=opacity, color='b', label='alive_1')
rects1_2 = plt.bar(index, values1_2, bar_width, alpha=opacity, color='orange', label='alive_2', bottom=values1_1)
rects2_1 = plt.bar([i + bar_width for i in index], values2_1, bar_width, alpha=opacity, color='g', label='dead_1')
rects2_2 = plt.bar([i + bar_width for i in index], values2_2, bar_width, alpha=opacity, color='red', label='dead_2', bottom=values2_1)
plt.xlabel('Features')
plt.ylabel('Values')
plt.title('Bar chart of features')
plt.xticks([i + bar_width / 2 for i in index], keys, rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig('./distribution_1,2.png',dpi=200)
plt.show()
