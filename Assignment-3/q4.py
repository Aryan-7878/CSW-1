# Function to process sales data using *args and **kwargs

def process_sales(*args, **kwargs):
    # Calculate total sales
    total_sales = sum(args)
    
    # Count number of extra info items
    extra_info_count = len(kwargs)
    
    # Display results
    print(f"Total Sales Amount: {total_sales}")
    print(f"Number of Extra Information Items: {extra_info_count}")
    print("Extra Information Provided:")
    
    # Print each key-value pair in kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage
process_sales(3000, 2500, 7000, Name="John Doe", Wife="Fuck Hoe",Date="2025-11-01", Location="Bhubaneswar")