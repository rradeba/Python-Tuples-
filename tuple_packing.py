# task 3 
#inforation from orders 
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("James", "Charger", 1),
    ("Mark", "Gaming Console", 1 ),
    ("Tyler", "TV", 3 )
]


#unpack tuple and print formatted information

for i, ind_order in enumerate(orders, 1):
        order_name = ind_order[0]
        order_item = ind_order[1]
        order_quant = ind_order[2]
        item_num = str(i)
        print(f"Order {item_num} - {order_quant} {order_item} for {order_name}")
