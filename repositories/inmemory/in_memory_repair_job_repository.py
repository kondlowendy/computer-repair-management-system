class InMemoryRepairJobRepository:

    def __init__(self):
        self.repairs = []

    def save(self, repair):
        self.repairs.append(repair)
        return repair

    def find_by_status(self, status):
        return [
            repair for repair in self.repairs
            if repair.status == status
        ]

    def find_by_customer(self, customer_id):
        return [
            repair for repair in self.repairs
            if repair.customer_id == customer_id
        ]
