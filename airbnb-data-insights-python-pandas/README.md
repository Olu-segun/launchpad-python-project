# Airbnb Listings Data Cleaning and Enrichment (Pandas Project)

## 🏡 Project Overview
This project focuses on cleaning, transforming, and enriching Airbnb listings data using **Pandas**. The goal is to prepare the dataset for further analysis such as price trends, host performance, and neighborhood-based insights.

## 🧹 Data Cleaning Steps
1. **Converted price fields to numeric values**
   ```python
   clean_data['price'] = clean_data['price'].replace(r'[$,]', '', regex=True).astype(float)
   ```

2. **Handled missing values**
   - Replaced missing `reviews_per_month` with `0`.
   - Filled missing `host_name` values with `"Not Specified"` instead of `"Unknown"`.
   - Removed rows where `neighbourhood_cleansed` was missing.

3. **Dropped rows with missing price or availability values**
   ```python
   clean_data.dropna(subset=['price', 'availability_30'], inplace=True)
   ```

## 💡 Data Enrichment
1. **Created new feature: `price_per_booking`**
   ```python
   enriched_data['price_per_booking'] = enriched_data['price'] * enriched_data['minimum_nights']
   ```

2. **Categorized listing availability**
   ```python
   enriched_data['availability_category'] = pd.cut(
       enriched_data['availability_365'],
       bins=[-1, 99, 300, 365],
       labels=['Rare', 'Part-time', 'Full-time']
   )
   ```

## 📊 Exploratory Questions
- How does **average price vary** across different neighborhoods?
  ```python
  clean_data.groupby('neighbourhood_cleansed')['price'].mean().sort_values(ascending=False)
  ```
- How many listings **have never been reviewed**?
  ```python
  len(clean_data[clean_data['number_of_reviews'] == 0])
  ```

## 🛠️ Tools and Libraries
- **Python 3.10+**
- **Pandas**
- **NumPy**

## 📈 Potential Extensions
- Integrate with visualization tools such as **Matplotlib** or **Seaborn**.
- Export results to **Power BI** for reporting.
- Automate updates using **Airflow** or **DBT**.

---
💡 *This project demonstrates strong data cleaning, transformation, and enrichment skills using Pandas — a key step before analysis and visualization.*
