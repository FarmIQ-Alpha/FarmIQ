# Given data for an example
#this is a test
B = 1000  # Total available subsidy budget ($)
A = 100  # Total available acreage (acres)

# Product information (for simplicity, let's use two products)
P = [2, 4]  # Current prices per unit ($)
r = [0.50, 0.25]  # Expected price increases (decimal)
Y = [20, 10]  # Yields per acre (units)
SSL = [0.75, 0.50]  # Self-sufficiency levels (as decimal)


# Function to calculate the total and per-acre subsidy allocation for each product
def calculate_subsidies(A, B, P, r, Y, SSL):
    # Calculate the adjusted total impact
    adjusted_total_impact = sum(A * Y[i] * SSL[i] * P[i] * r[i] for i in range(len(P)))

    # Calculate the total subsidy for each product
    total_subsidies = [(A * Y[i] * SSL[i] * P[i] * r[i] / adjusted_total_impact) * B for i in range(len(P))]

    # Assuming the acreage for each product is proportionally allocated based on Y and SSL
    allocated_acreage = [A * SSL[i] for i in range(len(P))]  # Simplified allocation based on SSL only for demonstration

    # Calculate the subsidy per acre for each product
    subsidy_per_acre = [total_subsidies[i] / allocated_acreage[i] for i in range(len(P))]

    return total_subsidies, subsidy_per_acre, allocated_acreage


# Execute the calculation
total_subsidies, subsidy_per_acre, allocated_acreage = calculate_subsidies(A, B, P, r, Y, SSL)

# Display the results
print("Total Subsidies for Each Product: ", total_subsidies)
print("Allocated Acreage for Each Product: ", allocated_acreage)
print("Subsidy Per Acre for Each Product: ", subsidy_per_acre)
