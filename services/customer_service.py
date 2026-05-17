from repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    def create_customer(self, customer):

        if not customer.get("email"):
            raise ValueError("Customer email is required")

        return self.repository.create(customer)

    def get_all_customers(self):
        return self.repository.get_all()

    def get_customer(self, customer_id):
        return self.repository.read(customer_id)
