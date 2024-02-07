
#预览处理后的数据
import numpy as np
import matplotlib.pyplot as plt
img3d = np.load('D:\python\MedicalSeg\tools\data\abdomen\abdomen_phase0\images\0b2be9e0-886b-4144-99f0-8bb4c6eaa848-0000.npy')
print(img3d.shape)#经过采样，形状发生了改变
plt.imshow(img3d[60,:,:],'gray')
plt.show()