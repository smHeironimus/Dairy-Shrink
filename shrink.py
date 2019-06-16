import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 4
    ind = np.arange(n)

    store_901 = (8.05, 4.75, 6.05, 7.67)
    store_903 = (10.77, 9.02, 12.08, 7.36)
    store_904 = (20.1, 25.97, 14.74, 16.32)
    store_905 = (0.97, 16.5, 11.52, 10.66)
    store_906 = (12.29, 4.35, 9.93, 11.88)
    store_951 = (8.75, 2.51, 9.34, 7.03)
    store_952 = (9.55, 10.87, 13.35, 6.81)
    store_953 = (10.74, 17.07, 8.54, 11.37)

    plt.plot(store_901, 'g-', label='901')
    plt.plot(store_903, 'r-', label='903')
    plt.plot(store_904, 'b:', label='904')
    plt.plot(store_905, 'c-', label='905')
    plt.plot(store_906, 'm-', label='906')
    plt.plot(store_951, 'y:', label='951')
    plt.plot(store_952, 'k-', label='952')
    plt.plot(store_953, 'b-.', label='952')

    plt.legend()
    plt.ylabel("Shrink Percentage")
    plt.xlabel("Weeks")
    plt.title("Dairy Shrink - West Region")
    plt.xticks(ind, ('37', '38', '39', '40'))
    plt.show()


main()
