data = input()

company_data = {}

while data != "End":
    company_name, employee_id = data.split(" -> ")

    if company_name not in company_data:
        company_data[company_name] = []

    if employee_id not in company_data[company_name]:
        company_data[company_name].append(employee_id)

    data = input()

sorted_company_data = sorted(company_data.items(), key=lambda kvpt: kvpt[0])

for company_names, employee_ids in sorted_company_data:
    print(company_names)

    for employee_id in employee_ids:
        print(f"-- {employee_id}")