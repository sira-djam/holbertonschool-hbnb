# Objective

Design a detailed class diagram for the Business Logic layer of the HBnB application. This diagram will depict the entities within this layer, their attributes, methods, and the relationships between them. The primary goal is to provide a clear and detailed visual representation of the core business logic, focusing on the key entities: User, Place, Review, and Amenity.

---

```mermaid
classDiagram
direction RL
class BaseModel:::className {
    <<Abstract Base Class>>
    int id
    string datetime
    add()
    update()
    del()
}
class User {
    string Email
    string First Name
    string Last Name
    string Password
    boolean Administrator
    list places
    change_permission()
    list_places()
}
class Place {
    string Title
    string Description
    float Price
    float Latitude
    float Longitude
    list Amenities
    list_amenities()
    list_review()
}
class Review {
    float Rating
    string Comment
}
class Amenity {
    string Name
    string Description
}
User <|-- BaseModel
Place <|-- BaseModel
Review <|-- BaseModel
Amenity <|-- BaseModel
User "1.*" <|--|>"1" Place
User "0.n" <|--|> "1" Review
Place "0.n" <|--|> "1" Review
Place "0.n" <|--|> "1" Amenity

%% Custom CSS for Mermaid
classDef default fill:#808080,stroke:#00ffff,color:white;
classDef base fill:#3a8eba,stroke:#00ffff;

User:::default
Place:::default
Review:::default
Amenity:::default
BaseModel:::base
```
## Class Description

User : class containing user information like names, email, password... It can list places created.\
Place : class containing places information like description, price, location... It can list associated amenities and reviews.\
Review : class containing reviews information like ratings and comments.\
Amenity : class containing amenities information like name and description.\
BaseModel : Abstract Base Class containing information common to all classes of the BusinessLogicLayer

## Class Relationships

All classes inherits attributes and methods from ABC BaseModel\
Users : can creates multiple reviews and owns multiples places\
Places : owned by a User, can have list of amenities and can be reviewed multiple times.\
Amenities : associated with a Place.\
Reviews : can be created by User about Place.