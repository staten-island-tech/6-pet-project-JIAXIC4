wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def staff(person):
    found = False

    for dept, docs in wards.items():
        if person in docs:
            print(person + " works in " + dept)
            found = True

    if not found:
        print(person + " not found, adding to General")
        if "General" not in wards:
            wards["General"] = []
        wards["General"].append(person)

staff("Bob")
staff("Zoe")

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
