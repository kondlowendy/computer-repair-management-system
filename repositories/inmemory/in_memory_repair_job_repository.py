from typing import Dict, Optional, List
from repositories.repair_job_repository import RepairJobRepository
from domain.repair_job import RepairJob


class InMemoryRepairJobRepository(RepairJobRepository):

    def __init__(self):
        self._storage: Dict[str, RepairJob] = {}

    def save(self, entity: RepairJob) -> None:
        self._storage[entity.id] = entity

    def find_by_id(self, id: str) -> Optional[RepairJob]:
        return self._storage.get(id)

    def find_all(self) -> List[RepairJob]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    # 🔥 NEW METHODS (IMPORTANT)

    def find_by_status(self, status: str) -> List[RepairJob]:
        return [job for job in self._storage.values() if job.status == status]

    def find_by_customer(self, customer_id: str) -> List[RepairJob]:
        return [job for job in self._storage.values() if job.customer_id == customer_id]
