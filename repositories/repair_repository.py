class RepairRepository:

    def __init__(self):
        self.repairs = []

    def create(self, repair):
        self.repairs.append(repair)
        return repair

    def get_all(self):
        return self.repairs

    def read(self, repair_id):
        for repair in self.repairs:
            if repair["repair_id"] == repair_id:
                return repair
        return None
