## Usage of "SOLID principles"

1. **Single Responsibility Principle (SRP)**: A class should have only one reason to change. In other words, a class should have only one responsibility.

**Example**
Suppose you're developing a system for an online store. You might have separate classes for handling product information, customer data, and order processing. Each class should handle its specific responsibilities without unnecessary coupling.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class OrderProcessor:
    def process_order(self, product, customer):
        # Process the order logic here
        pass
```

2. **Open/Closed Principle (OCP)**: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means you should be able to add new functionality without changing existing code.

**Example**
Suppose you have a basic logging system. Instead of modifying the existing logger, you can create new loggers for different outputs (e.g., file, console) without changing the existing code.

```python
class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class FileLogger(Logger):
    def log(self, message):
        # Write to a file
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        # Print to the console
        pass
```

3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without affecting the correctness of the program.

**Example**
If you have a base class for shapes, any subclass (like Circle or Square) should be usable interchangeably without breaking the expected behavior.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def area(self):
        return self.side_length * self.side_length
```

4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.

**Example**
Avoid creating large, monolithic interfaces. Instead, create smaller, focused interfaces that cater to the specific needs of the clients.

```python
class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self, document):
        pass

class FaxMachine:
    def fax(self, document):
        pass

# Better approach using ISP
class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self, document):
        pass

class Fax:
    def fax(self, document):
        pass
```

5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

**Example**
Instead of tightly coupling high-level modules to specific low-level modules, introduce abstractions (interfaces or abstract classes) that allow for more flexibility and easier testing.

```python
class SwitchableDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(SwitchableDevice):
    def turn_on(self):
        # Implement turn on for light bulb
        pass

    def turn_off(self):
        # Implement turn off for light bulb
        pass

class Fan(SwitchableDevice):
    def turn_on(self):
        # Implement turn on for fan
        pass

    def turn_off(self):
        # Implement turn off for fan
        pass
```
