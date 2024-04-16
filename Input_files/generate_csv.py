import csv
import random

# Function to generate random data for each attribute
def generate_data():
    Provider_Name = "Provider" + str(random.randint(1, 1000))
    NPI = str(random.randint(1000000000, 9999999999))
    Medicaid_EP_Hospital_Type = random.choice(["Type A", "Type B", "Type C"])
    Specialty = random.choice(["Specialty 1", "Specialty 2", "Specialty 3"])
    Business_Street_Address = "Address" + str(random.randint(1, 1000))
    Business_City = "City" + str(random.randint(1, 100))
    Business_County = "County" + str(random.randint(1, 50))
    Business_ZIP_Code = str(random.randint(10000, 99999))
    Business_State_Territory = random.choice(["State A", "State B", "State C"])
    Program_Year = random.randint(2019, 2023)
    Payment_Year = random.randint(2019, 2023)
    Payment_Year_Number = random.randint(1, 4)
    Payment_Criteria_Medicaid_Only = random.choice(["Yes", "No"])
    Payee_Name = "Payee" + str(random.randint(1, 1000))
    Payee_NPI = str(random.randint(1000000000, 9999999999))
    Disbursement_Amount = round(random.uniform(1000, 10000), 2)
    Total_Payments = round(random.uniform(10000, 100000), 2)
    Longitude = round(random.uniform(-180, 180), 6)
    Latitude = round(random.uniform(-90, 90), 6)
    
    return [Provider_Name, NPI, Medicaid_EP_Hospital_Type, Specialty, Business_Street_Address, Business_City, Business_County, Business_ZIP_Code, Business_State_Territory, Program_Year, Payment_Year, Payment_Year_Number, Payment_Criteria_Medicaid_Only, Payee_Name, Payee_NPI, Disbursement_Amount, Total_Payments, Longitude, Latitude]

# Generate data for 10,000 records
data = [generate_data() for _ in range(10)]

# Write data to CSV file
with open('Input_files/records.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Provider_Name", "NPI", "Medicaid_EP_Hospital_Type", "Specialty", "Business_Street_Address", "Business_City", "Business_County", "Business_ZIP_Code", "Business_State_Territory", "Program_Year", "Payment_Year", "Payment_Year_Number", "Payment_Criteria__Medicaid_Only", "Payee_Name", "Payee_NPI", "Disbursement_Amount", "Total_Payments", "Longitude", "Latitude"])
    # Write data
    writer.writerows(data)

print("CSV file generated successfully!")
