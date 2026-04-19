# Assignment 8: State Transition Diagrams

## 1. Device Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Received
    Received --> Diagnosing : Technician inspects device
    Diagnosing --> InRepair : Repair approved
    Diagnosing --> AwaitingApproval : Awaiting customer approval
    AwaitingApproval --> InRepair : Approved
    AwaitingApproval --> Cancelled : Rejected
    InRepair --> Completed : Repair finished
    Completed --> Collected : Customer picks up / delivery done
```

### Explanation

* States: Received, Diagnosing, AwaitingApproval, InRepair, Completed, Collected, Cancelled
* Tracks full lifecycle of a device
* Maps to:

  * FR-002: Device intake recording
  * FR-004: Repair tracking
  * FR-006: Service handling

---

## 2. Customer Account

```mermaid
stateDiagram-v2
    [*] --> New
    New --> Active : Registered
    Active --> Returning : Uses service again
    Active --> Inactive : No activity
```

### Explanation

* Tracks customer engagement
* Maps to FR-001: Customer registration

---

## 3. Repair Job

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Assigned : Technician assigned
    Assigned --> InProgress : Repair started
    InProgress --> WaitingParts : Parts required
    WaitingParts --> InProgress : Parts received
    InProgress --> Completed : Repair done
    Completed --> Closed : Job finalized
    Created --> Cancelled : Customer cancels
```

### Explanation

* Tracks repair job progress
* Maps to FR-004: Repair tracking

---

## 4. Payment

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Paid : Payment successful
    Pending --> Failed : Payment failed
    Paid --> Recorded : Stored in system
```

### Explanation

* Tracks payment lifecycle
* Maps to FR-008: Pricing and profit calculation

---

## 5. Accessory Record

```mermaid
stateDiagram-v2
    [*] --> Logged
    Logged --> Verified : Technician confirms
    Verified --> Returned : Given back to customer
    Logged --> Missing : Not returned
```

### Explanation

* Prevents accessory disputes
* Maps to FR-003: Accessory tracking

---

## 6. Service Request

```mermaid
stateDiagram-v2
    [*] --> Requested
    Requested --> Scheduled : Booking confirmed
    Scheduled --> InTransit : Device moving
    InTransit --> Completed : Delivered
```

### Explanation

* Tracks pickup/delivery service
* Maps to FR-006: Service handling options

---

## 7. Notification

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Sent : Notification delivered
    Sent --> Read : Customer viewed
```

### Explanation

* Keeps customers informed
* Supports system communication

---

## 8. Technician Assignment

```mermaid
stateDiagram-v2
    [*] --> Unassigned
    Unassigned --> Assigned : Technician allocated
    Assigned --> Working : Repair started
    Working --> Completed : Task finished
```

### Explanation

* Tracks technician workload
* Supports repair workflow efficiency
