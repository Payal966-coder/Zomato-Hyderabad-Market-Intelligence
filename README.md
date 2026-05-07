# ZOMATO MARKET INTELLIGENCE: HYDERABAD HUB

&nbsp;&nbsp;&nbsp;&nbsp;
**Transforming 590+ raw restaurant data points into actionable business intelligence.**

---

### 📊 Dashboard Preview
![Zomato Hyderabad Market Analysis](Screenshot%202026-05-07%20163212.png)

---

### 📌 Table of Contents
* Overview
* Dashboard Features
* Tech Stack
* Project Structure
* Installation & Usage
* Key Insights
* UI/UX Design Decisions
* Connect With Me

### 🧠 Overview
This project converts raw Zomato restaurant CSV data into a **4-panel strategic dashboard** built entirely with Python.
Instead of relying on BI tools like Tableau or Power BI, every chart, layout, and color decision is coded from scratch — giving full control over design, spacing, and visual hierarchy.

**Goal:** Move beyond default matplotlib aesthetics and build something that looks like it belongs in a corporate analytics report.

### 📊 Dashboard Features

| Panel | Chart Type | What It Shows |
| :--- | :--- | :--- |
| Top-left | Scatter Plot | Price vs Rating Distribution |
| Top-right | Donut Chart | Market Segment Share (Budget, Mid, Elite) |
| Bottom-left | Horizontal Bar | Top 10 Best-Rated Establishments |
| Bottom-right | Horizontal Bar | Market Presence by Cuisine (Dominance) |

### 🛠️ Tech Stack

| Library | Version | Purpose |
| :--- | :--- | :--- |
| Python | 3.13+ | Core language |
| Pandas | 2.0+ | Data loading, cleaning & grouping |
| NumPy | 1.24+ | Fast numerical aggregation |
| Matplotlib | 3.7+ | All chart rendering & layout design |

### 📁 Project Structure

📦 Zomato-Market-Intelligence-Hyderabad  
 ┣ 📄 HyderabadResturants.csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← Raw dataset (590+ rows)  
 ┣ 🐍 Zomato_Restaurant_data_Insights_Dashbiard.py ← Main script — all logic & charts  
 ┣ 🖼️ Screenshot 2026-05-07 163212.png ← High-res dashboard preview  
 ┗ 📝 README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← You are here

### 🚀 Installation & Usage

**Step 1 — Clone the repo** `git clone https://github.com/Payal966-coder/Zomato-Market-Intelligence-Hyderabad.git`  
`cd Zomato-Market-Intelligence-Hyderabad`

**Step 2 — Install dependencies** `pip install pandas numpy matplotlib`

**Step 3 — Run the dashboard** `python Zomato_Restaurant_data_Insights_Dashbiard.py`

The dashboard will render in a window and provides a high-resolution strategic overview of the Hyderabad restaurant market.

### 💡 Key Insights
* 🧁 **Desserts & Beverages** are the top categories, indicating a shift towards cafe culture.
* 💸 **Budget Segment** dominates approx **70% of the market**, showing high price sensitivity.
* 📏 **Mid-Range** pricing (₹150-₹300) shows the highest density of 4+ star ratings.
* ⭐ The market maintains a solid **3.95/5 average rating** across the city.

### 🎨 UI/UX Design Decisions
* ✔ **Cyan-Neon Palette** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Professional, cohesive look
* ✔ **Custom GridSpec** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Precise control over margins to prevent label clipping
* ✔ **Value Labels** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Direct labels on bars for quick reading
* ✔ **Donut Chart** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Cleaner and more modern feel
* ✔ **Spines Removed** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Reduces visual noise

### 🤝 Connect With Me

**Payal Saxena** &nbsp;&nbsp;

---
**Made with Python by Payal Saxena** | If you found this useful, give it a ⭐ on GitHub!
