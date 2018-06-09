import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados
plt.hist(dados['sepal_length'], bins=12)
plt.show()