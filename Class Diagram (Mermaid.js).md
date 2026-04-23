# Class Diagram

```mermaid
classDiagram

class Customer {
- customerId: String
- name: String
- email: String
- phone: String
+ register()
+ updateDetails()
}

class Technician {
- technicianId: String
- name: String
- specialization: String
- availability: Boolean
+ assignJob()
+ updateStatus()
}

class Device {
- deviceId: String
- type: String
- brand: String
- model: String
- serialNumber: String
+ registerDevice()
+ updateDeviceInfo()
}

class RepairJob {
- jobId: String
- status: String
- issueDescription: String
- priority: String
- dateCreated: Date
+ createJob()
+ updateStatus()
+ assignTechnician()
}

class Invoice {
- invoiceId: String
- amount: Double
- status: String
- dateIssued: Date
+ generateInvoice()
+ calculateTotal()
}

class Payment {
- paymentId: String
- amount: Double
- paymentMethod: String
- paymentDate: Date
+ processPayment()
+ validatePayment()
}

Customer "1" --> "0..*" RepairJob : creates
RepairJob "1" --> "1" Device : for
Technician "1" --> "0..*" RepairJob : handles
RepairJob "0..1" --> "1" Technician : assignedTo
RepairJob "1" --> "1" Invoice : generates
Invoice "1" --> "1..*" Payment : receives
