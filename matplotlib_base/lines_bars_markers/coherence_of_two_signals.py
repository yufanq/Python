import numpy as np
import matplotlib.pyplot as plt
'''
比较一致性
cohere(x, y, NFFT=256, Fs=2, Fc=0, detrend=<function detrend_none>,
		 window=<function window_hanning>, noverlap=0, pad_to=None, 
        sides='default', scale_by_freq=None, *, data=None, 
          **kwargs)[source]


'''
#Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t)) # white noise 1
nse2 = np.random.randn(len(t)) # white naise 2

#Two signals with a coherent port at 10 Hz and a random port
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig ,axs = plt.subplots(2,1)
axs[0].plot(t,s1,t,s2)
axs[0].set_xlim(0,2) # X轴范围
axs[0].set_xlabel('Time')
axs[0].set_ylabel('S1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')
fig.tight_layout()

plt.show()