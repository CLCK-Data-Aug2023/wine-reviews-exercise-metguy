import pandas as pd

wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

wine_reviews.points.describe()

average_points = wine_reviews.groupby("country").points.mean().round(1)

print(average_points)

average_count = wine_reviews.groupby("country").points.count()

print(average_count)

result = pd.DataFrame()
result["count"] = average_count
result["point"] = average_points

print(result)

result.to_csv('data/reviews-per-country.csv', index=True)