# Cafeteria Ordering System — Vision and Scope

**Version:** 1.0 (approved)  
**Prepared by:** Karl Wiegers, Process Impact  
**Date:** November 4, 2018

## Revision History
| Version | Date | Author | Description |
| --- | --- | --- | --- |
| 1.0 draft 1 | 2018-10-13 | Karl Wiegers | Initial draft |
| 1.0 approved | 2018-11-04 | Karl Wiegers | Baseline after inspection |

## 1. Business Requirements
### 1.1 Background, Business Opportunity, and Customer Needs
Process Impact employees currently spend about 60 minutes each workday to buy and eat lunch in the cafeteria, including ~20 minutes walking, selecting meals, and paying by cash or card. Off-site lunches average 90 minutes. Phone-ahead orders are possible but do not guarantee preferred menu items, and the cafeteria discards significant unsold food. A web-based ordering and delivery system would save employees time, increase the likelihood of getting desired meals, reduce food waste, and improve cafeteria efficiency. Future integration with local restaurants could broaden menu choices and enable bulk-purchase savings while shifting some meals away from the onsite cafeteria.

### 1.2 Business Objectives and Success Criteria
- **BO-1:** Reduce cafeteria food wastage by 50% within 6 months of the initial release.  
  - **Scale:** Value of food discarded weekly.  
  - **Meter:** Cafeteria Inventory System logs.  
  - **Baseline (2018 study):** 30% wastage.  
  - **Plan:** <15%; **Must:** <20%.
- **BO-2:** Reduce cafeteria operating costs by 15% within 12 months of the initial release.
- **BO-3:** Increase effective work time by 20 minutes per employee per day within 3 months of the initial release.
- **SC-1:** At least 75% of current cafeteria patrons use the Cafeteria Ordering System within 6 months of launch.
- **SC-2:** Improve the average quarterly cafeteria satisfaction rating by 0.5 within 3 months and by 1.0 within 12 months of launch.

### 1.3 Business Risks
- **RI-1:** The Cafeteria Employees Union could request contract renegotiations for new roles and hours. *(Probability: 0.6; Impact: 3)*
- **RI-2:** Low employee adoption could reduce ROI for the system and operational changes. *(Probability: 0.3; Impact: 9)*
- **RI-3:** Local restaurants might decline price reductions, lowering satisfaction and usage. *(Probability: 0.4; Impact: 3)*

## 2. Vision of the Solution
### 2.1 Vision Statement
For employees who want to order meals online from the company cafeteria or local restaurants, the Cafeteria Ordering System is an Internet-based application that supports individual or group orders, processes payments, and triggers delivery to designated locations on the Process Impact campus. Unlike current phone or in-person ordering, it saves travel time and expands available food choices.

### 2.2 Major Features
- **FE-1:** Order meals from cafeteria menu for pickup or delivery.
- **FE-2:** Order meals from local restaurants for delivery.
- **FE-3:** Create, view, modify, and delete meal service subscriptions.
- **FE-4:** Register for meal payment options.
- **FE-5:** Request meal delivery.
- **FE-6:** Create, view, modify, and delete cafeteria menus.
- **FE-7:** Order custom meals not on the cafeteria menu.
- **FE-8:** Produce recipes and ingredient lists for custom meals from the cafeteria.
- **FE-9:** Provide access via corporate intranet or authorized external Internet access.

### 2.3 Assumptions and Dependencies
- **AS-1:** Intranet-enabled computers and printers will support cafeteria staff processing without missing delivery windows.
- **AS-2:** Cafeteria staff and vehicles are available to deliver all orders within 15 minutes of the requested time.
- **DE-1:** If a restaurant has its own online ordering system, the Cafeteria Ordering System must support bidirectional communication.

## 3. Scope and Limitations
### 3.1 Scope of Initial and Subsequent Releases
| Feature | Release 1 | Release 2 | Release 3 |
| --- | --- | --- | --- |
| FE-1 | Standard lunch-menu meals; delivery payable only by payroll deduction | Add breakfast and dinner ordering; accept credit/debit cards | — |
| FE-2 | Not implemented | Not implemented | Full implementation |
| FE-3 | Implemented if time permits (medium priority) | Fully implemented | — |
| FE-4 | Register for payroll deduction payments only | Register for credit and debit cards | — |
| FE-5 | Delivery only to company campus sites | Add delivery to selected off-site locations | — |
| FE-6 | Fully implemented | — | — |
| FE-7 | Not implemented | Not implemented | Fully implemented |
| FE-8 | Not implemented | Fully implemented | — |
| FE-9 | Fully implemented | — | — |

### 3.2 Limitations and Exclusions
- **LI-1:** Some cafeteria items will not be suitable for delivery; the online menus are a subset of full cafeteria offerings.
- **LI-2:** The system applies only to the cafeteria at the main Process Impact campus in Clackamas, Oregon.

## 4. Business Context
### 4.1 Stakeholder Profiles
| Stakeholder | Major Value | Attitudes | Major Interests | Constraints |
| --- | --- | --- | --- | --- |
| Corporate Management | Improved productivity; cafeteria cost savings | Strong support through release 2; release 3 contingent on earlier results | Savings must exceed development and usage costs | None identified |
| Cafeteria Staff | More efficient staffing; higher patron satisfaction | Concern about union relations and possible downsizing; otherwise receptive | Job preservation | Training for Internet use; need delivery staff and vehicles |
| Patrons | Better selection; time savings; convenience | Enthusiastic but may still value social aspects of in-person dining | Ease of use; delivery reliability; menu availability | Need corporate intranet access |
| Payroll Department | Minimal direct benefit; must enable payroll-deduction registration | Recognizes value but dislikes extra software work | Minimal changes to payroll applications | No resources yet committed for changes |
| Restaurant Managers | Increased sales and exposure | Receptive but cautious | Minimal new technology; costs and effort of delivery | Might lack staff/capacity; may need Internet access |

### 4.2 Project Priorities
- **Primary focus:** Achieve targeted waste reduction, adoption, and satisfaction improvements within the first two releases.
- **Secondary focus:** Expand delivery coverage and restaurant integration once core cafeteria ordering stabilizes.

### Operating Environment
Planguage notation is used to state quantitative objectives precisely. All content © 2018 Karl E. Wiegers. All Rights Reserved.
