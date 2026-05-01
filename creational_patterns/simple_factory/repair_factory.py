from src.repair_job import RepairJob

class RepairFactory:
    @staticmethod
    def create_repair(repair_type, description):
        if repair_type == "screen":
            return RepairJob(description, "Screen Repair")
        elif repair_type == "battery":
            return RepairJob(description, "Battery Replacement")
        else:
            raise ValueError("Invalid repair type")
