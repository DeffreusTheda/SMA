# IBDP ComSci Topic 1

## Consideration in Changing to a New System

- Extent of change e.g complete change, front-end or back-end changes, and new features.
- Limitation of new system e.g compatibility issue, need of learning/adapting to new changes, and data migration.
- Change in the roles of user e.g how the user use the software.

## Difficulties in Changing Software Systems

- Resistance to change
- Some features may be removed
- New system may be slower from new features
- Incompatibility with other existing system in use
- Data loss or data migration risks
- Costly

## 4 Ways to Change

> \* I think that the cons are easily mitigated with cloud backups, which I believe any organization should utilize; this also apply to other ways to change to a new system. Any considerate organization would create backup before changing or updating their system.

### Direct Changeover

Old system get immediately replaced entirely by the new system.

- Pros:
  - Changeover swift; no awaiting; immediate effect
  - Low costs
- Cons:
  - \* No backup in case of failure; risky

### Parallel

New system is used in addition to the old system, with the same data entered; This might be tedious.<br>

- Pros:
  - \* Backup if one of the system fail; lower risks
  - Real-time comparison of new and old system -> decision on change continuation; verification of new system functionality
- Cons:
  - Increased costs in resources and money for running both system, especially with huge-scale organization

### Pilot

New system implemented at smaller scale for testing, then expands across the organization.<br>

- Pros:
  - Sandboxed failures in the tested small part of organization
  - Pilot/tester can teach others
  - All features were tested before adoption to the whole organization
- Cons:
  - \* No backup in cases of failure for the pilot group
  - Lengthy implementation

### Phased

New system is introduced in phases, replacing old system gradually.<br>

- Pros:
  - Ease of adaptation
  - Staged training
- Cons:
  - \* No backup for the part of system in ongoing phase
  - Lengthy implementation

## Data Migration

A big challange when changing from an old system to a new system of the same purpose. The scale of the system directly affect data migration. Problems may include:

- Different file formats when changing to different software (not update from existing software, okay?)
- Data structure differences; this require algorithm to change from old data structure to the new data structure
- Different rules for what constitutes 'valid data' e.g not negative, date format
- Risks of failures in data transfer, resulting in loss of data
- Different convention based on software origin e.g currencies, languages used, and date format (USA moment)

## Legacy system

Transition from old system to a new one can be caused by outdate, legacy system that is not up to the new standard i.e security, and efficiency, in addition to end-of-support and unavailability of legacy system.
Although, changing to a new system may be costly and time-consuming, especially with huge-scale organization.
Alternative to transition to new system is maintaining and updating end-of-support legacy software (not upstream) by recruiting persons well versed in the legacy system's programming language.

## Local vs Remote (SaaS) Software

Local software runs on an organization system/computer e.g Notepad++, Adobe Photoshop, etc.  
Remote software, also called 'Software as a Service', is usually accessed from a web browser e.g Office 365, Google Docs, etc.

Common characteristics of local and remote software:

| Local Software                         | Remote Software                       |
| -------------------------------------- | ------------------------------------- |
| **One-time** fee                       | **Subscription** fee                  |
| Used on **specific OS**                | Use on **any computer** via internet  |
| **No** free trial                      | Free trial **often** available        |
| Require **installment**                | **No Installment** required           |
| **Some** automatic update              | **All** update automatic              |
| **Less likely** has supplemental apps  | **Most likely** has supplemental apps |
| New version **require** a new purchase | Always on latest version              |
| Mobile synchronization often costly    | Mobile synchronization often free     |

### SaaS

Benefits:

- Employee mobility
- Cost savings; does not use organization resources
- Scalability; need enough servers/data centers
- Fewer support staff; handled by the third-party service company
- Pay as you go; subscription model
- Easier maintenance

Drawbacks:

- Geographical distance with the service server
- Availability; reliance on the third-party company to fix issues
- Security; configured not specifically for the organization
- Compliance; less control of the software
- Provider gets acquired; features may change
- Data corruption/recovery
