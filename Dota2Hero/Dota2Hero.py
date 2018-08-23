#################################RND: Dota2Hero
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

dota = pd.read_csv("hero_stats.csv")
dota.shape

armor = sns.swarmplot(data = dota, y='Armor')

sns.jointplot(dota['Attacks Per Second'],dota['Damage Per Second'],kind = 'reg')

facett = sns.Implot(data=dota, x = 'Attack Damage', y = 'Damage Per Second', hue = 'Primary Stat', fit_reg = False, legend = True, legend_out = True)

fig = sns.lmplot( data=dota, x='Increased Attack Speed', y='Attacks Per Second', hue='Attack Type',fit_reg=True, legend=True, legend_out=True, aspect=16/10)

ax = sns.violinplot(x="Movement Speed", y="Primary Stat", hue="Attack Type",
data=dota, palette="Set2", split=True, scale="count", inner="stick", scale_hue=False, bw=.2)

ax = sns.boxplot(x="%Physical Damage Reduction", y="Primary Stat", data=dota)

ax = sns.stripplot(x="Primary Stat", y="Mana", hue="Attack Type", data=dota, jitter=True)

ax = sns.stripplot("Primary Stat", "Base Damage Max", "Attack Type", data=dota,
palette="Set1", size=25, marker="D",edgecolor="blue", alpha=.2)