Assignment 03 — CHANGES

1. What I Changed

First, I changed the product data from tuples into a `Product` class. The class stores the product name, price, and category. I did this because using objects makes the product information easier to understand and use in the rest of the program.

Second, I created an `OrderItem` class instead of keeping each order item as a tuple. An `OrderItem` contains a `Product` object and a quantity. I also created an `Order` class that contains a customer and a list of order items. This uses composition because an order has a customer and has many items.

Third, I changed the customer tier code. The original program used several `if` and `elif` statements to check whether a customer was silver, gold, or platinum. I created a base `Customer` class and separate `Silver`, `Gold`, and `Platinum` classes. Each class has its own discount rate and points multiplier. This uses inheritance and polymorphism and removes the repeated tier checking.

Fourth, I separated the calculations from the receipt printing. The `Order` class now has methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. These methods return values instead of printing them. The `receipt()` method is responsible for creating the receipt text. This makes the calculations easier to understand and test.

Fifth, I replaced several magic numbers with named constants. For example, I used `TAX_RATE`, `DISCOUNT_LIMIT`, `BULK_LIMIT`, `BULK_RATE`, and `POINTS_STEP`. I also moved the tax calculation into the `Product` class. The constructors check basic invalid states, such as a quantity below 1 or an empty customer name.

After making the changes, I ran `python Assignment_03.py`. The program printed `PASS - behaviour is unchanged. Your refactor is safe.` This means the output from the refactored program was exactly the same as the original program.

2. Short Reflection

The biggest improvement was changing the old tuples into classes because the program became easier to understand. The customer tier classes also made the discount and points rules more organized. I tried to keep the code simple because I still need to understand and explain the code myself. The most important part was keeping the original output exactly the same, especially the receipt formatting and calculations. I checked this by running the self-test after making the changes and making sure it printed PASS.

3. Prompt Log

For this assignment, I used AI to help me understand and refactor the existing code while keeping the original behavior.

My first prompt was: "Complete this OOP refactoring assignment using the uploaded Assignment_03.py. Keep the output exactly the same and make the code simple."

The AI suggested using `Product`, `OrderItem`, `Customer`, customer tier subclasses, and `Order` classes. I used the suggestions but kept the implementation simple and made changes to the structure and naming.

My second prompt was: "Replace the tier if/elif logic with inheritance and polymorphism without changing the discount or points rules."

The AI suggested creating separate classes for the different customer tiers. I accepted this idea and checked that the discount percentages and points multipliers were still the same as the original program.

My third prompt was: "Separate the calculations from receipt printing and keep the exact original output."

The AI suggested putting the calculations into separate methods and using a `receipt()` method for the output. I used this approach and checked the complete output using the program's self-test.

My fourth prompt was: "Add simple constructor validation and replace magic numbers with named constants."

The AI suggested validating values in constructors and using named constants for the tax rate, discount threshold, bulk quantity, bulk discount, and points calculation. I used these changes and ran the self-test again.

For every change, I checked the code and ran `python Assignment_03.py`. The final result was PASS, so the refactored program kept the same behavior as the original. I also check with the ai whether the code has any errors in it and the result is positive.

**Ownership statement:** By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.
