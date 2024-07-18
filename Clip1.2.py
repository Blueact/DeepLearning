import pandas as pd


def remove_rows_with_value(data, target_value, filter_type):
    if type(target_value) is str:
        result = data.map(lambda x: x == target_value)
        has_target_value = result.any(axis=1)
        data_filtered = data[~has_target_value]
        data_filtered.to_csv(f'filtered_data_{filter_type}.csv', index=False)
        return data_filtered
    else:
        result = data.map(lambda x: x in target_value)
        has_target_value = result.any(axis=1)
        data_filtered = data[~has_target_value]
        data_filtered.to_csv(f'filtered_data_{filter_type}.csv', index=False)
        return data_filtered


def keep_rows_with_value(data, target_value, filter_type):
    if type(target_value) is str:
        result = data.map(lambda x: x == target_value)
        has_target_value = result.any(axis=1)
        data_filtered = data[has_target_value]
        return data_filtered
    else:
        result = data.map(lambda x: x in target_value)
        has_target_value = result.any(axis=1)
        data_filtered = data[has_target_value]
        data_filtered.to_csv(f'filtered_data_{filter_type}.csv', index=False)
        return data_filtered


def search_value(data):
    unique_values_with_index = {}
    for i in data.columns:
        unique_values = data[i].unique().tolist()
        unique_values_with_index[i] = unique_values

    for index, values in unique_values_with_index.items():
        print(f"{index}: {values}")


def check_value(data, column_name, column_value):
    for i in column_value:
        if i in data[column_name]:
            print('Error Age Clip')
            print('\n')
        else:
            print('AGE OK')
            print('\n')


def keep_column(data, column_name, column_value):
    for i in range(len(data)):
        if data.loc[i, column_name] in column_value:
            data.loc[i, column_name] = 10000 + data.loc[i, column_name]
    return data


def recover_column(data, column_name):
    data[column_name] = data[column_name].apply(lambda x: x - 10000 if x > 10000 else x)
    return data


file_path = 'C:\\DeepLearning\\Covid Data.csv'
data = pd.read_csv(file_path)
column = list([i, j] for i, j in zip(range(len(data.columns)), data.columns))
print(data.dtypes)
ls = []
flag = 0
for i in column:
    print(i)
    print(type(i[1]))
    if ' ' in i[1]:
        ls.append(i[0])
        flag = 1

if flag == 1:
    print("Exist space")
    delete = input("delete space?[y/n]")
    if delete == 'y':
        new_columns = [col.replace(' ', '') for col in data.columns]
        data.columns = new_columns
else:
    print('OK')
search_value(data)
print('\n')
column_name = 'AGE'
column_value = [97, 98, 99]
check_value(data, column_name, column_value)
for i in column_value:
    data[column_name] = data[column_name].replace(i, i+10000)
search_value(data)
wrong_value = 97
correct_value = 1
data.replace(wrong_value, correct_value, inplace=True)
search_value(data)

target_value = [98, 99]
filter_type = 'unknown&error'
data_removed = remove_rows_with_value(data, target_value, filter_type)
data_removed = recover_column(data_removed, column_name)
check_value(data_removed, column_name, column_value)
data_removed.to_csv(f'filtered_data_{filter_type}.csv', index=False)
target_value = '9999-99-99'
filter_type = 'dead'
data_alive = remove_rows_with_value(data_removed, target_value, filter_type)
filter_type = 'alive'
data_dead = keep_rows_with_value(data_removed, target_value, filter_type)
search_value(data_dead)
print('\n')
search_value(data_alive)
print(len(data))
print(len(data_removed))
print(len(data_alive))
print(len(data_dead))