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
    tests = {'touch_test': 'Ice Disturbance'}
            # 'Part1_1': 'Driving motor with constant DC voltage'
            # 'Part1_2_1': 'Driving with constant (DC) voltage - 1 V'
            # 'Part1_2_2': 'Driving with constant (DC) voltage - 1.5 V'
            # 'Part1_2_3': 'Driving with constant (DC) voltage - 2 V'
            # 'Part1_2_4': 'Driving with constant (DC) voltage - 2.5 V'
            # 'Part1_2_5': 'Driving with constant (DC) voltage - 3 V'
            # 'Part1_3_1': 'Driving motor with square wave - 0.15 A'
            # 'Part1_3_2': 'Driving motor with square wave - 0.3 A'
            # 'Part1_3_3': 'Driving motor with square wave - 0.45 A'
            # 'Part1_3_4': 'Driving motor with square wave - 0.6 A'
            # 'Part1_3_5': 'Driving motor with square wave - 0.75 A'
            # 'Part2_1_1': 'Driving motor with slow square wave - 1 V'
            # 'Part2_1_2': 'Driving motor with slow square wave - 1.5 V'
            # 'Part2_1_3': 'Driving motor with slow square wave - 2 V'
            # 'Part2_1_4': 'Driving motor with slow square wave - 2.5 V'
            # 'Part2_1_5': 'Driving motor with slow square wave - 3 V'
            # 'Part3_3_1': 'Driving motor with square wave - 0.15 A'
            # 'Part3_3_2': 'Driving motor with square wave - 0.3 A'
            # 'Part3_3_3': 'Driving motor with square wave - 0.45 A'
            # 'Part3_3_4': 'Driving motor with square wave - 0.6 A'
            # 'Part3_3_5': 'Driving motor with square wave - 0.75 A'
    for dataset in tests.keys():
        print dataset
        data = get_csv_data(dataset)
        plot_dataset(data, tests[dataset])
    plt.show()


if __name__ == '__main__':
    main()