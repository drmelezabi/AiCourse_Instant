## Clean code principles

1. **Meaningful Names:**
   Use descriptive names for variables, functions, classes, and modules to make the code self-explanatory.

   ```python
   # Bad:
   def func(a, b):
       return a + b

   # Good:
   def calculate_sum(x, y):
       return x + y
   ```

2. **Functions Should Do One Thing:**
   Keep functions focused and concise, performing a single task.

   ```python
   # Bad:
   def process_data_and_send_email(data):
       # Process data
       ...
       # Send email
       ...

   # Good:
   def process_data(data):
       ...

   def send_email(subject, message):
       ...
   ```

3. **Comments Are a Last Resort:**
   Strive to write self-explanatory code, reducing the need for excessive comments.

   ```python
   # Bad:
   # Calculate the square of a number
   def square(x):
       return x * x

   # Good:
   def calculate_square(x):
       return x * x
   ```

4. **Small Functions:**
   Keep functions short and focused to improve readability and ease of maintenance.

   ```python
   # Bad:
   def complex_calculation(data):
       ...
       ...
       ...

   # Good:
   def simple_calculation(data):
       ...
   ```

5. **DRY (Don't Repeat Yourself):**
   Avoid duplicating code; use functions, classes, and modules to encapsulate and reuse logic.

   ```python
   # Bad:
   result1 = 2 * 3
   result2 = 2 * 3

   # Good:
   factor = 2
   result1 = factor * 3
   result2 = factor * 3
   ```

6. **Single Responsibility Principle (SRP):**
   Classes and functions should have a single, well-defined responsibility.

   ```python
   # Bad:
   class User:
       def create_user(self, data):
           ...

       def send_email(self, email):
           ...

   # Good:
   class User:
       def create(self, data):
           ...

   class EmailSender:
       def send(self, email):
           ...
   ```

7. **Avoid Magic Numbers:**
   Use named constants or variables to make the code more expressive and maintainable.

   ```python
   # Bad:
   if status == 2:
       ...

   # Good:
   STATUS_COMPLETED = 2
   if status == STATUS_COMPLETED:
       ...
   ```

8. **Consistent Formatting:**
   Follow a consistent code style and formatting to improve readability and reduce confusion.

   ```python
   # Bad:
   def my_function(x,y):
       return x+y

   # Good:
   def my_function(x, y):
       return x + y
   ```

9. **Open/Closed Principle:**
   Code entities (classes, functions) should be open for extension but closed for modification.

   ```python
   # Bad:
   def calculate_total(items, discount):
       ...

   # Good:
   class DiscountCalculator:
       def apply_discount(self, items):
           ...
   ```

10. **Unit Tests:**
    Write comprehensive unit tests to ensure code correctness and facilitate future changes.

    ```python
    # Bad:
    def divide(a, b):
        return a / b

    # Good:
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```
