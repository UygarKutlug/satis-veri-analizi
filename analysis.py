def add_total_price(df):
    df["total_price"] = df["quantity"] * df["unit_price"]
    return df


def total_revenue(df):
    return df["total_price"].sum()


def revenue_by_category(df):
    return df.groupby("category")["total_price"].sum()


def top_selling_products(df, n=3):
    return (
        df.groupby("product")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
