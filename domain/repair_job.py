class RepairJob:
    def __init__(self, id: str, description: str, status: str = "Pending", customer_id: str = ""):
        self.id = id
        self.description = description
        self.status = status
        self.customer_id = customer_id

    def __eq__(self, other):
        return isinstance(other, RepairJob) and self.id == other.id

    def __repr__(self):
        return f"RepairJob(id={self.id}, status={self.status})"
