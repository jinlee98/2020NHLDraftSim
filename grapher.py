import numpy as np
import matplotlib.pyplot as plt

# copy over dataset for a player:
percentages = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4000000000000001, 4.3, 9.2, 11.4, 13.4, 12.4, 10.0, 10.9, 7.5, 4.1000000000000005, 3.3000000000000003, 2.9000000000000004, 3.0, 1.5, 2.0, 1.5, 0.6, 0.3, 0.3, 0.0, 0.0, 0.0]
selection_number = []
for i in range(1, 32):
    selection_number.append(i)

y_pos = np.arange(len(selection_number))

# Create bars
plt.bar(y_pos, percentages)

# Create names on the x-axis
plt.xticks(y_pos, selection_number)

plt.title('Hendrix Lapierre Draft Percentages')
plt.xlabel('Draft Position')
plt.ylabel('Percentage Chance')

# Show graphic
plt.show()
