#!/usr/bin/python
import matplotlib.pyplot as plt
import csv
data = []
with open('results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row[1])

plt.plot(data)
plt.ylabel('amplitude')
plt.xlabel('slice #')
plt.title('wav file')
plt.show()
