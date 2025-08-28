import os
import csv
import random
import string
from datetime import datetime, timedelta
from PIL import Image, ImageDraw

# Output folders
os.makedirs("data/structured", exist_ok=True)
os.makedirs("data/unstructured", exist_ok=True)
os.makedirs("data/multimodal/product_images", exist_ok=True)

PRODUCT_IDS = [f"P{1000+i}" for i in range(100)]
SUPPLIERS = ["SupplierA", "SupplierB", "SupplierC"]
CATEGORIES = ["Electronics", "Home", "Appliances", "Toys"]
LANGUAGES = ["en", "fr", "zh", "es"]

def generate_product_catalog():
    with open("data/structured/product_catalog.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "Name", "Category", "Price", "Weight", "Supplier"])
        for pid in PRODUCT_IDS:
            writer.writerow([
                pid,
                f"Product-{pid}",
                random.choice(CATEGORIES),
                round(random.uniform(10, 1000), 2),
                round(random.uniform(0.5, 5.0), 2),
                random.choice(SUPPLIERS)
            ])

def generate_sales_data():
    with open("data/structured/sales_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "UnitsSold", "Region", "Date"])
        for _ in range(1000):
            writer.writerow([
                random.choice(PRODUCT_IDS),
                random.randint(1, 50),
                random.choice(["US", "EU", "IN", "CN"]),
                (datetime.today() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
            ])

def generate_return_claims():
    with open("data/structured/return_claims.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ReturnID", "ProductID", "Reason", "Approved", "ReturnImagePath"])
        for i in range(300):
            img_name = f"img_{1000+i}.jpg"
            writer.writerow([
                f"R{i+1}",
                random.choice(PRODUCT_IDS),
                random.choice(["Damaged", "Defective", "Fake", "Wrong Item"]),
                random.choice(["Yes", "No"]),
                f"product_images/{img_name}"
            ])

def generate_warranty_claims():
    issues = ["Overheating", "Stopped Working", "Battery Drain", "Display Flicker"]
    with open("data/structured/warranty_claims.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "IssueDescription", "DateClaimed", "Outcome"])
        for _ in range(300):
            writer.writerow([
                random.choice(PRODUCT_IDS),
                random.choice(issues),
                (datetime.today() - timedelta(days=random.randint(0, 730))).strftime("%Y-%m-%d"),
                random.choice(["Approved", "Rejected", "Pending"])
            ])

def generate_customer_reviews():
    reviews = [
        "This product gets very hot when charging.",
        "Too noisy and unreliable.",
        "Excellent build quality!",
        "Battery swells after 6 months.",
        "Seems like a knock-off product.",
    ]
    with open("data/unstructured/customer_reviews.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "Language", "ReviewText"])
        for _ in range(500):
            writer.writerow([
                random.choice(PRODUCT_IDS),
                random.choice(LANGUAGES),
                random.choice(reviews)
            ])

def generate_support_tickets():
    issues = [
        "Customer reported overheating after 2 days.",
        "Received wrong product in packaging.",
        "Warranty not honored.",
        "Fake product returned for refund.",
        "Broken item in box.",
    ]
    with open("data/unstructured/support_tickets.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["TicketID", "ProductID", "IssueText"])
        for i in range(200):
            writer.writerow([
                f"TCKT{i+1}",
                random.choice(PRODUCT_IDS),
                random.choice(issues)
            ])

def generate_regulatory_notices():
    notices = [
        "CPSC has recalled batch #A2341 due to overheating issues.",
        "FDA warns about mislabeled ingredients in products sold after Jan 2023.",
        "CE regulation updated: All electric toys must carry label X12.",
        "Import ban on items not following new packaging norms from July 2024."
    ]
    with open("data/unstructured/regulatory_notices.txt", "w") as f:
        for line in notices:
            f.write(f"{line}\n")

def generate_product_images():
    for i in range(1000, 1300):
        img = Image.new("RGB", (128, 128), (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255)))
        draw = ImageDraw.Draw(img)
        draw.text((10, 50), f"ID {i}", fill=(0, 0, 0))
        img.save(f"data/multimodal/product_images/img_{i}.jpg")

# Execute all generators
generate_product_catalog()
generate_sales_data()
generate_return_claims()
generate_warranty_claims()
generate_customer_reviews()
generate_support_tickets()
generate_regulatory_notices()
generate_product_images()

print("✅ Mock data generated in /data/")
