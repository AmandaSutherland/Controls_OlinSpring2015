import csv

import matplotlib.pyplot as plt
import numpy as np

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def get_csv_data(filename):
    with open('data/' + filename + '.csv', 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        csv_data = [row for row in datareader]
    csv_data = [[float(row[0]), translate(float(row[1]), 0, 255, 0, 5)] for row in csv_data]
    return csv_data


def plot_channel(data, label, channel=0, color_shape='bo'):
    for i in range(len(data)):
        plt.plot(i*0.25 , data[i][channel], color_shape)
    plt.plot(0, data[0][channel], color_shape, label=label)


def plot_dataset(data, title):
    plt.figure()
    plt.subplot(2,1,1)
    plot_channel(data, 'Thermistor Temperature (C)', 0, 'bo')
    plt.plot([0, 260], [40,40], 'r', label='Goal Temperature (40C)')
    plt.axis([0,250, 35,42])
    plt.legend(loc='lower center')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.title(title)

    plt.subplot(2,1,2)
    plot_channel(data, 'Output Voltage of Controller', 1, 'go')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend(loc=0)


def main():
    tests = {'ice_test': 'Ice Disturbance'}
            # 'test':'Test Data',
            #'roomT_to_goal': 'Running from No Input'
            #'above_roomT_to_goal': 'Running from Heated Environment'
            #'wind_test': 'Wind Disturbance'
            #'ice_test': 'Ice Disturbance'
    for dataset in tests.keys():
        print dataset
        data = get_csv_data(dataset)
        plot_dataset(data, tests[dataset])
    plt.show()


if __name__ == '__main__':
    main()