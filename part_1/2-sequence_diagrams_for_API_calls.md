# Objective

Develop sequence diagrams for at least four different API calls to illustrate the interaction between the layers (Presentation, Business Logic, Persistence) and the flow of information within the HBnB application. The sequence diagrams will help visualize how different components of the system interact to fulfill specific use cases, showing the step-by-step process of handling API requests.

---

## User Registration

### A user signs up for a new account.

```mermaid
sequenceDiagram
participant User
participant Presentation Layer(API)
participant Business Logic Layer(Models)
participant Persistence Layer(Database)

User->>Presentation Layer(API): Register User(email, password...)
Presentation Layer(API)->>Business Logic Layer(Models): Validate and Process Request
Business Logic Layer(Models)->>Persistence Layer(Database): Save Data
Persistence Layer(Database)-->>Business Logic Layer(Models): Confirm Save
Business Logic Layer(Models)-->>Presentation Layer(API): Return Response
Presentation Layer(API)-->>User: Return Success/Failure
```

This API call uses input data to create a new User. User gives datas to the Presentation Layer. The Presentation Layer sends the datas to the Business Logic Layer to create the new User. Then the Business Logic Layer sends the new User to Persistence Layer to save it in the database. Finally, each layer send success or failure response to previous layer up to the user.

## Place Creation

### A user creates a new place listing.

```mermaid
sequenceDiagram
participant User
participant Presentation Layer(API)
participant Business Logic Layer(Models)
participant Persistence Layer(Database)

User->>Presentation Layer(API): Create New Place(title, description...)
Presentation Layer(API)->>Business Logic Layer(Models): Validate and Process Request
Business Logic Layer(Models)->>Persistence Layer(Database): Save Data
Persistence Layer(Database)-->>Business Logic Layer(Models): Confirm Save
Business Logic Layer(Models)-->>Presentation Layer(API): Return Response
Presentation Layer(API)-->>User: Return Success/Failure
```

This API call uses input data to create a new Place. User gives datas to the Presentation Layer. The Presentation Layer sends the datas to the Business Logic Layer to create the new Place. Then the Business Logic Layer sends the new Place to Persistence Layer to save it in the database. Finally, each layer send success or failure response to previous layer up to the user.

## Review Submission

### A user submits a review for a place.

```mermaid
sequenceDiagram
participant User
participant Presentation Layer(API)
participant Business Logic Layer(Models)
participant Persistence Layer(Database)

User->>Presentation Layer(API): Create New Review(rating, comment...)
Presentation Layer(API)->>Business Logic Layer(Models): Validate and Process Request
Business Logic Layer(Models)->>Persistence Layer(Database): Save Data
Persistence Layer(Database)-->>Business Logic Layer(Models): Confirm Save
Business Logic Layer(Models)-->>Presentation Layer(API): Return Response
Presentation Layer(API)-->>User: Return Success/Failure
```

This API call uses input data to create a new Review. User gives datas to the Presentation Layer. The Presentation Layer sends the datas to the Business Logic Layer to create the new Review. Then the Business Logic Layer sends the new Review to Persistence Layer to save it in the database. Finally, each layer send success or failure response to previous layer up to the user.

## Fetching a List of Places

### A user requests a list of places based on certain criteria.

```mermaid
sequenceDiagram
participant User
participant Presentation Layer(API)
participant Business Logic Layer(Models)
participant Persistence Layer(Database)

User->>Presentation Layer(API): Request list of places(price, loction...)
Presentation Layer(API)->>Business Logic Layer(Models): Process Request with filters
Business Logic Layer(Models)->>Persistence Layer(Database): Fetch corresponding places
Persistence Layer(Database)-->>Business Logic Layer(Models): Send places
Business Logic Layer(Models)-->>Presentation Layer(API): Return Places Data
Presentation Layer(API)-->>User: Display places
```

This API call uses input data to retrieve Places. User gives datas to the Presentation Layer. The Presentation Layer sends the datas to the Business Logic Layer to apply filters. Then the Business Logic Layer fetch the corresponding places from Persistence Layer. Persistence Layer send Places to Business Logic Layer. Business Logic Layer return these Places datas to Presentation Layer. Presentation Layer display the list of Places.