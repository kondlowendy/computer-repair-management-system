# Domain Model
The RepairJob entity acts as the central component of the system.

## Entities

| Entity       | Attributes                                                                 | Methods (Responsibilities)                          | Relationships |
|--------------|---------------------------------------------------------------------------|----------------------------------------------------|--------------|
| Customer     | customerId, name, email, phone                                            | register(), updateDetails()                        | Creates RepairJobs |
| Technician   | technicianId, name, specialization, availability                          | assignJob(), updateStatus()                        | Handles RepairJobs |
| Device       | deviceId, type, brand, model, serialNumber                                | registerDevice(), updateDeviceInfo()               | Belongs to Customer |
| RepairJob    | jobId, status, issueDescription, dateCreated, priority                    | createJob(), updateStatus(), assignTechnician()    | Central entity |
| Invoice      | invoiceId, amount, status, dateIssued                                     | generateInvoice(), calculateTotal()                | Linked to RepairJob |
| Payment      | paymentId, amount, paymentMethod, paymentDate                             | processPayment(), validatePayment()                | Linked to Invoice |

## Relationships

- A Customer can create multiple RepairJobs (1..*)
- Each RepairJob belongs to exactly one Customer (1)
- Each RepairJob is associated with one Device (1)
- A Technician can handle multiple RepairJobs (0..*)
- A RepairJob may be assigned to one Technician (0..1)
- Each RepairJob generates exactly one Invoice (1)
- An Invoice can have one or more Payments (1..*)

## Business Rules

1. A customer must be registered before creating a repair job.
2. Each repair job must include a valid issue description.
3. A technician can only be assigned if they are available.
4. A repair job must be completed before an invoice is finalized.
5. Payments cannot exceed the total invoice amount.
6. A device must be registered before a repair job is created.
7. Each repair job must be linked to exactly one invoice.
