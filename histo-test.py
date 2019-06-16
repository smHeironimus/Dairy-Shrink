import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (150, 160, 146, 172, 155)
menStd = (20, 30, 32, 10, 20)

fig, ax = plt.subplots()

ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
p1 = ax.bar(ind, menMeans, width, color='r', bottom=0, yerr=menStd)


womenMeans = (145, 149, 172, 165, 200)
womenStd = (30, 25, 20, 31, 22)
p2 = ax.bar(ind + width, womenMeans, width,
            color='y', bottom=0, yerr=womenStd)

otherMeans = (110, 190, 135, 178, 100)
otherStd = (20, 23, 29, 41, 32)
p3 = ax.bar(ind + width, otherMeans, width,
            color='b', bottom=0, yerr=otherStd)

ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday'))

ax.legend((p1[0], p2[0], p3[0]), ('Men', 'Women', 'Other'))
ax.yaxis.set_units('inch')
ax.autoscale_view()

plt.show()