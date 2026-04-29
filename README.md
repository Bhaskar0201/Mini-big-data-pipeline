# Student Enrollment ETL Pipeline

## 📌 Overview

This project implements a simple yet practical **ETL (Extract, Transform, Load)** pipeline using Python. It processes raw student enrollment data from a CSV file, cleans and standardizes it, and loads the transformed data into a PostgreSQL database.

The goal of this project is to demonstrate real-world data engineering practices such as data cleaning, validation, and database integration.

---

## ⚙️ Tech Stack

* **Python**
* **Pandas**
* **PostgreSQL**
* **SQLAlchemy**
* **psycopg2**

---

## 📁 Project Structure

```
etl-student-data/
│── etl.py                # Main ETL script
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .gitignore           # Ignored files
│── .env (optional)      # Environment variables (not committed)
│── studentdata_raw.csv  # Input dataset (optional)
```

---

## 🔄 ETL Workflow

### 1. Extract

* Reads raw data from a CSV file (`studentdata_raw.csv`)
* Loads data into a Pandas DataFrame

### 2. Transform

* Parses and standardizes date values
* Converts fee values to numeric format
* Handles missing or invalid data:

  * Missing fees → replaced with `0`
  * Missing student names → replaced with `"Unknown"`
  * Invalid dates → replaced with current date
* Ensures correct data types for each column

### 3. Load

* Connects to PostgreSQL using SQLAlchemy
* Inserts cleaned data into the target table (`enrollments_cleaned`)
* Appends new records without overwriting existing data

---

## 🔐 Environment Variables (Recommended)

To keep sensitive information secure, use environment variables instead of hardcoding credentials.

### Example `.env` file:

```
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/etl-student-data.git
cd etl-student-data
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set environment variables

* Create a `.env` file or export variables manually

### 4. Run the ETL script

```
python etl.py
```

---

## 🧪 Example Output

* Raw CSV data is cleaned and transformed
* Cleaned data is successfully inserted into PostgreSQL table:

  ```
  enrollments_cleaned
  ```

## 🚀 Future Improvements

* Add logging instead of print statements
* Implement data validation checks
* Schedule ETL using cron or Airflow
* Add unit tests for transformation logic
* Dockerize the application for easier deployment

---

## 👨‍💻 Author

Bhaskar

---

## 📄 License

This project is open-source and available under the MIT License.
