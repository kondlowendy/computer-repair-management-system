from repositories.repair_repository import RepairRepository


class RepairService:

    def __init__(self):
        self.repository = RepairRepository()

    def create_repair(self, repair):

        if not repair.get("device"):
            raise ValueError("Device is required")

        if repair.get("status") not in ["Pending", "In Progress", "Completed"]:
            raise ValueError("Invalid repair status")

        return self.repository.create(repair)

    def get_all_repairs(self):
        return self.repository.get_all()

    def get_repair(self, repair_id):
        return self.repository.read(repair_id)
