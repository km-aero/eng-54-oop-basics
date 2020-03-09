# OOP Basics

We will look at:
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

### Class
Wrappers to define how an object looks and behaves.
Classes will wrap characteristics as attributes, behaviours and methods

### Method VS Functions
Methods are functions that belong to a specific data type.
Functions are anonymous and can be called anywhere.
Methods need to be called in an instance(class)

### Characteristics
Attributes assigned to each instance

### Instance
Occurrence of something.

### Self
Self refers to the instance initialised

### Abstraction
Ability to hide complexity using:
- Separation of concerns
- documentation
    - Specify which methods and how to use them
- inheritance

### Inheritance
Ability to pass to another class all methods and characteristics

'''python
class Animal():
    pass
    
class reptile(Animal):
'''

### Encapsulation
Making method or attributes private.

When methods/attributes are private, they can only be called by its own functions or within a class.

### Polymorphism
Means many forms.
It is the ability to overwrite methods and recall method from parent class using .super()

### .super()
It allows you to call methods from parent class.

Usage and case in point:
- when you want to overwrite a method
- when you want to add new functionality to a new method
- 