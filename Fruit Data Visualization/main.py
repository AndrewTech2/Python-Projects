import plotly.express as plt

data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}
plot = plt.scatter(data, x='Fruit', y='Amount')
plot.show()