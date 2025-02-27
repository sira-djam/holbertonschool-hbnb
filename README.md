# HBnB Project


## Summary
- [Description](#description)
- [Repo](#Repo)
- [UML](#UML)
- [Authors](#Authors)

## Description

HBnB (AirBnB Clone) project is about creating, step by step, a complete web application inspired by Airbnb, with a well-structured and scalable architecture.


## Repo

[Projet HBNB](https://github.com/JorreJ/holbertonschool-hbnb)


## Part 1 : UML
- 0 High-Level Package Diagram
- 1 Detailed Class Diagram for Business Logic Layer
- 2 Sequence Diagrams for API Calls
- 3 Documentation Compilation

### 0. High-Level Package Diagram
Create a high-level package diagram that illustrates the three-layer architecture of the HBnB application and the communication between these layers via the facade pattern. This diagram will provide a conceptual overview of how the different components of the application are organized and how they interact with each other.

[Package Diagram](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/part_1/0-high_level_package_diagram.md)

### 1. Detailed Class Diagram for Business Logic Layer
Design a detailed class diagram for the Business Logic layer of the HBnB application. This diagram will depict the entities within this layer, their attributes, methods, and the relationships between them. The primary goal is to provide a clear and detailed visual representation of the core business logic, focusing on the key entities: User, Place, Review, and Amenity.

[Class Diagram](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/part_1/1-detailed_class_diagram_for_business_logic_layer.md)



### 2. Sequence Diagrams for API Calls
Develop sequence diagrams for at least four different API calls to illustrate the interaction between the layers (Presentation, Business Logic, Persistence) and the flow of information within the HBnB application. The sequence diagrams will help visualize how different components of the system interact to fulfill specific use cases, showing the step-by-step process of handling API requests.

[Sequence Diagrams](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/part_1/2-sequence_diagrams_for_API_calls.md)

### 3. Documentation Compilation

Compile all the diagrams and explanatory notes created in the previous tasks into a comprehensive technical document. This document will serve as a detailed blueprint for the HBnB project, guiding the implementation phases and providing a clear reference for the system’s architecture and design.

[Technical Documentation](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/part_1/3-documentation_compilation.md)

## Part 2 : BL and API

- Directories and files purposes
- Requirements

### Directories and files purposes

- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the API endpoints, organized by version (`v1/`).
- The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
- The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` will contain a brief overview of the project.

### Requirements

to install dependencies :

```text
pip install -r requirements.txt
```

to run the application :

```text
python run.py
```

### Entities

In this task, we have :

1. Implemented classes
2. Ensure relationships
3. Handle attribute validation and updates

- [BaseModel](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/app/models/basemodel.py)
- [User](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/app/models/user.py)
- [Place](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/app/models/place.py)
- [Amenity](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/app/models/amenity.py)
- [Review](https://github.com/JorreJ/holbertonschool-hbnb/blob/main/app/models/review.py)

## Authors

- [@Jade Jorré](https://github.com/JorreJ)
- [@Blandine Soileux](https://github.com/sira-djam)