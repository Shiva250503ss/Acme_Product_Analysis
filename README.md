# ACME Sales Forecasting Model

## Project Overview
This project develops a sales forecasting model for ACME, a company structured across multiple levels (Portfolio, Geography, Category, Brand, and Segment). The model aims to predict sales in various market scenarios and helps in decision-making by providing insights into potential sales and margins under different constraints.

## Background
ACME's structure consists of various levels, with sales aggregated at the Segment level up to the Portfolio level. The challenge is to scientifically predict sales across different segments and aggregate these to higher levels, considering various constraints and market dynamics.

## Objectives
1. **Synthetic Data Generation:** Simulate a realistic dataset representing ACME's structure and constraints.
2. **Maximize Sales:** Develop scenarios to maximize sales within given constraints.
3. **Maximize Margin:** Focus on maximizing profit margins across different segments.
4. **Sales and Margin Goals:** Achieve specific sales or margin targets while optimizing the other metric.
5. **Annual Projections:** Provide annual sales forecasts over a 5-year period, adjusting constraints annually.

## Data
The synthetic dataset generated mimics real-world conditions with constraints on trends and contributions at each segment level. Details include:
- **Initial Sales and Margin:** Base figures for sales and margin percentage.
- **Trend Constraints:** Minimum and maximum growth percentages.
- **Contribution Constraints:** Minimum and maximum contribution percentages per unit within its level.

The dataset is structured across ACME's hierarchies: Portfolios, Geographies, Categories, Brands, and Segments.

## Repository Structure
- `Algorithm.ipynb`: Jupyter notebook containing the main forecasting algorithm.
- `dataset.py`: Python script to generate the synthetic dataset.
- `EDA.ipynb`: Exploratory Data Analysis notebook analyzing the synthetic dataset.

## Data Generation:
   Run `dataset.py` to generate a synthetic dataset saved as `Acme_Synthetic_Dataset.csv`. This script simulates realistic sales data with constraints for each segment.

## Algorithm Execution
Open `Algorithm.ipynb` in a Jupyter environment to run the sales forecasting model. This notebook contains the detailed steps and calculations used to predict future sales and margin scenarios under various constraints defined by the company's structure.

## Data Analysis
Use `EDA.ipynb` for initial explorations and visualizations of the synthetic dataset. This notebook helps understand the distribution and relationship of the different data points which are crucial for setting realistic constraints and expectations in the forecasting model.

## Technologies Used
- **Python**: Primary programming language used for project development.
- **Pandas**: Utilized for data manipulation and analysis.
- **NumPy**: Employed for numerical operations within the dataset.
