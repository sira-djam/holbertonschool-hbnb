classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
}
class FacadePattern {
    +handleRequest
}
class BusinessLogicLayer {
    +ModelClasses
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> FacadePattern : Calls API
FacadePattern --> BusinessLogicLayer : Calls Business Methods
BusinessLogicLayer --> PersistenceLayer : Database Operations