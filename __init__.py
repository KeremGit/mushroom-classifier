
boolean_options = ['t','f']
schema = {
    'class': {'target': True, 'categories': ['e','p']},
    'cap-shape': {'categories': ['x', 'f', 's', 'b', 'o']}, 
    'cap-surface': {'categories': ['t', 's', 'y', 'h', 'g']}, 
    'cap-color': {'categories': ['n', 'y', 'w', 'g', 'e']}, 
    'gill-attachment': {'categories': ['a', 'd', 'x', 'e', 's']}, 
    'gill-spacing': {'categories': ['c', 'd', 'f', 'e', 'a']}, 
    'gill-color': {'categories': ['w', 'n', 'y', 'p', 'g']}, 
    'stem-root': {'categories': ['b', 's', 'r', 'c', 'f']}, 
    'stem-surface': {'categories': ['s', 'y', 'i', 't', 'g']}, 
    'stem-color': {'categories': ['w', 'n', 'y', 'g', 'o']}, 
    'veil-type': {'categories': ['u', 'w', 'a', 'e', 'f']}, 
    'veil-color': {'categories': ['w', 'y', 'n', 'u', 'k']}, 
    'ring-type': {'categories': ['f', 'e', 'z', 'l', 'r']}, 
    'spore-print-color': {'categories': ['k', 'p', 'w', 'n', 'r']}, 
    'habitat': {'categories': ['d', 'g', 'l', 'm', 'h']}, 
    'season': {'categories': ['a', 'u', 'w', 's']}, 
    'does-bruise-or-bleed': {'categories': boolean_options}, 
    'has-ring': {'categories': boolean_options},
     'cap-diameter': {},
    'stem-height': {},
    'stem-width': {},
}

for column_name, properties in schema.items():
    target = properties.get('target', False)
    categories = properties.get('categories', [])
    
    if(target):
        print(f"filter out all df rows where df[target] is not in {categories}")
        
    elif(len(categories) > 0):
        print(f"convert column to str")
        print(f"filter out all values not in {categories}")
    else:
        print(f"filter out non-numerical values")

