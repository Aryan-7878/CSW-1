# Define a generator function to yield high sales
def filter_high_sales(sales, threshold):
    for amount in sales:
        if amount >= threshold:
            yield amount  # yield returns one value at a time


# Demonstration
daily_sales = [250, 800, 450, 1200, 600]
threshold = 500

print(f"Daily Sales: {daily_sales}")
print(f"Threshold: {threshold}")
print("High Sales:")

# Use the generator and print each high sale
for sale in filter_high_sales(daily_sales, threshold):
    print(sale)