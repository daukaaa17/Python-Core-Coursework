from operator import index
class Pagination:
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page

    def page_count(self):
        a = len(self.data)
        if a % self.items_on_page == 0:
            n = a // self.items_on_page
        else:
            n = a // self.items_on_page + 1
        return n
    def item_count(self):
        return len(self.data)
    def count_items_on_page(self, page_number):
        if page_number > self.page_count() - 1:
            raise Exception("Invalid index. Page is missing.")
        else:
            if page_number < self.page_count() - 1:
                return self.items_on_page
            elif page_number == self.page_count() - 1:
                return len(self.data) // self.items_on_page + 1
            else:
                return len(self.data) % self.items_on_page

    def find_page(self, data):
        if data in self.data :
            parts = [self.data[i:i + self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]
            print(type(parts))
            c = []
            for part in parts:
                if len(data) < self.items_on_page:
                    if data in part:
                        c.append(parts.index(part))
                else:
                    z = [data[i:i + self.items_on_page] for i in range(0, len(data), self.items_on_page)]
                    for sukas in z:
                        if sukas in part:
                            c.append(parts.index(part))
            return c
        else:
            raise Exception('\'{}\' is missing on the pages'.format(data))

    def display_page(self, page_number):
        parts2 = [self.data[i:i + self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]
        return (parts2[page_number])
# pages = Pagination('Your beautiful text', 5)
# print(pages.page_count())
# print(pages.count_items_on_page(4))
# print(pages.find_page('beautiful'))
# print(pages.display_page(0))
