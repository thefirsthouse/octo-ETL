## 📦 ETL Pipeline for Orders Data
A simple ETL (Extract, Transform, Load) pipeline for processing raw order data and generating aggregated statistics per user.
### 🚀 Overview
This project implements a data processing pipeline that:
1. Extracts raw data from a CSV file
2. Validates the structure of the dataset
3. Cleans invalid and inconsistent records
4. Transforms data by adding calculated fields
5. Aggregates data to generate user-level statistics
6. Loads the processed data into a new CSV file
### Pipeline Architecture
```
Extract -> Validate -> Clean -> Transform -> Aggregate -> Load
```
### 📂 Project Structure
```
.
|- main.py         # CLI entry point
|- pipeline.py     # Orchestrates the ETL process
|- steps.py        # Individual ETL steps
|- config.py
|_ data.py         # Input/output data (optional)
```
### ⚙️ Installatiom
Make sure you have Python 3.8+ installed.
Install dependencies:
``` bash
pip install -r requirements.txt
```
### ▶️ Usage
Run the pipeline via CLI:
``` bash
python main.py --input data/orders.csv --output data/result.csv
```
### 📊 Example Input
``` csv
user_id,product,price,quantity,date
1,Laptop,999.99,1,2024-06-01
2,Phone,499.99,2,2024-06-02
...
```
### 📈 Example Output
``` csv
user_id,total_spent
1,999.99
2,999.98
...
```
## 🔍 Data Processing Details
### ✅ Validation
- Checks if required columns exist
- Ensures dataset is not empty
### 🧹 Cleaning
- Removes rows with missing values
- Drops duplicates
- Filters invalid data (price ≤ 0, quantity ≤ 0)
- Removes invalid dates
### 🔧 Transformation
- Adds `total = price * quantity`
### 📊 Aggregation
- Groups data by `user_id`
- Calculates total spending per user