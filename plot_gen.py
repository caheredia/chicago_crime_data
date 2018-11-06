import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#plot days of week in sparkline graphs

means = np.arange(10, 60, 10)
sigma = 7
means_dict = {}
for item in means:
    means_dict[item] = np.random.normal(item, sigma, 365)

df = pd.DataFrame(means_dict)


fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex=True, figsize=(12, 4))
title = 'Broken Spears decrease overtime'
for column, axess in zip(df.columns[::-1], (ax1, ax2, ax3, ax4, ax5)):
    df[column].plot(kind='density', ax=axess, color='orange')
    axess.set_ylabel('column ' + str(column), rotation=0, labelpad=50, fontsize=16)
    axess.get_yaxis().set_ticks([])
    axess.set_xticks(means)
    axess.set_facecolor('.97')

    axess2 = axess.twinx()
    std = round(df[column].std(), 1)
    local_low = round(df[column].min(), 1)
    local_max = round(df[column].max(), 1)
    local_mean = round(df[column].mean(), 1)
    right_string = 'std: {std} mean: {local_mean} max: {local_max}'.format(
        std=std, local_mean=local_mean,  local_max=local_max)
    axess2.set_ylabel(right_string, rotation=0, labelpad=125, fontsize=16, color='gray')
    axess2.get_yaxis().set_ticks([])
ax1.set_title(title, fontsize=18)

fig.show()
plt.show()
