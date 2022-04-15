import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import NUM_DATA_POINTS

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time'][-NUM_DATA_POINTS:]
    # y1 = data['total_1'][-100:]
    y2 = data['LC'][-NUM_DATA_POINTS:]

    plt.cla()

    # plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='LC')
    plt.title('Load Cell')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=40)

plt.tight_layout()
plt.show()