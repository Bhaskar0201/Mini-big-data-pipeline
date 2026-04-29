# import pandas as pd
# from dateutil import parser
# from sqlalchemy import create_engine
# from datetime import datetime

# # =============== CONFIG SECTION ===============
# # Change ONLY your PostgreSQL password here

# DB_USER = "postgres"
# DB_PASSWORD = "your_password"  # <-- change this
# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "database_name"

# CSV_PATH = "studentdata_raw.csv"
# TABLE_NAME = "enrollments_cleaned"


# # =============== EXTRACT STEP ===============

# print("STEP 1: Reading raw CSV file...")

# try:
#     df = pd.read_csv(CSV_PATH)
#     print("CSV loaded successfully.")
#     print("\nRAW DATA:")
#     print(df)
# except FileNotFoundError:
#     print(f"CSV file not found at path: {CSV_PATH}")
#     print("Make sure the file is in the same folder as this script.")
#     raise


# # =============== TRANSFORM STEP ===============

# print("\n STEP 2: Transforming data...")

# def parse_date_safe(date_str):
#     """
#     Try to parse a date string into a proper datetime.
#     If it fails, return NaT (Not a Time).
#     """
#     try:
#         return parser.parse(str(date_str))
#     except Exception:
#         return pd.NaT

# # Parse the order_date column
# df["enrollment_date"] = df["enrollment_date"].apply(parse_date_safe)

# # Convert amount to numeric, invalid values become NaN
# df["fees_paid"] = pd.to_numeric(df["fees_paid"], errors="coerce")

# # Replace missing/NaN amounts with 0
# df["fees_paid"] = df["fees_paid"].fillna(0)

# df["student_name"] = df["student_name"].replace("", "Unknown")
# df["student_name"] = df["student_name"].fillna("Unknown")

# # Drop rows where order_date is NaT (invalid date)
# # df = df.dropna(subset=["enrollment_date"])

# # Convert invalid dates to NaT
# df["enrollment_date"] = pd.to_datetime(df["enrollment_date"], errors="coerce")

# # Replace NaT with today’s date
# today = datetime.today().strftime("%d-%m-%Y")
# df["enrollment_date"] = df["enrollment_date"].fillna(today)

# # Cast order_id to int (if needed)
# df["student_id"] = df["student_id"].astype(int)



# print("Transformation complete.")
# print("\nTRANSFORMED DATA:")
# print(df)


# # =============== LOAD STEP ===============

# print("\n STEP 3: Loading data into PostgreSQL...")

# connection_url = (
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# try:
#     engine = create_engine(connection_url)
#     # append -> add new rows; index=False -> don't write pandas index
#     df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
#     print(f"Data loaded successfully into table '{TABLE_NAME}'.")
# except Exception as e:
#     print("Error while loading data into PostgreSQL:")
#     print(e)
#     raise

# print("\nETL JOB FINISHED SUCCESSFULLY")

