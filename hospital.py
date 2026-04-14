wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def staff(person):
    found = False

    staff = {}
    for dept, docs in wards.items():
        if person in docs:
            print(person + " works in " + dept)
            found = True

    if not found:
        print(person + " not found, adding to General Dept")
        wards["General Dept"] = []
        wards["General Dept"].append(person)

staff("Bob")
staff("Justin")

print(wards)

# """     for staff in wards:
#         if wards['name'] in staff:


#         else:
#             wards[sushi['name']] = {
#                 'price': sushi['price'],
#                 'qty' : 1           }
    
#     for staff, value in wards.item():
#         price = value['price'] * value['qty']
#         print(sushi, value['qty'], price)
