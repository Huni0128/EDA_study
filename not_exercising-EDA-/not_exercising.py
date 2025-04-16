import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family="NanumGothic")

class HealthDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)
        self.data = self.data.drop(columns="시점")
        self.data = self.data[self.data["대분류"]=="성별"]
        self.data = self.data.rename(columns={"합계": "운동을 할 충분한 시간이 없어서"})
        self.data = self.data.rename(columns={"합계.1": "함께 운동을 할 사람이 없어서"})
        self.data = self.data.set_index("분류")

    def get_data(self):
        return self.data

class HealthDataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_pie_chart(self, column, ax, title):
        self.data[column].plot.pie(explode=[0,0.02], ax=ax, autopct="%1.1f%%", textprops={"fontsize": 16, 'fontweight': 'bold'})
        ax.set_title(title, fontsize=20, fontweight='bold')
        ax.set_ylabel("")

    def visualize(self, save_path):
        fig, ax = plt.subplots(1, 2, figsize=(16, 8))
        self.plot_pie_chart("운동을 할 충분한 시간이 없어서", ax[0], "운동을 할 충분한 시간이 없어서")
        self.plot_pie_chart("함께 운동을 할 사람이 없어서", ax[1], "함께 운동을 할 사람이 없어서")
        plt.savefig(save_path)

health_data = HealthDataProcessor("./data/not_exercising.xlsx")
health_data.load_data()
data = health_data.get_data()

visualizer = HealthDataVisualizer(data)
visualizer.visualize("images/man_women.png")
