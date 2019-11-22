
import pandas as pd
import numpy as np

dataset = \
    """色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
    青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
    乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
    乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
    青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
    浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
    青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
    乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
    乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
    乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
    青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
    浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
    浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
    青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
    浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
    乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
    浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
    青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

# write into a file
# your code here
lines = dataset.split("\n")
lines = list(map(lambda line_num, line:
                 (("编号," + line.lstrip().replace(" ", ",")) if line_num == 0
                  else (str(line_num) + "," + line.lstrip().replace(" ", ","))) + "\n", range(lines.__len__()), lines))
file = r'machine_learning.csv'  # file path, you can change the direction
with open(file, "w") as f:
    f.writelines(lines)

# add a new data
# your code here
df = pd.read_csv(file)
new_line = np.array([[len(lines), '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '好']])
df = pd.DataFrame(new_line, columns=df.columns.tolist())
df.to_csv(r'./machine_learning.csv', mode='a', index=False, header=False)

# vertify
df = pd.read_csv(file, dtype=str)
print(df.head())

# read file
# your code here
# 普通文件读取
columns = []
datalist = []
with open(file, "r") as f:
    lines = f.readlines()
columns = lines[0].strip().split(',')
for line in lines[1:]:
    datalist.append(line.strip().split(","))

# csv读取
# columns = df.columns.tolist()
# datalist = df.values[:, 1:].tolist()
# print(datalist)


# vertify
print(columns == ['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1] == ['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '好'])

# your code here
data_white = [data for data in datalist if (data[1] == '浅白')]
data_beyond_zero_point_five = [data for data in datalist if (float(data[7]) > 0.5)]
print("浅白")
print(data_white, "  ", len(data_white))
print(">0.5")
print(data_beyond_zero_point_five, "  ", len(data_beyond_zero_point_five))
