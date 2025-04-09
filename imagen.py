import matplotlib.pyplot as plt
import numpy as np
i=np.array([[1,2],[4,4]])
plt.imshow(i, cmap='gray', interpolation='nearest')
plt.show()