from repositories.inmemory.in_memory_repair_job_repository import InMemoryRepairJobRepository


class RepairJob:
    def __init__(self, id, description, status="Pending", customer_id="C1"):
        self.id = id
        self.description = description
        self.status = status
        self.customer_id = customer_id


def test_find_by_status():
    repo = InMemoryRepairJobRepository()

    repo.save(RepairJob("1", "Repair A", status="Pending"))
    repo.save(RepairJob("2", "Repair B", status="Completed"))

    results = repo.find_by_status("Pending")

    assert len(results) == 1
    assert results[0].id == "1"


def test_find_by_customer():
    repo = InMemoryRepairJobRepository()

    repo.save(RepairJob("1", "Repair A", customer_id="C1"))
    repo.save(RepairJob("2", "Repair B", customer_id="C2"))

    results = repo.find_by_customer("C1")

    assert len(results) == 1
    assert results[0].id == "1"
