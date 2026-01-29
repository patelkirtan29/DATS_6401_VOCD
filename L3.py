#%%
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(6401)

#%%
N = 365
data = np.random.rand(N,4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
print(df.head(5))
# print(df.describe())
# print(df.info())

#%%
date = pd.date_range(start='1/1/2000', periods=len(df), freq='D')
df.index = date
ax = df.plot(
        subplots=True, layout=(4,1), sharex=True,
        grid=True, figsize=(10,5), lw = 2,
        xlabel='time', ylabel='mag'
    )
ax[0,0].set_ylabel('Mag', fontsize=16)
ax[3,0].set_xlabel('Time', fontsize=16)
ax[0,0].set_title('Test', fontsize=16)
plt.tight_layout()
plt.show()

#%%
tips = sns.load_dataset('tips')
print(tips.columns)
print(tips['time'].unique())
date = pd.date_range(start='1/1/2000', periods=len(tips), freq='D')
tips.index = date
tips[['tip', 'total_bill']].plot(
    kind = 'line',
    title = 'Tip Dataset',
    xlabel = 'Time',
    ylabel = 'USD($)',
    fontsize = 16,
    grid = True
)
plt.tight_layout()
plt.show()

#%%
tips[['tip', 'total_bill']].plot(
    kind = 'hist',
    title = 'Tip Dataset Histogram',
    xlabel = 'USD($)',
    ylabel = 'Frequency',
    fontsize = 16,
    grid = True,
    bins = 50
)
print('tip mean', tips['tip'].mean())
plt.tight_layout()
plt.show()

#%%
tip_group = tips.loc[:, ['sex', 'tip']].groupby(['sex']).sum()
tip_group.reset_index(inplace=True)
tip_group.sort_values(by=['tip'], ascending=False, inplace=True)
tip_group.plot(
    kind='bar',
    x='sex',
    y='tip',
    title = 'Tip Dataset Bar Chart',
    grid = True,
    fontsize = 16,
    ylabel = 'USD($)',
    xlabel = 'Sex',
)
plt.tight_layout()
plt.show()