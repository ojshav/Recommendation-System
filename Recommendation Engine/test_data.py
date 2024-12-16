import csv
import random
import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Constants
NUM_ROWS = 30000
CATEGORIES = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Tablet'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Sweater'],
    'Home & Kitchen': ['Blender', 'Toaster', 'Cookware Set', 'Vacuum Cleaner', 'Coffee Maker'],
    'Books': ['Fiction', 'Non-Fiction', 'Biography', 'Self-Help', 'Mystery'],
    'Beauty': ['Lipstick', 'Moisturizer', 'Perfume', 'Shampoo', 'Foundation'],
    'Sports': ['Football', 'Basketball', 'Tennis Racket', 'Yoga Mat', 'Running Shoes'],
    'Toys': ['Action Figure', 'Board Game', 'Doll', 'Puzzle', 'Remote Car']
}
PAYMENT_METHODS = ['Credit Card', 'Debit Card', 'PayPal', 'Cash on Delivery']
AGE_GROUPS = ['18-25', '26-35', '36-45', '46-60', '60+']
GENDERS = ['Male', 'Female', 'Other']


def generate_user_data(num_rows):
    """Generate user demographic and profile data"""
    users = []
    used_user_ids = set()

    for _ in range(num_rows):
        while True:
            user_id = fake.uuid4()
            if user_id not in used_user_ids:
                used_user_ids.add(user_id)
                break

        email = fake.email() if random.random() > 0.1 else np.nan

        users.append([
            user_id,
            fake.first_name(),
            fake.last_name(),
            email,
            random.choice(GENDERS),
            random.choice(AGE_GROUPS),
            fake.city(),
            fake.country(),
            fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
        ])

    return users


def generate_product_data(num_rows):
    """Generate realistic product information"""
    products = []
    used_product_ids = set()

    for _ in range(num_rows):
        while True:
            product_id = fake.uuid4()
            if product_id not in used_product_ids:
                used_product_ids.add(product_id)
                break

        category = random.choice(list(CATEGORIES.keys()))
        product_name = random.choice(CATEGORIES[category])
        base_price = round(random.uniform(10, 1000), 2)

        # Introduce outliers and NaN
        if random.random() < 0.05:
            base_price = base_price * random.uniform(2, 5)  # Outlier
        if random.random() < 0.05:
            base_price = np.nan

        discount_amount = round(base_price * random.uniform(0, 0.3), 2) if base_price is not np.nan else np.nan

        products.append([
            product_id,
            product_name,
            category,
            base_price,
            discount_amount,
            random.randint(1, 500),
            fake.sentence(nb_words=10)
        ])

    return products


def generate_transaction_data(users, products, num_rows):
    """Generate transaction data"""
    transactions = []

    for _ in range(num_rows):
        user_id = random.choice(users)[0]
        product = random.choice(products)
        product_id = product[0]
        product_price = product[3]

        if not pd.isna(product_price):
            transaction_amount = round(product_price * random.uniform(0.9, 1.1), 2)
        else:
            transaction_amount = round(random.uniform(10, 1000), 2)

        # Introduce outliers and NaN
        if random.random() < 0.05:
            transaction_amount = transaction_amount * random.uniform(2, 5)  # Outlier
        if random.random() < 0.05:
            transaction_amount = np.nan

        discount_amount = round(transaction_amount * random.uniform(0, 0.3), 2) if transaction_amount is not np.nan else np.nan

        transactions.append([
            fake.uuid4(),
            user_id,
            product_id,
            transaction_amount,
            random.choice(PAYMENT_METHODS),
            fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
            random.randint(1, 14),
            discount_amount
        ])

    return transactions


def generate_interaction_data(users, products, num_rows):
    """Generate user interaction data"""
    interactions = []

    for _ in range(num_rows):
        user_id = random.choice(users)[0]
        product_id = random.choice(products)[0]
        time_spent_on_pages = round(random.uniform(1, 120), 2)

        # Introduce outliers and NaN
        if random.random() < 0.05:
            time_spent_on_pages = time_spent_on_pages * random.uniform(2, 5)  # Outlier
        if random.random() < 0.05:
            time_spent_on_pages = np.nan

        interactions.append([
            fake.uuid4(),
            user_id,
            product_id,
            random.randint(1, 20),
            random.randint(5, 100),
            random.randint(1, 20),
            time_spent_on_pages,
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(1, 5) if random.random() > 0.2 else np.nan,
            fake.sentence(nb_words=10) if random.random() > 0.2 else ''
        ])

    return interactions

# Generate data
print("Generating data...")
user_data = generate_user_data(NUM_ROWS)
product_data = generate_product_data(len(CATEGORIES) * 50)
transaction_data = generate_transaction_data(user_data, product_data, NUM_ROWS)
interaction_data = generate_interaction_data(user_data, product_data, NUM_ROWS)

# Prepare file paths
user_file = 'test_user_data.csv'
product_file = 'test_product_data.csv'
transaction_file = 'test_transaction_data.csv'
interaction_file = 'test_interaction_data.csv'

# Write datasets to CSV files
def write_csv(file_path, data, headers):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

write_csv(user_file, user_data, ['UserID', 'FirstName', 'LastName', 'Email', 'Gender', 'AgeGroup', 'City', 'Country', 'DateOfBirth'])
write_csv(product_file, product_data, ['ProductID', 'ProductName', 'Category', 'BasePrice', 'DiscountAmount', 'StockQuantity', 'Description'])
write_csv(transaction_file, transaction_data, ['TransactionID', 'UserID', 'ProductID', 'TransactionAmount', 'PaymentMethod', 'PurchaseDate', 'DeliveryTime', 'DiscountAmount'])
write_csv(interaction_file, interaction_data, ['InteractionID', 'UserID', 'ProductID', 'ViewedPages', 'ProductViewHistory', 'SearchQueries', 'TimeSpentOnPages', 'WishlistItems', 'CartAddedItems', 'CartAbandonedItems', 'ReviewRating', 'ReviewText'])

print(f"Data with realistic product information saved to:")
print(f"1. {user_file}")
print(f"2. {product_file}")
print(f"3. {transaction_file}")
print(f"4. {interaction_file}")
