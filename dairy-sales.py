import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import stdev
from statistics import mean
from statistics import variance


def main():
    user_input = int(input("What period sales do you want to see?"))
    if user_input == 8:
        period_8()
    elif user_input == 9:
        period_9()
    elif user_input == 10:
        period_10()
    elif user_input == 11:
        period_11()
    else:
        print("Invalid Input")
        main()


def period_8():
    days = 7
    ind = np.arange(days)

    week_1 = (1660.08, 815.42, 806.09, 1131.10, 804.39, 874.19, 1488.50)
    week_2 = (1573.14, 1062.79, 1000.42, 1017.26, 2218.39, 657.99, 1009.80)
    week_3 = (2552.43, 1502.99, 851.82, 1171.10, 721.15, 957.58, 1012.95)
    week_4 = (1310.32, 1226.90, 867.07, 1054.50, 703.62, 832.35, 1142.31)

    plt.plot(week_1, 'g-', label='Week 1')
    plt.plot(week_2, 'b-', label='Week 2')
    plt.plot(week_3, 'r-.', label='Week 3')
    plt.plot(week_4, 'c:', label='Week 4')

    plt.legend()
    plt.ylabel('Sales')
    plt.title('Period 8 Dairy Sales')
    plt.xticks(ind, ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
    print('The mean of Week 1 is', mean(week_1))
    print('The standard deviation of Week 1 is', stdev(week_1, xbar=None))
    print('The variance of Week 1 is', variance(week_1, xbar=None))
    print('The mean of Week 2 is', mean(week_2))
    print('The standard deviation of Week 2 is', stdev(week_2, xbar=None))
    print('The variance of Week 2 is', variance(week_2, xbar=None))
    print('The mean of Week 3 is', mean(week_3))
    print('The standard deviation of Week 3 is', stdev(week_3, xbar=None))
    print('The variance of Week 3 is', variance(week_3, xbar=None))
    print('The mean of Week 4 is', mean(week_4))
    print('The standard deviation of Week 4 is', stdev(week_4, xbar=None))
    print('The variance of Week 4 is', variance(week_4, xbar=None))
    plt.show()


def period_9():
    days = 7
    ind = np.arange(days)

    week_1 = (1416.52, 987.04, 766.67, 939.28, 637.45, 839.00, 1107.03)
    week_2 = (1532.97, 1109.48, 804.79, 1005.38, 749.81, 770.97, 1001.74)
    week_3 = (1689.57, 836.91, 620.83, 1028.74, 788.34, 716.40, 1291.59)
    week_4 = (1504.97, 870.39, 623.03, 893.39, 645.67, 750.66, 1054.17)

    plt.plot(week_1, 'g-', label='Week 1')
    plt.plot(week_2, 'b-', label='Week 2')
    plt.plot(week_3, 'r-.', label='Week 3')
    plt.plot(week_4, 'c:', label='Week 4')

    plt.legend()
    plt.ylabel('Sales')
    plt.title('Period 9 Dairy Sales')
    plt.xticks(ind, ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
    print('The mean of Week 1 is', mean(week_1))
    print('The standard deviation of Week 1 is', stdev(week_1, xbar=None))
    print('The variance of Week 1 is', variance(week_1, xbar=None))
    print('The mean of Week 2 is', mean(week_2))
    print('The standard deviation of Week 2 is', stdev(week_2, xbar=None))
    print('The variance of Week 2 is', variance(week_2, xbar=None))
    print('The mean of Week 3 is', mean(week_3))
    print('The standard deviation of Week 3 is', stdev(week_3, xbar=None))
    print('The variance of Week 3 is', variance(week_3, xbar=None))
    print('The mean of Week 4 is', mean(week_4))
    print('The standard deviation of Week 4 is', stdev(week_4, xbar=None))
    print('The variance of Week 4 is', variance(week_4, xbar=None))
    plt.show()


def period_10():
    days = 7
    ind = np.arange(days)

    week_1 = (1298.71, 944.91, 803.82, 945.77, 735.17, 923.98, 1239.39)
    week_2 = (1595.54, 891.91, 829.91, 964.65, 904.25, 568.68, 1125.20)
    week_3 = (1808.71, 1018.22, 778.58, 767.82, 652.53, 830.30, 1134.60)
    week_4 = (1523.49, 970.34, 835.86, 1207.03, 676.53, 693.96, 1132.16)

    plt.plot(week_1, 'g-', label='Week 1')
    plt.plot(week_2, 'b-', label='Week 2')
    plt.plot(week_3, 'r-.', label='Week 3')
    plt.plot(week_4, 'c:', label='Week 4')

    plt.legend()
    plt.ylabel('Sales')
    plt.title('Period 10 Dairy Sales')
    plt.xticks(ind, ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
    print('The mean of Week 1 is', mean(week_1))
    print('The standard deviation of Week 1 is', stdev(week_1, xbar=None))
    print('The variance of Week 1 is', variance(week_1, xbar=None))
    print('The mean of Week 2 is', mean(week_2))
    print('The standard deviation of Week 2 is', stdev(week_2, xbar=None))
    print('The variance of Week 2 is', variance(week_2, xbar=None))
    print('The mean of Week 3 is', mean(week_3))
    print('The standard deviation of Week 3 is', stdev(week_3, xbar=None))
    print('The variance of Week 3 is', variance(week_3, xbar=None))
    print('The mean of Week 4 is', mean(week_4))
    print('The standard deviation of Week 4 is', stdev(week_4, xbar=None))
    print('The variance of Week 4 is', variance(week_4, xbar=None))
    plt.show()


def period_11():
    days = 7
    ind = np.arange(days)

    week_1 = (1437.45, 886.21, 759.01, 895.53, 742.15, 700.07, 1036.90)
    week_2 = (1459.89, 1042.40, 1422.92, 1894.29, 242.97, 519.89, 1278.29)
    week_3 = (763.13, 852.46, 881.98, 1083.54, 803.19, 1004.82, 1440.47)
    week_4 = (960.61, 1021.66, 780.44, 1009.93, 0, 0, 0)

    plt.plot(week_1, 'g-', label='Week 1')
    plt.plot(week_2, 'b-', label='Week 2')
    plt.plot(week_3, 'r-.', label='Week 3')
    plt.plot(week_4, 'c:', label='Week 4')

    plt.legend()
    plt.ylabel('Sales')
    plt.title('Period 11 Dairy Sales')
    plt.xticks(ind, ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
    print('The mean of Week 1 is', mean(week_1))
    print('The standard deviation of Week 1 is', stdev(week_1, xbar=None))
    print('The variance of Week 1 is', variance(week_1, xbar=None))
    print('The mean of Week 2 is', mean(week_2))
    print('The standard deviation of Week 2 is', stdev(week_2, xbar=None))
    print('The variance of Week 2 is', variance(week_2, xbar=None))
    print('The mean of Week 3 is', mean(week_3))
    print('The standard deviation of Week 3 is', stdev(week_3, xbar=None))
    print('The variance of Week 3 is', variance(week_3, xbar=None))
    print('The mean of Week 4 is', mean(week_4))
    print('The standard deviation of Week 4 is', stdev(week_4, xbar=None))
    print('The variance of Week 4 is', variance(week_4, xbar=None))
    plt.show()


main()

