# Define tax rate
SALES_TAX_RATE = 0.07

# Set prices for all items
bread = 10.00
apples = 6.00
cake = 13.00
cookies = 9.00
carrots = 6.00

# Calculate subtotal
subtotal = bread + apples + cake + cookies + carrots

# Calculate sales tax
tax = subtotal * SALES_TAX_RATE

# Calculate total
total = subtotal + tax

# Display results
print("Subtotal: ${:.2f}".format(subtotal))
print("Sales Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total))
