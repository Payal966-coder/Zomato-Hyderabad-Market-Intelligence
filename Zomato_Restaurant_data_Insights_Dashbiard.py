import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# -------------------- 1. DATA LOADING & CLEANING --------------------

df = pd.read_csv('HyderabadResturants.csv')
df.columns = df.columns.str.strip().str.lower()
column_map = {'name': 'names', 'rating': 'ratings', 'cost for one': 'price for one'}
df.rename(columns=column_map, inplace=True)

df = df.dropna(subset=['names', 'ratings', 'price for one', 'cuisine']).drop_duplicates()
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')
df['price for one'] = pd.to_numeric(df['price for one'].astype(str).str.replace('[^0-9]', '', regex=True), errors='coerce')
df = df.dropna(subset=['ratings', 'price for one'])

# Calculations
total_rest = len(df)
avg_rating = round(df['ratings'].mean(), 2)
avg_price = int(df['price for one'].mean())
cuisines_list = df['cuisine'].str.split(',').explode().str.strip()
top_cuisines_data = cuisines_list.value_counts().head(10).sort_values()
lead_cuisine = top_cuisines_data.index[-1].title()

# -------------------- 2. VISUAL ARCHITECTURE --------------------
plt.style.use('dark_background')
fig = plt.figure(figsize=(20, 12), facecolor='#0B0C10')
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35, top=0.70, bottom=0.08, left=0.2, right=0.95)

fig.text(0.5, 0.96, "ZOMATO MARKET INTELLIGENCE: HYDERABAD HUB", fontsize=30, fontweight='bold', ha='center', color='#66FCF1')
fig.text(0.5, 0.93, "Strategic Data Intelligence Dashboard | Final Production Build 2026", fontsize=11, ha='center', color='#C5C6C7', alpha=0.5)

# -------------------- 3. KPI MODULES (FIXED POSITION) --------------------
kpis = [("OUTLETS", f"{total_rest}", "#45A29E"), 
        ("AVG RATING", f"{avg_rating}/5", "#66FCF1"), 
        ("AVG PRICE", f"₹{avg_price}", "#C5C6C7"), 
        ("LEAD CUISINE", f"{lead_cuisine}", "#45A29E")]

for i, (label, value, col) in enumerate(kpis):
    ax = fig.add_axes([0.1 + (i * 0.21), 0.78, 0.18, 0.08], facecolor='#1F2833')
    ax.spines[['top','right','bottom','left']].set_visible(False)
    ax.axvline(x=0.01, color=col, linewidth=8)
    ax.text(0.5, 0.7, label, ha='center', color='#C5C6C7', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.25, value, ha='center', color='white', fontsize=20, fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])

# -------------------- 4. CHARTS  --------------------

# Plot 1: Price vs Rating
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(df['price for one'], df['ratings'], alpha=0.3, color='#66FCF1', s=40)
ax1.set_title('PRICE VS RATING DISTRIBUTION', color='#66FCF1', pad=25, fontweight='bold', fontsize=13)
ax1.set_xlim(0, 500); ax1.set_ylim(2, 5.2)

# Plot 2: Market Share
ax2 = fig.add_subplot(gs[0, 1])
bins = [0, 150, 300, 500, 10000]; lbls = ['Budget', 'Mid', 'Upper', 'Elite']
df['seg'] = pd.cut(df['price for one'], bins=bins, labels=lbls)
m_data = df['seg'].value_counts().sort_index()
ax2.pie(m_data, labels=m_data.index, autopct='%1.1f%%', startangle=140, 
        colors=['#1F2833', '#45A29E', '#66FCF1', '#C5C6C7'],
        pctdistance=0.75, wedgeprops={'width': 0.45, 'edgecolor': '#0B0C10'})
ax2.set_title('MARKET SEGMENT SHARE', color='#66FCF1', pad=25, fontweight='bold', fontsize=13)

# Plot 3: Top Rated 
ax3 = fig.add_subplot(gs[1, 0])
top_rated = df.nlargest(10, 'ratings').sort_values('ratings')
bars3 = ax3.barh(top_rated['names'], top_rated['ratings'], color='#66FCF1')
ax3.set_title('TOP RATED ESTABLISHMENTS', color='#66FCF1', pad=25, fontweight='bold', fontsize=13)
ax3.set_xlim(4, 5)
ax3.bar_label(bars3, padding=5, fmt='%.1f', fontsize=9)

# Plot 4: Cuisine Dominance
ax4 = fig.add_subplot(gs[1, 1])
bars4 = ax4.barh(top_cuisines_data.index, top_cuisines_data.values, color='#45A29E')
ax4.set_title('MARKET PRESENCE BY CUISINE', color='#66FCF1', pad=25, fontweight='bold', fontsize=13)
ax4.bar_label(bars4, padding=5, fontsize=9)

# Final formatting
for ax in [ax1, ax3, ax4]:
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=10)

plt.show()