# Software Requirements

## Introduction

The Identity Exchange (IE) is an entity that acts as Broker Identity Federation that implement one time blind Proof of Existence (PoE) that establish that a real person is behind an account without reveling sensible user information. IE also use Proof of Attributes (PoA) to enable specific verification as part of the claims.

![Indentity Exchange](./documentation/images/IE.png)

## Functional Requirements

### Use Cases

### User Stories

| Category  | User Stories  |
|:---:|-------------|
| User  | *As an* user of the Relying Party (RP), *I want to* use the consent banner as an entry point *so that* I can log in to the Identity Exchanger (IE) through Proof of Existence (PoE) using e.g., FIDO2. |
| User  | *As an* Relying Party (RP) user, *I want to* use the consent banner as an entry point for the Proof of Attribute (PoA) *so that* it can be verified the actual value of the user's age using e.g., Google Authentication, eIDAS2. |
| User  | *As an* Relying Party (RP) user, *I want to* use the consent banner as an entry point for the Proof of Attribute (PoA) *so that* if a user is authenticated through the browser (e.g. in Google) the authentication is transferred to the Identity Exchange, allowing the verification process through the PoA. |
| Relaying Party  | *As a* Relying Party (RP), *I want to* be able to decide on both the Identity Assurance Level (IAL) and the Authenticator Assurance Level (AAL) supported by the Identity Providers (IdPs) *so that* the Identity Exchanger (IE) provides connectivity only to Identity Providers (IdPs) that meet these requirements. |
| Relaying Party  | *As a* Relying Party (RP), *I want to* be able to decide the Federation Assurance Level (FAL) supported by the Identity Exchanger (IE), *so that* I can select between the different Federation Assurance Levels (FAL) offered by the Identity Exchanger (IE). |
| Relaying Party | *As a* Relying Party (RP), *I want to* verify user consent from a Proof of Attribute (PoA), so the Identity Provider (IdP) and Identity Exchange (IE) must support these mechanisms or define third-party connectors that allow verifications to be performed. |
| Identity Provider  | *As an* Identity Provider (IdP), *I want to* authenticate the user from a Proof of Existence (PoE) based on Biometrics, *so that* the user must have an end device that supports standard FIDO2. |
| Identity Provider  | *As an* Identity Provider (IdP), *I want to* authenticate the user from a Proof of Existence (PoE) based on eIDAS2 Authentication, *so that* the user must be in possession of an eID. |

## Non-functional Requirements

- Performance: The software should respond to user actions within 2 seconds and support concurrent user access without significant performance degradation.

- Usability: The user interface should be intuitive and user-friendly, with clear navigation and consistent design.

- Reliability: The software should have a minimum uptime of 99% and provide error handling and data backup mechanisms.

- Security: User authentication should be implemented, and data should be encrypted during transmission and storage.

- Compatibility: The software should be compatible with popular web browsers (e.g., Chrome, Firefox, Safari) and responsive across different screen sizes.

- Scalability: The software should handle a growing number of users and projects without compromising performance

- Maintainability: The software should be modular, well-documented, and allow for future updates and enhancements.

## System Constraints

- Hardware Limitations: The software should be compatible with standard hardware configurations, including desktops, laptops, and mobile devices.

- Software Dependencies: The software should be developed using a specific programming language and framework (e.g., Python and Django) and utilize a relational database (e.g., PostgreSQL).

- Regulatory and Legal Requirements: The software should comply with relevant data privacy and protection regulations, such as GDPR.

## Assumptions and Dependencies

- Assumption: Users will have a reliable internet connection to access the software.

- Dependency: The software development team will have access to the required development tools and infrastructure.
