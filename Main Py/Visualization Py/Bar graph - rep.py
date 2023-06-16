import matplotlib.pyplot as plt


# Sample data
x = ['A', 'B', 'C', 'D', 'E']  # Categories
y = [10, 24, 15, 20, 12]  # Values

# Create a bar graph
plt.bar(x, y)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')

# Show the plot
plt.show()
