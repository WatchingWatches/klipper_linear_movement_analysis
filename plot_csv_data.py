import os
import csv
import glob
import numpy as np
from enum import Enum
from dataclasses import dataclass
from matplotlib import pyplot as plt


class Plot_Mode(Enum):
    relative_power = 1
    #frequency_range = 2

    def __str__(self):
        return self.name + "_csv"
    
MODE: Plot_Mode = Plot_Mode.relative_power

@dataclass
class relative_power_data:
    velocity = []
    power = []
    axis = ''

def read_csv_data(name_type: str)-> list:
    data = []
    for filename in glob.glob(os.path.join(os.getcwd(),'csv_files/', f"{name_type}*.csv")):
        with open(filename, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            rows = []
            for row in csvreader:
                rows.append(row)
            data.append(rows)

    return data

def plot_relative_power(data):
    plt.ioff()
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlabel("velocity in mm/s")
    plt.ylabel("relative power")
    velocities = [float(row['velocity']) for row in data[1]]
    relative_powers = []
    for index in range(len(velocities)):
        values = 0
        for file in data:
            values += float(file[index]['relative_power'])
        relative_powers.append(values)

    axis = ''
    for file in data:
        axis += str(file[0]['axis'])

    plt.title("Vibration power for axis {}".format(axis))
    plt.plot(velocities, relative_powers, marker='o', label="measurement data")
    plt.show()
    plt.savefig("relative_power.png")
    plt.close('all')

if __name__ == '__main__':
    if MODE == Plot_Mode.relative_power:
        data = read_csv_data(str(MODE))
        plot_relative_power(data)