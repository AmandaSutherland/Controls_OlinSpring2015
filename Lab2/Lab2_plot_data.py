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
    csv_data = [[float(row[0]), translate(float(row[2]), 0, 1024, 0, 5), float(row[3])] for row in csv_data]
    return csv_data

def current_math(data1, data2, data3):
    Vd = 5 
    Vm = data2
    R = 15
    currents = []
    for i in range(len(data2)):
        Vm_i = 3.75
        average_current = ((Vd - Vm_i)/R)
        current = ((Vd - Vm[i])/R)
        switched_current = (data3[i]*(current-average_current)) + average_current 
        currents.append(switched_current)
    return data1, currents

def plot_channel(data, label, channel=0, channel2=1, channel3=2, color_shape='b-'):
    data1 = [d[channel] for d in data]
    data2 = [d[channel2] for d in data]
    data3 = [d[channel3] for d in data]
    data1,data3 = current_math(data1,data2,data3)
    plt.figure()
    plt.plot(data1, data3, color_shape, label=label)
    plt.xlabel('Time (s)')
    plt.ylabel('Current (amps)')
    plt.title('Driving Motor with Constant DC Voltage (8V)')

def main():
    tests = {'Part2_1_8V': 'Driving motor with constant DC voltage - 8V'}
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
        plot_channel(data, tests[dataset])
    plt.show()


if __name__ == '__main__':
    main()