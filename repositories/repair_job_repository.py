from typing import List
from repositories.repository import Repository
from domain.repair_job import RepairJob


class RepairJobRepository(Repository[RepairJob, str]):
    """
    Entity-specific repository for RepairJob.
    """

    def find_by_status(self, status: str) -> List[RepairJob]:
        pass

    def find_by_customer(self, customer_id: str) -> List[RepairJob]:
        pass
