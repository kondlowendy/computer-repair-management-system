class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def update_details(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
