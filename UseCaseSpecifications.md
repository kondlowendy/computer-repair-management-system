# Computer Repair Management System - Use Case Specifications

---

## **1. Register Device**
**Actor:** Customer  
**Description:** Customer registers a device for repair in the system.  
**Precondition:** Customer account exists.  
**Postcondition:** Device is saved in the system and ready for intake.  

**Basic Flow:**  
1. Customer logs in to the system.  
2. Customer enters device information (type, brand, model, problem description).  
3. Customer submits registration.  
4. System confirms successful registration.  

**Alternative Flows:**  
- Invalid device information → System shows error and requests correction.  
- Customer not logged in → System prompts for login.  

---

## **2. Record Device Intake**
**Actor:** Technician  
**Description:** Technician logs the receipt of a registered device along with accessories.  
**Precondition:** Device has been registered.  
**Postcondition:** Device intake recorded in the system.  

**Basic Flow:**  
1. Technician selects the registered device.  
2. Technician records received accessories (charger, bag, etc.).  
3. Technician submits intake information.  
4. System confirms intake recorded successfully.  

**Alternative Flows:**  
- Missing accessories → System prompts technician to confirm or flag as missing.  
- Device not registered → System shows error message.  

---

## **3. Add Accessories**
**Actor:** Technician  
**Description:** Technician records additional accessories received or updated after initial intake.  
**Precondition:** Device intake has been recorded.  
**Postcondition:** Accessories updated in the system.  

**Basic Flow:**  
1. Technician selects device.  
2. Technician lists new accessories.  
3. Technician saves updated accessory information.  

**Alternative Flows:**  
- Accessory already recorded → System alerts technician to avoid duplicates.  
- Device not found → System shows error.  

---

## **4. Update Repair Status**
**Actor:** Technician / Admin  
**Description:** Update the current status of a repair for tracking purposes.  
**Precondition:** Device intake has been recorded.  
**Postcondition:** Repair status is updated and available for tracking.  

**Basic Flow:**  
1. Select device from repair list.  
2. Update repair status (e.g., Diagnosed, In Progress, Completed).  
3. System notifies customer of the updated status.  

**Alternative Flows:**  
- Device not found → System shows error.  
- Technician tries to skip required fields → System prompts to fill them.  

---

## **5. Track Repair Status**
**Actor:** Customer / Delivery Staff  
**Description:** Allows users to view the current status of a repair.  
**Precondition:** Device is registered and intake recorded.  
**Postcondition:** User sees the updated repair status.  

**Basic Flow:**  
1. Customer logs in.  
2. Customer selects their device.  
3. System displays current repair status.  

**Alternative Flows:**  
- Device not registered → System shows error message.  
- System temporarily unavailable → Notify user to retry.  

---

## **6. Choose Service Option**
**Actor:** Customer  
**Description:** Customer chooses the repair service type (pickup, delivery, or drop-off).  
**Precondition:** Device is registered.  
**Postcondition:** Service type is saved and recorded in the system.  

**Basic Flow:**  
1. Customer selects service option.  
2. Confirms choice.  
3. System saves service option successfully.  

**Alternative Flows:**  
- Invalid selection → System prompts customer to choose again.  
- Customer cancels operation → System maintains previous selection.  

---

## **7. Calculate Profit**
**Actor:** Admin  
**Description:** System calculates total profit by comparing repair costs to pricing.  
**Precondition:** Repairs must be completed.  
**Postcondition:** Profit report is generated and available to Admin.  

**Basic Flow:**  
1. Admin selects reporting period.  
2. System calculates total revenue minus costs.  
3. System displays profit report.  

**Alternative Flows:**  
- No completed repairs → System shows warning “No data available for selected period.”  
- Incorrect cost data → Admin notified to review inputs.  

---

## **8. View Reports**
**Actor:** Admin  
**Description:** Generates operational reports for system performance and repair tracking.  
**Precondition:** Repairs exist in the system.  
**Postcondition:** Report is generated and displayed to Admin.  

**Basic Flow:**  
1. Admin selects report type (daily, weekly, monthly).  
2. System generates report with repair data, revenue, and profit.  
3. Admin views report.  

**Alternative Flows:**  
- No data available → System shows message “No records for the selected period.”  
- Report generation fails → System prompts to retry.  
