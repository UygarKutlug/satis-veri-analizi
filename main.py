import pandas as pd

from analysis import (
    add_total_price,
    total_revenue,
    revenue_by_category,
    top_selling_products
)

def main():
    df = pd.read_csv("data/sales.csv")

    df = add_total_price(df)

    print("Toplam Ciro:")
    print(total_revenue(df))

    print("\nKategori Bazlı Ciro:")
    print(revenue_by_category(df))

    print("\nEn Çok Satan Ürünler:")
    print(top_selling_products(df))


if __name__ == "__main__":
    main()
