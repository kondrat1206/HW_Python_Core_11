from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        self.current_page = 0
        self.page_size = 0

    def set_page_size(self, page_size):
        self.page_size = page_size

    def __iter__(self):
        self.current_page = 0
        return self

    def __next__(self):
        start_idx = self.current_page * self.page_size
        end_idx = (self.current_page + 1) * self.page_size
        items = list(self.data.items())
        #print(items)

        if start_idx >= len(items):
            raise StopIteration

        self.current_page += 1
        return items[start_idx:end_idx]

# Пример использования:

address_book = AddressBook()
address_book.data = {'John Doe': '123 Main St', 'Jane Smith': '456 Oak Ave', 'Bob Johnson': '789 Elm Blvd', 'Alice Brown': '101 Pine Dr'}
address_book.set_page_size(3)

for page in address_book:
    print("__________NEW____________")
    for el in page:
        print(f"{el[0]} {el[1]}")
    print("__________END____________")
    #print(page)
