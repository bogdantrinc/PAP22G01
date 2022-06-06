import matplotlib.pyplot as plt

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
fig1.dpi = 200
ay1.plot([1,2,3], [5,5,5], label="TEST1")
ay2.plot([2,3,4], [4,4,4], label="TEST2")
ay1.legend()
ay2.legend()
plt.xlabel('seconds')
plt.ylabel('km')
plt.title("My example Graph")
plt.show()