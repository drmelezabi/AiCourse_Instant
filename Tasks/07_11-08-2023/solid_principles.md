## Solid principles

1. **Single Responsibility Principle (SRP)**: A class should have only one reason to change, meaning it should have only one responsibility.

**Bad Code (SRP Violation):**

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def calculate_total(self, items):
        # Calculate total price
        pass

    def send_order_confirmation(self):
        # Send email to customer
        pass
```

**Good Code (SRP Compliant):**

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class OrderCalculator:
    def calculate_total(self, items):
        # Calculate total price
        pass

class EmailSender:
    def send_order_confirmation(self, customer):
        # Send email to customer
        pass
```

2. **Open/Closed Principle (OCP)**: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

**Bad Code (OCP Violation):**

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Circle):
                total_area += 3.14 * shape.radius ** 2
            # More shape types...
        return total_area
```

**Good Code (OCP Compliant):**

```python
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        return total_area
```

3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without affecting the correctness of the program.

**Bad Code (LSP Violation):**

```python
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
```

**Good Code (LSP Compliant):**

```python
class Bird:
    def move(self):
        pass

class Ostrich(Bird):
    def move(self):
        # Implement ostrich-specific movement
        pass
```

4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.

**Bad Code (ISP Violation):**

```python
class Worker:
    def work(self):
        pass

class Manager:
    def manage(self):
        pass
```

**Good Code (ISP Compliant):**

```python
class Workable:
    def work(self):
        pass

class Manageable:
    def manage(self):
        pass

class Worker(Workable):
    pass

class Manager(Workable, Manageable):
    pass
```

5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

**Bad Code (DIP Violation):**

```python
class LightBulb:
    def turn_on(self):
        pass

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()
```

**Good Code (DIP Compliant):**

```python
class Switchable:
    def operate(self):
        pass

class LightBulb(Switchable):
    def operate(self):
        self.turn_on()

    def turn_on(self):
        pass

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.operate()
```

Applying the SOLID principles can lead to more modular, maintainable, and flexible code, making it easier to extend and modify your software as requirements change.
