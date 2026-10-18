"""This utility tool manages retail or stock inventory levels represented across multiple individual store location
dictionaries. It makes use of key existence checks, safely accesses fields via .get(), and merges multiple stock
records using dictionary comprehension patterns and update operators."""
def main():
    store1 = {"Pen": 20, "Book": 15, "Pencil": 30}
    store2 = {"Pen": 10, "Book": 5, "Eraser": 12}

    print("Store 1:", store1)
    print("Store 2:", store2)

    inventory = {item: store1.get(item, 0) + store2.get(item, 0)
                 for item in store1.keys() | store2.keys()}

    print("\nMerged Inventory:", inventory)

    item = input("\nEnter item to check: ")

    if item in inventory:
        print("Stock Available:", inventory.get(item, 0))
    else:
        print("Item not found!")

    new_item = input("Enter new item: ")
    quantity = int(input("Enter quantity: "))

    inventory.update({new_item: quantity})
    print("\nUpdated Inventory:", inventory)


if __name__ == "__main__":
    main()
