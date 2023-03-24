import math
class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.page = []
        self.info = []
        i = 0
        for x in self.collection:
            if len(self.info) < self.items_per_page - 1 :
                print(len(self.info))
                print(self.items_per_page)
                self.info.append(x)
            
            else:
                self.info.append(self.collection[(items_per_page - 1) + (i * items_per_page)])
                self.page.append(self.info)
                self.info = []
                i += 1

        if len(self.info) > 0:
            self.page.append(self.info)

    # returns the number of items within the entire collection
    def item_count(self):
        
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        
        return math.ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return len(self.page[page_index])

        except:
            return -1


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        j = 0
        
        for i, page in enumerate(self.page):
            
            for thing in page:
                if j == item_index:
                    return i
                j+=1

        return -1