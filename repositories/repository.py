from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')


class Repository(ABC, Generic[T, ID]):
    """
    Generic repository interface for all entities.
    """

    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or update entity"""
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Retrieve entity by ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Retrieve all entities"""
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete entity by ID"""
        pass
