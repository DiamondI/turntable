import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import json


def get_data():
    """
    data.json 中是一个列表，其中写了各种物品
    """
    with open("data.json", "r", encoding="utf-8") as rf:
        data = json.load(rf)
    return data

# 设置字体为行楷
font_manager.fontManager.addfont("fonts/Xingkai SC/Xingkai.ttc")
plt.rcParams['font.sans-serif'] = ['Xingkai SC']

x_tail = 0
y_tail = 2
dx = 0
dy = -1

def draw_pie_chart():
    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")

    raw_data = get_data()
    data = {i: 1 / len(raw_data) for i in raw_data}

    circle = mpatches.Circle((0, 0), 0.1, ec="lightcoral", color="maroon", zorder=100)
    ax.add_patch(circle)

    ax.pie(data.values(), labels=data.keys(), radius=1, textprops={'fontsize':20}, wedgeprops=dict(linewidth=1, edgecolor='w'))

    fig.savefig("images/pie.png")
    # plt.show()


if __name__ == "__main__":
    draw_pie_chart()