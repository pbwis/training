import pandas as pd


y = {'f(x)': [3, 12, 4, 7], 'g(x)':[1, 3, -3, 8]}
x = [1, 2, 3, 4]

graph = pd.DataFrame(y, x)
graph.plot(kind='line', grid=True, title='test graph', ylabel='Y', xlabel='X')
