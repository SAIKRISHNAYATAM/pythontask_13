import csv


def write():
    """this is write function"""
    with open("csv_file1.csv", "w", newline="", encoding="utf8") as file:
        fieldnames = ["emp_id", "emp_name", "emp_salary"]
        obj = csv.DictWriter(file, fieldnames=fieldnames)
        obj.writeheader()
        obj.writerow({"emp_id": 21000, "emp_name": "sai", "emp_salary": 60000})
        obj.writerow({"emp_id": 21001, "emp_name": "krishna", "emp_salary": 80000})
        obj.writerow({"emp_id": 21002, "emp_name": "nithin", "emp_salary": 40000})

        def update():
            obj.writerow({"emp_id": 21271, "emp_name": "saikumar", "emp_salary": 20000})
        update()


write()
