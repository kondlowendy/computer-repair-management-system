1.1 Key Domain Entities

The system is built around managing customers, devices, repair jobs, technicians, and payments.

📊 Domain Model Table
Entity	Attributes	Methods	Relationships
Customer	customerId, name, email, phone, address	register(), updateProfile()	Places RepairTicket
Device	deviceId, type, brand, model, serialNumber, status	updateStatus(), getDetails()	Belongs to Customer, linked to RepairTicket
Technician	technicianId, name, specialization, availabilityStatus	assignJob(), updateStatus()	Works on RepairTicket
RepairTicket	ticketId, issueDescription, status, createdDate, completionDate	assignTechnician(), updateStatus(), closeTicket()	Links Customer, Device, Technician
ServiceTask	taskId, description, cost, status	updateTask(), calculateCost()	Part of RepairTicket
Invoice	invoiceId, totalAmount, paymentStatus, dateIssued	generateInvoice(), markPaid()	Linked to RepairTicket
Payment	paymentId, amount, method, paymentDate	processPayment(), validatePayment()	Associated with Invoice
1.2 Relationships Overview
A Customer can own multiple Devices
A Customer can create multiple RepairTickets
Each RepairTicket is linked to one Device
Each RepairTicket is assigned to one or more Technicians
A RepairTicket contains multiple ServiceTasks
Each RepairTicket generates one Invoice
Each Invoice can have one or more Payments
1.3 Business Rules
A customer can submit unlimited repair tickets but each ticket must relate to one device.
A technician can handle multiple tickets but only if they are available.
A repair ticket cannot be closed until all service tasks are completed.
An invoice is only generated when a repair ticket is marked as completed.
Payments must equal or exceed the invoice total before marking invoice as “paid”.
Each device must have a unique serial number.
