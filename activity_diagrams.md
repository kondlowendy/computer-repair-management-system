# Assignment 8: Activity Diagrams

## 1. Device Intake Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Customer brings device]
    B --> C[Record device details]
    C --> D[Record accessories]
    D --> E[Assign technician]
    E --> F([End])
```

### Explanation

* Ensures all device and accessory data is captured
* Addresses lost record problem

---

## 2. Repair Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Diagnose issue]
    B --> C{Repair approved?}
    C -->|Yes| D[Start repair]
    C -->|No| E[Cancel job]
    D --> F{Need parts?}
    F -->|Yes| G[Order parts]
    G --> D
    F -->|No| H[Complete repair]
    H --> I([End])
```

### Explanation

* Includes decision-making and looping
* Handles real repair scenarios

---

## 3. Payment Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Generate invoice]
    B --> C[Customer pays]
    C --> D{Payment successful?}
    D -->|Yes| E[Record payment]
    D -->|No| F[Retry payment]
    E --> G([End])
```

### Explanation

* Ensures reliable payment handling
* Supports profit tracking

---

## 4. Pickup/Delivery Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Request pickup/delivery]
    B --> C[Schedule service]
    C --> D[Transport device]
    D --> E[Confirm delivery]
    E --> F([End])
```

---

## 5. Profit Calculation Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Enter repair cost]
    B --> C[Enter service price]
    C --> D[Calculate profit]
    D --> E[Store result]
    E --> F([End])
```

---

## 6. Notification Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Trigger event]
    B --> C[Generate message]
    C --> D[Send notification]
    D --> E([End])
```

---

## 7. Customer Registration Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Enter details]
    B --> C[Validate input]
    C --> D{Valid?}
    D -->|Yes| E[Create account]
    D -->|No| F[Show error]
    E --> G([End])
```

---

## 8. Cancel Repair Workflow

```mermaid
flowchart TD
    A([Start]) --> B[Request cancellation]
    B --> C[Check repair status]
    C --> D{In progress?}
    D -->|Yes| E[Stop repair]
    D -->|No| F[Cancel directly]
    E --> G[Update status]
    F --> G
    G --> H([End])
```

### Explanation

* Handles both early and late cancellations
* Improves system flexibility
