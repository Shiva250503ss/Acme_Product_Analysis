import pandas as pd
import numpy as np

# -----------------------------------------------------
# 1. GLOBAL DEFAULT CONSTRAINTS
# -----------------------------------------------------
global_constraints = {
    "min_trend": -5,          # Default min growth = -5%
    "max_trend": 15,          # Default max growth = 15%
    "min_contribution": 5,    # Default min contribution = 5%
    "max_contribution": 40,   # Default max contribution = 40%
    "margin_range": (30, 60), # Margin between 30% and 60%
    "sales_range": (500_000, 5_000_000)  # Sales between $0.5M and $5M
}

# -----------------------------------------------------
# 2. PORTFOLIO-SPECIFIC OVERRIDES
# -----------------------------------------------------
portfolio_constraints = {
    "Hair/APDO": {
        "min_trend": 0,
        "max_trend": 15,
        "min_contribution": 4,
        "max_contribution": 30
    }
}

# -----------------------------------------------------
# 3. BRAND-SPECIFIC OVERRIDES
# -----------------------------------------------------
brand_constraints = {
    "Bobbi Brown": {
        "min_trend": -1,
        "max_trend": 3,
        "min_contribution": 7,
        "max_contribution": 14
    },
    "Elizabeth Arden": {
        # The image mentions max contribution = 13% or 15%, max trend=7%,
        # you can tweak as needed:
        "min_trend": 0,
        "max_trend": 7,
        "min_contribution": 6,
        "max_contribution": 15
    },
    "Frederic Malle": {
        "min_trend": -3,
        "max_trend": 4
    }
    # Kilian, Balmain, Aveda not explicitly shown with numeric constraints,
    # so they use global defaults unless you'd like to add your own here.
}

# -----------------------------------------------------
# 4. HIERARCHY CHOICES (from the image)
# -----------------------------------------------------
portfolios = [
    "Skin/Body",
    "Fragrance + Color Cosmetics",
    "Hair/APDO"
]

geographies = [
    "North America",
    "Europe",
    "South America",
    "Asia"
]

categories = [
    "Fragrance",
    "Hair Dye",
    "Face Make-Up",
    "Make Up Brushes",
    "Tools"
]

brands = [
    "Kilian",
    "Frederic Malle",
    "Balmain",
    "Bobbi Brown",
    "Aveda",
    "Elizabeth Arden"
]

possible_segments = [
    "Lipstick",
    "Mascara",
    "Toner",
    "Bronzer",
    "Fragrance"
]

# -----------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------
def merge_constraints(global_c, portfolio, brand):
    """
    Merge constraints from global -> portfolio -> brand.
    Priority: brand overrides portfolio overrides global.
    """
    # Start with global
    merged = {
        "min_trend": global_c["min_trend"],
        "max_trend": global_c["max_trend"],
        "min_contribution": global_c["min_contribution"],
        "max_contribution": global_c["max_contribution"]
    }

    # Check if the portfolio has any overrides
    if portfolio in portfolio_constraints:
        pc = portfolio_constraints[portfolio]
        if "min_trend" in pc:
            merged["min_trend"] = pc["min_trend"]
        if "max_trend" in pc:
            merged["max_trend"] = pc["max_trend"]
        if "min_contribution" in pc:
            merged["min_contribution"] = pc["min_contribution"]
        if "max_contribution" in pc:
            merged["max_contribution"] = pc["max_contribution"]

    # Check if the brand has overrides
    if brand in brand_constraints:
        bc = brand_constraints[brand]
        if "min_trend" in bc:
            merged["min_trend"] = bc["min_trend"]
        if "max_trend" in bc:
            merged["max_trend"] = bc["max_trend"]
        if "min_contribution" in bc:
            merged["min_contribution"] = bc["min_contribution"]
        if "max_contribution" in bc:
            merged["max_contribution"] = bc["max_contribution"]

    return merged

# -----------------------------------------------------
# 5. DATA GENERATION
# -----------------------------------------------------
def generate_acme_dataset(num_rows=1000):
    np.random.seed(42)  # for reproducibility
    rows = []

    for _ in range(num_rows):
        # Randomly pick the hierarchy attributes
        portfolio = np.random.choice(portfolios)
        geo = np.random.choice(geographies)
        cat = np.random.choice(categories)
        brand = np.random.choice(brands)
        segment = np.random.choice(possible_segments)

        # Merge constraints from global + portfolio + brand
        final_constraints = merge_constraints(global_constraints, portfolio, brand)

        # Random margin
        margin_low, margin_high = global_constraints["margin_range"]
        margin_value = np.random.randint(margin_low, margin_high + 1)

        # Random initial sales
        sales_low, sales_high = global_constraints["sales_range"]
        sales_value = np.random.randint(sales_low, sales_high + 1)

        # Build one row
        row = {
            "Portfolio": portfolio,
            "Geography": geo,
            "Category": cat,
            "Brand": brand,
            "Segment": segment,
            "Initial_Sales": sales_value,
            "Margin": margin_value,
            "Min_Trend": final_constraints["min_trend"],
            "Max_Trend": final_constraints["max_trend"],
            "Min_Contribution": final_constraints["min_contribution"],
            "Max_Contribution": final_constraints["max_contribution"]
        }
        rows.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(rows)
    return df

# -----------------------------------------------------
# 6. MAIN EXECUTION
# -----------------------------------------------------
if __name__ == "__main__":
    # Generate exactly 1000 rows
    df_acme = generate_acme_dataset(1000)

    print("Sample of generated dataset:")
    print(df_acme.head(10))

    # Save to CSV
    df_acme.to_csv("Acme_Synthetic_Dataset.csv", index=False)
    print("\nSaved 1000-row synthetic dataset to 'Acme_Synthetic_Dataset.csv'.")
