## Behavioral Design Patterns

<a name="Chain-of-Responsibility-Method"></a>

### 1. Chain of Responsibility Method

The Chain of Responsibility pattern allows multiple objects to handle a request without the sender needing to know which object will ultimately process it.

Example in Python:

```python
class Handler:
    def set_successor(self, successor):
        pass

    def handle_request(self, request):
        pass

class ConcreteHandler1(Handler):
    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        if request == "Request1":
            print("ConcreteHandler1: Handling Request1")
        else:
            self.successor.handle_request(request)

class ConcreteHandler2(Handler):
    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        if request == "Request2":
            print("ConcreteHandler2: Handling Request2")
        else:
            self.successor.handle_request(request)

handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()

handler1.set_successor(handler2)
handler1.handle_request("Request1")  # Output: ConcreteHandler1: Handling Request1
handler1.handle_request("Request2")  # Output: ConcreteHandler2: Handling Request2
```

<a name="Command-Method"></a>

### 2. Command Metho

The Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests and queuing of requests.

Example in Python:

```python
class Receiver:
    def action(self):
        print("Receiver: Performing action")

class Command:
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()

class Invoker:
    def set_command(self, command):
        self._command = command

    def execute_command(self):
        self._command.execute()

receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()

invoker.set_command(command)
invoker.execute_command()  # Output: Receiver: Performing action
```

<a name="Iterator-Method"></a>

### 3. Iterator Method

The Iterator pattern provides a way to access elements of a collection sequentially without exposing its underlying representation.

Example in Python:

```python
class MyCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return MyIterator(self._items)

class MyIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

collection = MyCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

for item in collection:
    print(item)
# Output:
# Item 1
# Item 2
# Item 3
```

<a name="Mediator-Method"></a>

### 4. Mediator Method

The Mediator pattern defines an object that encapsulates how a set of objects interact, allowing loose coupling between these objects.

Example in Python:

```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self._colleague1 = colleague1
        self._colleague2 = colleague2

    def notify(self, sender, event):
        if sender == self._colleague1:
            self._colleague2.handle_event(event)
        elif sender == self._colleague2:
            self._colleague1.handle_event(event)

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, event):
        self._mediator.notify(self, event)

    def handle_event(self, event):
        pass

class ConcreteColleague1(Colleague):
    def handle_event(self, event):
        print(f"ConcreteColleague1: Received event - {event}")

class ConcreteColleague2(Colleague):
    def handle_event(self, event):
        print(f"ConcreteColleague2: Received event - {event}")

mediator = ConcreteMediator(ConcreteColleague1(mediator), ConcreteColleague2(mediator))
colleague1 = mediator._colleague1
colleague2 = mediator._colleague2

colleague1.send("Event from Colleague1")
# Output: ConcreteColleague2: Received event - Event from Colleague1
```

<a name="Memento-Method"></a>

### 5. Memento Method

The Memento pattern allows capturing an object's internal state so that it can be restored to that state later.

Example in Python:

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self._state = memento.get_state()

originator = Originator()

originator.set_state("State 1")
memento = originator.create_memento()

originator.set_state("State 2")
print(originator._state)  # Output: State 2

originator.restore_memento(memento)
print(originator._state)  # Output: State 1
```

<a name="Observer-Method"></a>

### 6. Observer Method

The Observer pattern defines a one-to-many relationship between objects, so that when one object changes state, all its dependents are notified and updated automatically.

Example in Python:

```python
class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello observers!")
# Output:
# Received message: Hello observers!
# Received message: Hello observers!
```

<a name="State-Method"></a>

### 7. State Method

The State pattern allows an object to change its behavior when its internal state changes. It appears as if the object changed its class.

Example in Python:

```python
class State:
    def handle(self):
        pass

class ConcreteState1(State):
    def handle(self):
        print("ConcreteState1: Handling request in State 1")

class ConcreteState2(State):
    def handle(self):
        print("ConcreteState2: Handling request in State 2")

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Example usage:
state1 = ConcreteState1()
state2 = ConcreteState2()

context = Context(state1)
context.request()  # Output: ConcreteState1: Handling request in State 1

context.set_state(state2)
context.request()  # Output: ConcreteState2: Handling request in State 2
```

<a name="Strategy-Method"></a>

### 8. Strategy Method

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows a client to choose an algorithm from a family of algorithms at runtime.

Example in Python:

```python
class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# Example usage:
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context = Context(strategy_a)
context.execute_strategy()  # Output: Executing strategy A

context.set_strategy(strategy_b)
context.execute_strategy()  # Output: Executing strategy B
```

<a name="Template-Method"></a>

### 9. Template Method

The Template Method pattern defines the structure of an algorithm in the base class but allows subclasses to override specific steps of the algorithm without changing its structure.

Example in Python:

```python
class AbstractClass:
    def template_method(self):
        self.step1()
        self.step2()

    def step1(self):
        pass

    def step2(self):
        pass

class ConcreteClassA(AbstractClass):
    def step1(self):
        print("ConcreteClassA: Step 1")

    def step2(self):
        print("ConcreteClassA: Step 2")

class ConcreteClassB(AbstractClass):
    def step1(self):
        print("ConcreteClassB: Step 1")

    def step2(self):
        print("ConcreteClassB: Step 2")

# Example usage:
class_a = ConcreteClassA()
class_b = ConcreteClassB()

class_a.template_method()
# Output:
# ConcreteClassA: Step 1
# ConcreteClassA: Step 2

class_b.template_method()
# Output:
# ConcreteClassB: Step 1
# ConcreteClassB: Step 2
```

<a name="Visitor-Method"></a>

### 10. Visitor Method

The Visitor pattern lets you add further operations to objects without having to modify them. It separates algorithms from the objects on which they operate.

Example in Python:

```python
class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit(self, element):
        print(f"ConcreteVisitor1: Visiting {element}")

class ConcreteVisitor2(Visitor):
    def visit(self, element):
        print(f"ConcreteVisitor2: Visiting {element}")

class Element:
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit("ConcreteElementA")

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit("ConcreteElementB")

# Example usage:
visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

element_a = ConcreteElementA()
element_b = ConcreteElementB()

element_a.accept(visitor1)  # Output: ConcreteVisitor1: Visiting ConcreteElementA
element_b.accept(visitor2)  # Output: ConcreteVisitor2: Visiting ConcreteElementB
```

These are the explanations and examples of the Behavioral Design Patterns. If you have any more questions or need further clarification, feel free to ask!
