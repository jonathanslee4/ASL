import numpy as np

label = np.fromfile("000000.label", dtype=np.int32)
label = label.reshape((-1))

print(label)
print(len(label))
print(label.shape)