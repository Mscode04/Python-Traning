# Original list of dictionaries
Phones=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

phones = sorted(Phones, key=lambda x: int(x['model']))
print("Sorted list of dictionaries:", phones)
