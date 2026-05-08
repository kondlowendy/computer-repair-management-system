from repositories.repair_job_repository import RepairJobRepository

class InMemoryRepairJobRepository(RepairJobRepository):

    def __init__(self):
        self._storage = {}

    def save(self, entity):
        self._storage[entity.id] = entity

    def find_by_id(self, id):
        return self._storage.get(id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, id):
        if id in self._storage:
            del self._storage[id]
