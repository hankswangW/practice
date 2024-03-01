import csv
def check_month_ratios():
    data,data_list= read_months_for_analyse("V7",3,0.1)
    count_below_09 = 0
    count_09_to_095 = 0
    count_095_to_1 = 0
    count_1_to_105 = 0
    count_105_to_11 = 0
    count_above_11 = 0


    for item in data_list:
        if item < 0.9:
            count_below_09 += 1
        elif 0.9 <= item < 0.95:
            count_09_to_095 += 1
        elif 0.95 <= item < 1:
            count_095_to_1 += 1
        elif 1 <= item < 1.05:
            count_1_to_105 += 1
        elif 1.05 <= item < 1.1:
            count_105_to_11 += 1
        else:
            count_above_11 += 1


    average_value = sum(data_list) / len(data_list)
# 计算占比
    total_count = len(data_list)
    percentage_below_09 = (count_below_09 / total_count) * 100
    percentage_09_to_095 = (count_09_to_095 / total_count) * 100
    percentage_095_to_1 = (count_095_to_1 / total_count) * 100
    percentage_1_to_105 = (count_1_to_105 / total_count) * 100
    percentage_105_to_11 = (count_105_to_11 / total_count) * 100
    percentage_above_11 = (count_above_11 / total_count) * 100

# 写入 CSV 文件
    with open('ratios months statistics.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Range', 'Count', 'Percentage'])
        writer.writerow(['<0.9', count_below_09, percentage_below_09])
        writer.writerow(['0.9-0.95', count_09_to_095, percentage_09_to_095])
        writer.writerow(['0.95-1', count_095_to_1, percentage_095_to_1])
        writer.writerow(['1-1.05', count_1_to_105, percentage_1_to_105])
        writer.writerow(['1.05-1.1', count_105_to_11, percentage_105_to_11])
        writer.writerow(['>1.1', count_above_11, percentage_above_11])
        writer.writerow(['Average', '', average_value])
    print("统计结果已写入 statistics.csv 文件。")


def check_days_ratios():
    data,data_list= read_days_for_analyse("V7",3,0.1)
    count_below_09 = 0
    count_09_to_095 = 0
    count_095_to_1 = 0
    count_1_to_105 = 0
    count_105_to_11 = 0
    count_above_11 = 0


    for item in data_list:
        if item < 0.9:
            count_below_09 += 1
        elif 0.9 <= item < 0.95:
            count_09_to_095 += 1
        elif 0.95 <= item < 1:
            count_095_to_1 += 1
        elif 1 <= item < 1.05:
            count_1_to_105 += 1
        elif 1.05 <= item < 1.1:
            count_105_to_11 += 1
        else:
            count_above_11 += 1


    average_value = sum(data_list) / len(data_list)
# 计算占比
    total_count = len(data_list)
    percentage_below_09 = (count_below_09 / total_count) * 100
    percentage_09_to_095 = (count_09_to_095 / total_count) * 100
    percentage_095_to_1 = (count_095_to_1 / total_count) * 100
    percentage_1_to_105 = (count_1_to_105 / total_count) * 100
    percentage_105_to_11 = (count_105_to_11 / total_count) * 100
    percentage_above_11 = (count_above_11 / total_count) * 100

# 写入 CSV 文件
    with open('ratios statistics for days.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Range', 'Count', 'Percentage'])
        writer.writerow(['<0.9', count_below_09, percentage_below_09])
        writer.writerow(['0.9-0.95', count_09_to_095, percentage_09_to_095])
        writer.writerow(['0.95-1', count_095_to_1, percentage_095_to_1])
        writer.writerow(['1-1.05', count_1_to_105, percentage_1_to_105])
        writer.writerow(['1.05-1.1', count_105_to_11, percentage_105_to_11])
        writer.writerow(['>1.1', count_above_11, percentage_above_11])
        writer.writerow(['Average', '', average_value])
    print("统计结果已写入 statistics.csv 文件。")
    