wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def staff(person):
    for dept, docs in wards.items():
        if person in docs:
            print(person + " works in " + dept)

staff("Bob")


# """     for staff in wards:
#         if wards['name'] in staff:


#         else:
#             wards[sushi['name']] = {
#                 'price': sushi['price'],
#                 'qty' : 1           }
    
#     for staff, value in wards.item():
#         price = value['price'] * value['qty']
#         print(sushi, value['qty'], price)
