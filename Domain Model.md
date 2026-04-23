## Domain Model

| Entity       | Attributes                                                                 | Methods (Responsibilities)                          | Relationships |
|--------------|---------------------------------------------------------------------------|----------------------------------------------------|--------------|
| Customer     | customerId, name, email, phone                                            | register(), updateDetails()                        | Creates RepairJobs |
| Technician   | technicianId, name, specialization, availability                          | assignJob(), updateStatus()                        | Handles RepairJobs |
| Device       | deviceId, type, brand, model, serialNumber                                | registerDevice(), updateDeviceInfo()               | Belongs to Customer |
| RepairJob    | jobId, status, issueDescription, dateCreated, priority                    | createJob(), updateStatus(), assignTechnician()    | Central entity |
| Invoice      | invoiceId, amount, status, dateIssued                                     | generateInvoice(), calculateTotal()                | Linked to RepairJob |
| Payment      | paymentId, amount, paymentMethod, paymentDate                             | processPayment(), validatePayment()                | Linked to Invoice |
