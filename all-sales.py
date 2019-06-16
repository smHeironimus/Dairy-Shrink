import numpy as np
import matplotlib.pyplot as plt


def main():
    days = 7
    ind = np.arange(days)

    p8_week_1 = (1660.08, 815.42, 806.09, 1131.10, 804.39, 874.19, 1488.50)
    p8_week_2 = (1573.14, 1062.79, 1000.42, 1017.26, 2218.39, 657.99, 1009.80)
    p8_week_3 = (2552.43, 1502.99, 851.82, 1171.10, 721.15, 957.58, 1012.95)
    p8_week_4 = (1310.32, 1226.90, 867.07, 1054.50, 703.62, 832.35, 1142.31)

    p9_week_1 = (1416.52, 987.04, 766.67, 939.28, 637.45, 839.00, 1107.03)
    p9_week_2 = (1532.97, 1109.48, 804.79, 1005.38, 749.81, 770.97, 1001.74)
    p9_week_3 = (1689.57, 836.91, 620.83, 1028.74, 788.34, 716.40, 1291.59)
    p9_week_4 = (1504.97, 870.39, 623.03, 893.39, 645.67, 750.66, 1054.17)

    p10_week_1 = (1298.71, 944.91, 803.82, 945.77, 735.17, 923.98, 1239.39)
    p10_week_2 = (1595.54, 891.91, 829.91, 964.65, 904.25, 568.68, 1125.20)
    p10_week_3 = (1808.71, 1018.22, 778.58, 767.82, 652.53, 830.30, 1134.60)
    p10_week_4 = (1523.49, 970.34, 835.86, 1207.03, 676.53, 693.96, 1132.16)

    plt.plot(p8_week_1, 'r--', label='Period 8 Week 1')
    plt.plot(p8_week_2, 'r-.', label='Period 8 Week 2')
    plt.plot(p8_week_3, 'r-', label='Period 8 Week 3')
    plt.plot(p8_week_4, 'r:', label='Period 8 Week 4')

    plt.plot(p9_week_1, 'g-.', label='Period 9 Week 1')
    plt.plot(p9_week_2, 'g-.', label='Period 9 Week 2')
    plt.plot(p9_week_3, 'g-.', label='Period 9 Week 3')
    plt.plot(p9_week_4, 'g-.', label='Period 9 Week 4')

    plt.plot(p10_week_1, 'b:', label='Period 10 Week 1')
    plt.plot(p10_week_2, 'b:', label='Period 10 Week 2')
    plt.plot(p10_week_3, 'b:', label='Period 10 Week 3')
    plt.plot(p10_week_4, 'b:', label='Period 10 Week 4')

    plt.legend()
    plt.ylabel('Sales')
    plt.title('Periods 8-10 Dairy Sales')
    plt.xticks(ind, ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
    plt.show()


main()

