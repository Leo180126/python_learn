food_list = [
    ["Bơ", "Pizza", "Sữa"], 
    ["Xúc xích", "Táo", "Kem"], 
    ["Cà rốt", "Bánh đậu", "Cupcake"]
]
search_items = ["Cà rốt", "Táo", "Sữa"]

def search(food_list, search_items):
    for item in search_items:
        for i in range(len(food_list)):
            for j in range(len(food_list[i])):
                if food_list[i][j] == item:
                    print(f"{item} is in {i} {j}")
search(food_list, search_items)
# OUTPUT:
# Cà rốt is in 2 0
# Táo is in 1 1
# Sữa is in 0 2