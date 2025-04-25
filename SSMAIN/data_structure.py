
class node:
    def __init__(self, img_url , product_name, club_charge, product_price):
        self.product_name = product_name
        self.club_charge = club_charge
        self.product_price = product_price
        self.total_price = club_charge + product_price
        self.product_img = img_url
        self.next = None 

class linked_list:

    def __init__(self):
        self.head = None 

    def add_product(self,img_url,product_name, club_charge, product_price ):
        new_node = node(img_url,product_name, club_charge, product_price)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def get_head(self):
        return self.head

    def serialize(self):
        serialized_data = []
        current = self.head
        while current:
            serialized_data.append({
                "product_img":current.product_img,
                "product_name": current.product_name,
                "club_charge": float(current.club_charge),
                "product_price": float(current.product_price),
                "total_price": current.total_price,
            })
            current = current.next
        return serialized_data 

    def deserialize(self, data):
        for item in data:
            self.add_product(item["product_img"],item["product_name"], item["club_charge"], item["product_price"])
        return self 


    


