classDiagram

class Customer {
    +string customerId
    +string name
    +string email
    +string phone
    +string address
    +register()
    +updateProfile()
}

class Device {
    +string deviceId
    +string type
    +string brand
    +string model
    +string serialNumber
    +string status
    +updateStatus()
    +getDetails()
}

class Technician {
    +string technicianId
    +string name
    +string specialization
    +string availabilityStatus
    +assignJob()
    +updateStatus()
}

class RepairTicket {
    +string ticketId
    +string issueDescription
    +string status
    +date createdDate
    +date completionDate
    +assignTechnician()
    +updateStatus()
    +closeTicket()
}

class ServiceTask {
    +string taskId
    +string description
    +float cost
    +string status
    +updateTask()
    +calculateCost()
}

class Invoice {
    +string invoiceId
    +float totalAmount
    +string paymentStatus
    +date dateIssued
    +generateInvoice()
    +markPaid()
}

class Payment {
    +string paymentId
    +float amount
    +string method
    +date paymentDate
    +processPayment()
    +validatePayment()
}

Customer "1" --> "0..*" Device : owns
Customer "1" --> "0..*" RepairTicket : creates
Device "1" --> "0..*" RepairTicket : linkedTo
RepairTicket "1" --> "1..*" ServiceTask : contains
RepairTicket "1" --> "1" Invoice : generates
RepairTicket "0..*" --> "1..*" Technician : assignedTo
Invoice "1" --> "0..*" Payment : receives

2.1 Design Decisions
I introduced ServiceTask to break down repair work into smaller units for better tracking and cost calculation.
RepairTicket acts as the central entity connecting customers, devices, technicians, and billing.
Payment is separated from Invoice to support partial or multiple payments.
Many-to-many relationship between Technician and RepairTicket allows flexible job allocation.
Composition is used between RepairTicket → ServiceTask because tasks cannot exist without a ticket.
