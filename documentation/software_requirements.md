# Software Requirements

## Introduction

The Internet provides access to an ever increasing number of services, many of which require its users to have an account with credentials. This is a considerable cognitive burden for users and leads to password reuse and other poor security practices. Delegated authentication protocols offer a way out of this dilemma. These protocols allow a user to use her account at an Identity Provider (IdP) to log in to other services, called Relying Party (RP). This provides users with single sign-on functionality, where one account can be used to log in to many different services. The most widely used delegated authentication protocol today is OpenID Connect, supported by identity providers like Google and Microsoft. Unfortunately OpenID Connect is not privacy-friendly: the identity provider learns with each use which relying party the user logs in to. This necessitates a high degree of trust in the identity provider, and is especially problematic when the relying parties’ identity reveals sensitive information. This problem is extensible to other identity protocols such as SAML. Therefore, there is a need to remodel the flow of identity transactions to cater to both anonymity and accountability considerations. The starting point will be the study of the identity federation process.

## Identity Federation

In a federation protocol, a three-party relationship is formed between the subscriber, the IdP, and RP. Depending on the specifics of the protocol, different information passes between the participants at different times. The subscriber communicates with both the IdP and the RP, usually through a browser. The RP and the IdP communicate with each other in two ways:

- The front channel, through redirects involving the subscriber; or
- The back channel, through a direct connection between the RP and IdP, not involving the subscriber.

The subscriber authenticates to the IdP and the result of that authentication event is asserted to the RP across the network. In this transaction, the IdP acts as the verifier for the credential. The IdP can also make attribute statements about the subscriber as part of this process. These attributes and authentication event information are carried to the RP through the use of an assertion. There are several federation models: (1) Manual resitration, (2) Dynamic Registration, (3) Federation Authorities and (4) Proxied Federation. For the value, from the privacy and anonymization perspective, the Proxied Federation will be studied below.

![Federation](documentation/images/federation.png)

### Proxied Federation

In a proxied federation, communication between the IdP and the RP is intermediated in a way that prevents direct communication between the two parties. There are multiple methods to achieve this effect. Common configurations include:

- A third party that acts as a federation proxy (or broker)
- A network of nodes that distributes the communications

Where proxies are used, they function as an IdP on one side and an RP on the other. Therefore, all normative requirements that apply to IdPs and RPs SHALL apply to proxies in their respective roles.

![Federation Proxy](documentation/images/federation_proxy.png)

One of the main properties of the Identity Federation Proxy is blinding, which is discussed below.

#### Blinding in Proxied Federation

While some proxy structures — typically those that exist primarily to simplify integration — may not offer additional subscriber privacy protection, others offer varying levels of privacy to the subscriber through a range of blinding technologies. Privacy policies may dictate appropriate use of the subscriber attributes and authentication transaction data (e.g., identities of the ultimate IdP and RP) by the IdP, RP, and the federation proxy. Technical means such as blinding can increase effectiveness of these policies by making the data more difficult to obtain. As the level of blinding increases, the technical and operational implementation complexity may increase. Proxies need to map transactions to the appropriate parties on either side as well as manage the keys for all parties in the transaction.

Even with the use of blinding technologies, a blinded party may still infer protected subscriber information through released attribute data or metadata, such as by analysis of timestamps, attribute bundle sizes, or attribute signer information. The IdP could consider additional privacy enhancing approaches to reduce the risk of revealing identifying information of the entities participating in the federation.

The following table illustrates a spectrum of blinding implementations used in proxied federation. This table is intended to be illustrative, and is neither comprehensive nor technology specific.

![Federation Proxy](documentation/images/proxy_comparison.png)

## Our solution

IdPs that provide authentication services and RPs that consume those services are known as members of a federation. From an IdP’s perspective, the federation consists of the RPs that it serves. From an RP’s perspective, the federation consists of the IdPs that it uses. 

The Identity Exchange (IE) is an entity that acts as Broker Identity Federation that implement one time blind Proof of Existence (PoE) that establish that a real person is behind an account without reveling sensible user information. IE also use Proof of Attributes (PoA) to enable specific verification as part of the claims. As shown in the following figure, the entities that form part of the system are:

- User
- Identity Provider (IdP)
- Identity Exchange (IE)
- Relying Party (RP)

![Indentity Exchange](documentation/images/IE.png)

## Functional Requirements

1. **Setting up a trust chain**:

    - The IE must support different RP levels of assurances.
    - IE negotiate Identity Assurance Level and Authenticator Assurance with RP.
    - IE negotiate Federation Assurance Level with IdP.

2. **Integration on the consent banner**:

   - The IE access entry point is the consent banner that must be previously installed in the RP.
   - The user interface contained into the consent banner will directly display the IdPs supported by IE.

3. **Approach of information flow**

- As shown in the following figure, the IE is internally divided into an OIDC Provider to establish communication with the RP's OIDC client and an OIDC client to establish communication with the IdP. Taking this approach into consideration, the following information flows are defined as follows:

   ![Indentity Exchange in detail](./images/IE_detail.png)

   1. The user discovers a relying party.
      1. The user access the RP with the intent to create an account and access services on the RP.
   2. The user creates an account on the RP and as the last step of account creation, the RP asks for access to identity information from a user through a trusted IE.
      1. The RP acting as the client, creates an authentication request including the scope parameters which includes any attributes requested, proof of attributes (PoA) requested and the Level of Assurance (LoA) requirements. The authentication request includes:
         1. A redirect response created by the client, which triggers the user agent to make an authentication request to the OpenID Provider (OP) which is the IE in this context.
         2. This authentication request includes a client_id which is the client identifier, the scope , the redirect_uri where the client will receive the authentication response, the state which is a random string generated by the client to identify a session, prevent CSRF attacks and must be returned to the client in the authentication response, and other optional specifications.
   3. The IE logs the request from the RP and stores it against an identifier that it creates called the RP Link. The IE also validates the authentication request from the RP.
      1. This RP Link will be used to connect the information requested by the RP to the information provided by the IdP without either party knowing the identity of each other.
      2. The IE prompts the user to select an IdP. The user selects an IdP.
   4. Based on the selected IdP, the IE creates a Authentication Request for the selected IdP. Now the Exchange acts as a client and the IdP will be the OP. The IE will use all the information provided by the RP to create the scope . The authentication request includes:
      1. A redirect response created by the client (the IE now), which triggers the user agent to make an authentication request to the OpenID Provider (OP) which is the IdP now.
      2. This authentication request includes a `client_id` which is the client identifier (identifies the IE), the `scope`, the `redirect_uri` where the client will receive the authentication response, the state which is a random string generated by the client to identify a session, prevent CSRF attacks and must be returned to the client in the authentication response, and other optional specifications.
   5. The IdP validates that the authentication request came from the IE.
   6. The IdP prompts user to log into their account. The user provides necessary credentials to access their account on the IdP.
      1. There might be extra steps required for the user to satisfy the LoA requirements. These requirements will be specified in the `scope` of the authentication request. The Identity Assurance Level (IAL) or the Authenticator Assurance Level (AAL) might not be satisfied. The user will be required to meet the requirement levels by identity proofing mechanisms or adding multi-factor authentication to their IdP.
   7. An authentication response is returned to the client (the IE) which includes a code generated by the OP (the IdP) and the same `state` value provided by the client in the Authentication request in *step iv*.
      1. The authorization code called code is a random string issued by the IdP to be used in the request to the token endpoint - this is an endpoint at the OP (which in this step is the IdP). The OIDC has many code flows, for the purpose of this architecture I am using the Authorization code flow. The authorization code flow ensures that none of the tokens are exposed to the User Agent which removes the chance of any malicious applications on the User Agent being able to access the tokens.
   8. The IE validates the authentication response.
   9. Now, the IE creates a Token request which includes the `code` that was received in the authentication response in *step vii*, the `redirect_uri` which must match the value used in the authentication request in step 4, and the `client_assertion` which is the the signed client authentication JWT generated by the client(IE). The client must generate a new assertion JWT for each call to the token endpoint at the IdP.
      1. The signed JWT is a Json Web Token which has claims made by the IE and signed by it as well. These claims include `iss` which is the client ID of the client creating and issuing the JWT, the `aud` which is the URL of the OP’s (which is the IdP in this step) token endpoint, the `jti` which is a unique random identifier of the JWT and the date of creation and expiration.
   10. The IdP validates the Token request. The Token request is accepted when signature on the JWT (`client_assertion`) is validated using the IE’s registered public key.
   11. The OP (IdP) returns a Token Response which includes an ID Token and an Access Token, signed by the IdP.
       1. **ID Token**: It is the signed JWT which includes set of claims sent by the OP. These claims includes the `iss` which is the URL of the OP creating and issuing the ID Token, which is the IdP in this step, the `aud` which is client ID of the client (IE), the `sub` which is the identifier of the user, the `acr` which is the level of assurance at which the user was authenticated at, at the IdP, the `jti` which is a unique random identifier of the JWT to prevent reuse of token and the date of creation and expiration of the ID Token.
       2. The `sub` is a pairwise unique value which identifies the end-user of the OP to the client only. So a different Exchange will have a different value for the `sub` identifier for the same end-user. This is added to remove linkability if two clients collude (which in this case is two Exchanges).
       3. The ID Token may also include other requested claims (attributes and proof of attributes (PoA)) such as the end user’s email address or a Boolean confirming whether the end-user is over the age of 18.
       4. **Access Token**: An Access token can be used to make further requests for more User Information. For the sake of this example, I assume the RP requires no excess identity attributes from the IdP.
   12. The IE validates the Token response. The IE validates the ID Token and accepts it if the signature on the ID Token is validated using IdP’s registered public key.
   13. The IE extracts the subject identifier(`sub`) from the ID Token and checks whether it already has a an entry for that particular subject identifier. If one doesn’t exist, The Identity Exchange creates one and stores it against an identifier generated by the Exchange called the *IdP link*.
       1. Just like the RP Link mentioned in *step iii*, the *IdP Link* will be used to connect information provided by an IdP to an RP.
   14. The IE extracts all other claims from the ID Token as well. Before passing on the attributes to the RP that requested them, the IE asks for user consent.
       1. The IE prompts the user to give consent. The user provides the necessary consent.
   15. The Authentication Response to the request created in *step ii.a* is sent back to the client. Now the Exchange is back to acting as the OP and the RP will be the client. The response includes a code generated by the OP (the IE) and the same state value provided by the client in the Authentication request in *step ii.a*.
   16. The RP validates the Authentication response.
   17. The RP creates a Token Request to the IE. This request includes the ``code` , the `redirect_uri` used in the authentication request and the `client_assertion` which is the signed JWT generated by the client (RP).
   18. The IE validates the Token request. It also validates the signature on the JWT against the RP’s registered public key.
   19. The IE returns a successful Token response. This includes an ID Token and an Access Token signed by the IE. The ID Token includes all the information required by the RP in its initial request. The ID Token also contains the number of times this IdP has been used by the the end-user to create an account on the RP.
   20. The RP validates the Token response, as well as the ID Token and the JWT signed in the ID Token.
   21. The RP extracts all other claims from the ID Token as well. This includes identity attributes, proof of identity attributes (PoA), count of previous accounts on this RP and Levels of Assurance.
       1. The RP lets user know that account creation was successful if the previous count of accounts is less than the threshold created by the RP.

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

- Usability: The user interface (will be displayed only within the banner) so it must be intuitive and easy to use, with clear navigation and a coherent design.

- Reliability: The software, i.e., the IE should have a minimum uptime of 99% and provide error handling and data backup mechanisms.

- Compatibility: The software, i.e., the IE should be compatible with popular web browsers (e.g., Chrome, Firefox, Safari) and responsive across different screen sizes.

- Maintainability: The software, i.e., the IE should be modular, well-documented, and allow for future updates and enhancements. A microservice based architecture should be used.

- Encapsulation: The software, i.e., will be developed on Docker container to ensure deployment on Kubernetes.

- Development methodology: Considering the *maintainability* and *encapsulation* requirements, the software development methodology will be based on a Continuous Integration and Continuous Delivery (CI/CD) framework, emphasizing security through rigorous testing, static code analysis, vulnerability analysis in containerized libraries, etc.

## System Constraints

- Software Dependencies: The software should be developed using a specific programming language and framework (*Python* for the Backend and *React JS* for the Frontend), utilize a *Redys* database for short time storage and utilize a *PostgreSQL* relational database for long term storage. The software will respect strict compliance with OIDC and OAuth protocols, while using the official Python libraries defined by the standard documentation: https://openid.net/certified-open-id-developer-tools/.

- Regulatory and Legal Requirements: The software should comply with relevant data privacy and protection regulations, such as GDPR.

## Assumptions and Dependencies

- Assumption: Users will have a reliable internet connection to access the software.

- Dependency: The software development team will have access to the required development tools and infrastructure.
