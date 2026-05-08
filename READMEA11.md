# Assignment 11 – Repository Layer Implementation

## Overview

This assignment implements a **Repository Layer** to decouple business logic from data persistence in the Computer Repair Management System. The goal is to introduce a flexible and scalable architecture that allows switching between different storage mechanisms without modifying the core application logic.

---

## Architecture Design

The system follows a **Layered Architecture** with the Repository Pattern as the persistence abstraction layer:

## Repository Pattern

A generic repository interface defines standard CRUD operations used across all entities:

- save(entity)
- find_by_id(id)
- find_all()
- delete(id)

This ensures consistency and avoids duplication across repository implementations.

## In-Memory Implementation

The current system uses an in-memory repository implementation.

It:
- Uses a Python dictionary as a HashMap
- Stores entities using their unique ID as the key
- Supports full CRUD operations
- Is suitable for development and testing

Example:

## Factory Pattern (Storage Abstraction)

A Factory Pattern is used to manage repository creation.

The RepositoryFactory returns the correct implementation based on configuration:

- "MEMORY" → In-memory repository
- "DATABASE" → Future database implementation (stub)

This allows storage switching without modifying service logic.

## Service Layer Integration

Services do not directly instantiate repositories. Instead, repositories are accessed through the factory:

```python
self.repo = RepositoryFactory.get_repair_job_repository("MEMORY")
repositories/
    repository.py
    repair_job_repository.py
    inmemory/
        in_memory_repair_job_repository.py
    filesystem/ (future)

factories/
    RepositoryFactory.py

services/
    repair_job_service.py

---

# Key point you were missing

A README file:
- is ONE file
- but can contain MANY sections and code blocks

So what you copy is:
> one file → many sections inside it

---

If you want, I can next help you:
✔ :contentReference[oaicite:0]{index=0}  
✔ or :contentReference[oaicite:1]{index=1}  
✔ or :contentReference[oaicite:2]{index=2}  

Just say 
