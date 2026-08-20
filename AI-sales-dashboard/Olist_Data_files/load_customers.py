from mssql_python import connect
import csv

CSV_FILE = r"C:\Users\Metodi\Downloads\Olist_BI_Automation\olist_products_dataset.csv"

SQL_SERVER = "olist-dba-metodi.database.windows.net"
DATABASE = "olist-db"

connection_string = (
    f"Server={SQL_SERVER};"
    f"Database={DATABASE};"
    "Authentication=ActiveDirectoryDefault;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

print("Reading CSV...")

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.DictReader(file)

    with connect(connection_string) as conn:

        cursor = conn.cursor()

        insert_sql = """
            INSERT INTO raw.products
            (
                product_id,
                product_category_name,
                product_name_lenght,
                product_description_lenght,
                product_photos_qty,
                product_weight_g,
                product_length_cm,
                product_height_cm,
                product_width_cm
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        rows = []

        for row in reader:
            rows.append((
                row["product_id"],
                row["product_category_name"] or None,
                int(row["product_name_lenght"]) if row["product_name_lenght"] else None,
                int(row["product_description_lenght"]) if row["product_description_lenght"] else None,
                int(row["product_photos_qty"]) if row["product_photos_qty"] else None,
                int(row["product_weight_g"]) if row["product_weight_g"] else None,
                int(row["product_length_cm"]) if row["product_length_cm"] else None,
                int(row["product_height_cm"]) if row["product_height_cm"] else None,
                int(row["product_width_cm"]) if row["product_width_cm"] else None
            ))

        print(f"Uploading {len(rows)} products...")

        cursor.executemany(insert_sql, rows)
        conn.commit()

print(f"SUCCESS: {len(rows)} products uploaded!")