# -*- coding: utf-8 -*-
"""Border_crossing_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18WdhrWhm-TAUKMa1GR1Fk3QxHYPgyVzk

This analysis delves into the historical trends of U.S. border crossings at official ports of entry, investigating how these patterns intersect with key national and global events. While excluding undocumented crossings, the study examines the impacts of pivotal moments such as 9/11, the COVID-19 pandemic, and trade agreements like NAFTA (1994) and the USMCA (2020). Additionally, the analysis considers economic factors, such as Canadian tax policies that encourage cross-border shopping for lower-priced goods, and Mexico's appeal as a premier travel and vacation destination. The objective is to provide a data-driven overview of border-crossing trends over time, offering insights into economic, social, and historical influences—while steering clear of modern political debates. Through this lens, we aim to address key questions drawn from the dataset.

Questions for our examination:

*   Do crossing trends reflect significant global or national events, such as 9/11, the 2008 financial crisis, or the COVID-19 pandemic?

*   What is the distribution of border crossings between the U.S.-Mexico and U.S.-Canada borders, and what does it reveal about the significance of each border?

*   Which ports of entry handle the largest volumes of border crossings, and how do southern and northern ports compare in activity?

*    What are the most common methods of border crossing, and how do they compare in terms of usage volume?

*   How do border crossing rates vary among southern border states, and what factors contribute to the differences, particularly in New Mexico compared to Arizona, California, and Texas?

*   How do border crossing trends in 2019 compare to those in 2024, particularly in terms of recovery from the COVID-19 pandemic and changes in trade or travel patterns?
"""

# Commented out IPython magic to ensure Python compatibility.
## Reading in the data.
# %pip install seaborn
import pandas as pd
import numpy as np
from scipy import stats
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import calendar

df = pd.read_csv('/content/Border_Crossing_Entry_Data.csv')
df.head(10)

df.info()

null_check = df.isnull().any()
print(null_check)

df['Year'] = pd.to_datetime(df['Date']).dt.year
df

"""Question: Do crossing trends reflect significant global or national events, such as 9/11, the 2008 financial crisis, or the COVID-19 pandemic?

Border crossings experienced a notable decline during the 2008 recession, with numbers only recovering around 2016. This drop aligns with the broader economic downturn and its impact on trade, travel, and migration patterns. Another significant dip occurred in 2020 due to the COVID-19 pandemic. However, the decline in 2020 was less severe than that of the 2008 recession, likely because of the temporary nature of pandemic-related restrictions compared to the prolonged economic struggles of the earlier period.

Following the 2020 dip, there was a quicker recovery, suggesting resilience in cross-border activity and the adaptation of systems to new challenges. Looking ahead, it is reasonable to anticipate a continued increase in border crossings as global economic pressures and disparities drive relocation, trade, and travel. This trend highlights the interconnectedness of economic health, global events, and migration patterns, underscoring the critical role of border activity in economic and social dynamics.
"""

Yearly_Avg = df.groupby('Year')['Value'].mean().round(2)
Yearly_Avg
years = Yearly_Avg.index
plt.plot(years, Yearly_Avg, lw=3)
plt.xlabel("Year")
plt.ylabel("Yearly Average Value")
plt.title("Immigration Yearly Averges")
plt.show()

"""Question: What is the distribution of border crossings between the U.S.-Mexico and U.S.-Canada borders, and what does it reveal about the significance of each border?

This pie chart titled "Crossing between the Borders" illustrates the proportion of border crossings at the U.S.-Mexico and U.S.-Canada borders. The majority of crossings, 73.6%, occur at the U.S.-Mexico border, reflecting its status as the primary hub for border activity. In contrast, the U.S.-Canada border accounts for 26.4% of crossings. This disparity highlights the heavier traffic and economic and social ties at the southern border compared to the northern one.
"""

Border = df.groupby('Border')['Value'].sum().sort_values(ascending=False).head(10)
Country = Border.index

plt.pie(Border, labels=Country, startangle = 90, autopct='%1.1f%%')
plt.title ("Crossing between the Borders")
plt.show()

Freguent_Ports = df.groupby('Port Name')['Value'].sum().sort_values(ascending=False).head(10)
Freguent_Ports

"""Question: Which ports of entry handle the largest volumes of border crossings, and how do southern and northern ports compare in activity?

This bar chart titled "Frequent Ports" highlights the busiest ports of entry for border crossings in terms of total volume. The San Ysidro port leads with the highest volume, closely followed by El Paso and Laredo. Other significant ports include Hidalgo, Calexico, and Buffalo Niagara Falls. Ports such as Brownsville, Otay Mesa, Detroit, and Nogales show relatively lower volumes but still rank among the top 10. This distribution reflects the dominance of certain southern U.S. ports due to their proximity to Mexico, while Buffalo Niagara Falls and Detroit represent key northern entry points near the U.S.-Canada border.
"""

Port = Freguent_Ports.index

sorted_data = sorted(zip(Freguent_Ports, Port), reverse=False)
Freguent_Ports, Port = zip(*sorted_data)

def millions_formatter(Port, pos):
    """Formatter to display values in millions."""
    return f'{Port / 1e6:.1f}M'

plt.barh(Port, Freguent_Ports, height=0.5)
plt.xticks(rotation=80)
plt.xlabel("Port Name")
plt.ylabel("Value")
plt.title("Freguent Ports")
plt.show()

"""Question: What are the most common methods of border crossing, and how do they compare in terms of usage volume?

The bar chart highlights the top five methods of border crossing, measured in millions. Personal vehicle passengers dominate as the most utilized method, with over 6,000 million crossings, followed by personal vehicles at more than 4,000 million. Pedestrian crossings rank third, showing a notable yet smaller volume compared to vehicle-based methods. Commercial transportation methods, such as trucks and loaded truck containers, account for significantly fewer crossings, with truck containers being the least common. This distribution underscores the reliance on personal and passenger vehicle travel for border crossings, while commercial methods contribute a smaller share.
"""

Ingress = df.groupby('Measure')['Value'].sum().sort_values(ascending=False).head()
Method = Ingress.index

sorted_data = sorted(zip(Ingress, Method), reverse=False)
Ingress, Method = zip(*sorted_data)

def millions_formatter(Method, pos):
    """Formatter to display values in millions."""
    return f'{Method / 1e6:.1f}M'

plt.barh(Method, Ingress)
plt.title("Top 5 Methods for Broder Crossing", fontsize=20)
plt.xlabel("Crossing in Millions", fontsize=15)
plt.ylabel("Method of Transportation", fontsize=15)
plt.yticks(rotation=45, ha='right')  # Rotate y-axis labels for better readability
plt.gca().xaxis.set_major_formatter(FuncFormatter(millions_formatter))
plt.show()

"""Question: How do border crossing rates vary among southern border states, and what factors contribute to the differences, particularly in New Mexico compared to Arizona, California, and Texas?

Corresponding with the previous pie chart, we observe that southern border states experience significantly higher rates of border crossings compared to other regions, with the notable exception of New Mexico. This discrepancy can be attributed to several factors. New Mexico has a relatively low population density and lacks major urban centers near the border, which limits the volume of cross-border activity. Additionally, the areas across the border in Mexico adjacent to New Mexico are also sparsely populated, further reducing the flow of traffic in this region.

In contrast, Arizona, California, and Texas see the highest rates of border crossings. This can be explained by their larger diaspora populations, particularly in urban hubs near the border, which fosters regular travel between the U.S. and Mexico. Furthermore, passenger vehicles continue to be the dominant mode of border crossing, driven by the accessibility and proximity of major cities like San Diego, El Paso, and Nogales. These factors collectively contribute to the high volume of crossings in these states, emphasizing their role as critical points of connection along the U.S.-Mexico border.









"""

State_level = df.groupby('State')['Value'].sum().sort_values(ascending=False)
State = State_level.index
State

def millions_formatter(State_level, pos):
    """Formatter to display values in millions."""
    return f'{State_level / 1e6:.1f}M'

plt.plot(State_level, State, lw=3)
plt.title("Number of Border Crossers by State")
plt.xlabel("Crossers in Millions", fontsize=15)
plt.ylabel("States", fontsize=15)
plt.gca().xaxis.set_major_formatter(FuncFormatter(millions_formatter))
plt.show()

df['Month'] = pd.to_datetime(dfe['Date']).dt.month

Average_per_month = df.groupby('Month')['Value'].mean().round(2)
Month = Average_per_month.index
Month = Month.tolist()
Month = [calendar.month_name[i] for i in Month]
Month

Last_year = df.loc[df['Year']== 2024]
Last_year

Last_admin = df.loc[df['Year']==2020]
Last_admin

Last_admin_avg_monthly = Last_admin.groupby('Month')['Value'].mean().round(2)
Month = Last_admin_avg_monthly.index
Month = Month.tolist()
Month = [calendar.month_name[i] for i in Month]
Month

"""Question: How do border crossing trends in 2020 compare to those in 2024, particularly in terms of recovery from the COVID-19 pandemic and changes in trade or travel patterns?

The global impact of the COVID-19 pandemic in 2020 caused a sharp decline in cross-border travel, with a notable drop beginning in April as lockdowns and travel restrictions were implemented worldwide. While there was a steady recovery throughout the remainder of 2020, the number of crossings never fully returned to pre-pandemic levels by year-end. By 2024, cross-border travel showed significant improvement, reflecting eased restrictions, increased vaccination rates, and a gradual return to normalcy in trade and tourism. However, the long-term effects of the pandemic are still evident in altered travel behaviors and economic conditions, with some trade routes and travel patterns permanently reshaped. This comparison highlights the resilience of cross-border activity while underscoring the lingering impacts of one of the most disruptive global events in modern history.
"""

x_pos = np.arange(len(Month))

# Plot the bars using the numerical positions
plt.bar(x_pos - 0.2, Average_per_month, width=0.4, align='center', label='Average per month')  # width adjusted for clarity

plt.bar(x_pos + 0.2, Last_admin_avg_monthly, width=0.4, align='center', label='Last admin avg monthly')  # width adjusted for clarity

# Set the x-axis ticks to be the month names
plt.xticks(x_pos, Month, rotation=45, ha='right')  # ha='right' for better alignment of rotated labels


plt.title("Comparisson between year 2020 and 2024")
plt.xlabel("Months", fontsize=15)
plt.ylabel("Average Crossing", fontsize=15)
plt.legend(["2024", "2020"], loc="lower right")
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

"""Summary:
Border crossings experienced a significant decline during the 2008 recession, with recovery only starting around 2016, reflecting the broader economic downturn's impact on trade, travel, and migration. A second drop occurred in 2020 due to the COVID-19 pandemic, but this decline was less severe than in 2008, likely due to the temporary nature of pandemic restrictions. Following the 2020 dip, cross-border activity rebounded more quickly, showing resilience and adaptability.

Looking ahead, it is expected that border crossings will continue to increase as global economic pressures drive trade, travel, and migration. The U.S.-Mexico border sees the majority of crossings (73.6%) compared to the U.S.-Canada border (26.4%). The busiest ports of entry include San Ysidro, El Paso, and Laredo, with a dominance of personal vehicles as the primary method of crossing.

Southern U.S. states like California, Arizona, and Texas experience the highest rates of border crossings, driven by larger diaspora populations and urban centers near the border. In contrast, New Mexico has fewer crossings due to its low population density and sparse border areas.

The COVID-19 pandemic sharply reduced cross-border travel in 2020, but by 2024, crossings had largely recovered. Despite this, some travel behaviors and economic conditions remain altered, reflecting the lasting impact of the pandemic on global trade and migration patterns.
"""