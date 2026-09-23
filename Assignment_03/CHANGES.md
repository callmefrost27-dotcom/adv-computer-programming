# Assignment 03 — CHANGES

**Name:** ______________________  **Student ID:** ______________________

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products were stored as tuples inside one list. | I made a `Product` class containing the product name, price, and category. | Classes / encapsulation | Ran `python Assignment_03.py` and checked that it printed PASS. |
| 2 | Customers, orders, and items were represented by nested tuples. | I made `Customer`, `Order`, and `OrderItem` objects. An order contains one customer and several items. | Composition | Ran the self-test and checked the receipt output against the original output. |
| 3 | The membership tier rules used several `if/elif` conditions. | I made a base `Customer` class and `Silver`, `Gold`, and `Platinum` subclasses. | Inheritance / polymorphism | Checked the four tiers against the original discount and points rules, then ran the self-test. |
| 4 | The original `calc()` function calculated values and printed the receipt together. | I moved the calculations into methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. `receipt()` creates the output text. | Separation of calculation and I/O | Compared the complete output with the original locked output; the program printed PASS. |
| 5 | The original used a global tax variable and several unexplained numbers. | I used named constants such as `TAX_RATE`, `DISCOUNT_LIMIT`, `BULK_LIMIT`, and `POINTS_STEP`. | Encapsulation / clean code | Ran the self-test again and confirmed the final output stayed unchanged. |

## 2 · Short reflection (4–6 sentences)

The biggest improvement for me was turning the product and order data into objects because the program is easier to understand. The membership classes also make the different discount and points rules easier to find. I kept the original business rules instead of adding any new behaviour. The receipt formatting needed extra care because a small change to a line or blank space can make the behaviour test fail. I ran `python Assignment_03.py` after the changes and used the PASS result to check that the output was unchanged.

## 3 · Prompt log (Level 2 — required)

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Complete this OOP refactoring assignment from the uploaded file. Keep the output exactly the same and make the code simple." | Suggested simple `Product`, `OrderItem`, `Customer`, tier subclasses, and `Order` classes. | Edited and kept the parts that fit the assignment. | Ran `python Assignment_03.py` and checked for PASS. |
| 2 | "Replace the membership tier if/elif logic with inheritance and polymorphism without changing the existing rules." | Suggested separate classes for the membership tiers with methods for discount rates and point multipliers. | Accepted with my own method and class names. | Compared each tier's rules with the original code and ran the test. |
| 3 | "Separate the calculations from receipt printing but keep exactly the same output." | Suggested calculation methods that return values and a separate `receipt()` method. | Edited the receipt formatting to match the original. | Ran the program and checked that the output comparison passed. |
| 4 | "Add simple constructor validation and replace magic numbers with named constants." | Suggested basic validation and constants for the tax, thresholds, bulk discount, and points calculation. | Accepted and kept the implementation simple. | Read through the changed code and ran the self-test again. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left in the refactored domain model — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global` in the refactored solution; magic numbers are named.
- [x] The change table and reflection are filled in.
- [x] The prompt log and ownership statement are included.
