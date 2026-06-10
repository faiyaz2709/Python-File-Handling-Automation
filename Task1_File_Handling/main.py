import os
import shutil
import csv

# Create text file
with open("data.txt", "w") as file:
    file.write("Hello Internship")

# Read file
with open("data.txt", "r") as file:
    print(file.read())

# Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Faiyaz", 18])

# Create backup folder
os.makedirs("backup", exist_ok=True)

# Rename file
os.rename("data.txt", "new_data.txt")

# Move file
shutil.move("new_data.txt", "backup/new_data.txt")

print("Task completed successfully")
