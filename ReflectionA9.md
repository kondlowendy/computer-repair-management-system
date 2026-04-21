Designing the domain model and class diagram for the Computer Repair Management System was both challenging and insightful, especially because it required translating real-world repair shop operations into structured object-oriented components.

One of the main challenges I faced was identifying the correct level of abstraction. Initially, I had too many entities such as “Receptionist,” “Walk-in Customer,” and “Repair Status Tracker.” However, I realized that including too many granular objects made the system overly complex and difficult to model. I had to step back and focus on core domain entities like Customer, Device, RepairTicket, and Technician. This helped simplify the model while still maintaining all essential business functionality.

Another difficulty was defining relationships between entities correctly, especially deciding between aggregation and composition. For example, I initially treated ServiceTask as an independent entity, but later realized it should be tightly coupled with RepairTicket because tasks cannot exist without a repair job. This led me to correctly model it as a composition relationship.

Aligning the class diagram with previous assignments (requirements, use cases, and activity/state diagrams) was very important. From the use cases, I identified key interactions such as “Create Repair Ticket,” “Assign Technician,” and “Generate Invoice.” These directly influenced the methods in the RepairTicket and Invoice classes. The state diagrams also helped define status transitions like “Pending → In Progress → Completed,” which I reflected in the status attributes and updateStatus() methods.

A major trade-off I made was simplifying inheritance. Initially, I considered having a parent class called User with subclasses like Customer and Technician. However, I decided not to implement inheritance in this version because it added unnecessary complexity for the current scope. Instead, I kept them as separate classes with shared attributes duplicated where needed. This was a deliberate decision to prioritize clarity over strict object-oriented purity.

Another trade-off was reducing system features such as inventory management and advanced analytics. While these are realistic in a full system, including them would have made the class diagram too large and harder to interpret for assignment purposes.

Through this exercise, I learned that good object-oriented design is not about adding more classes, but about designing meaningful relationships between the right ones. I also learned the importance of keeping consistency across all system models—requirements, use cases, and class diagrams must all tell the same story.

Overall, this assignment improved my understanding of domain-driven design, especially how real-world processes like computer repair services can be structured into clean, maintainable software architecture.
