import io
import contextlib


# ============================================================================== 
# LEGACY STORE SYSTEM  —  messy but working.   DO NOT EDIT THIS SECTION.
# ============================================================================== 
PRODUCTS = [
    ("Laptop", 1200.0, "electronics"),
    ("Headphones", 200.0, "electronics"),
    ("Coffee Beans", 15.0, "food"),
    ("Notebook", 5.0, "stationery"),
    ("Water Bottle", 10.0, "food"),
    ("Monitor", 300.0, "electronics"),
    ("Pen", 2.0, "stationery"),
]

TAXRATE = 0.07
foodtax = 0.0
ORDERS = [
    ("Alice", "gold", [(0, 1), (1, 2), (2, 3)]),
    ("Bob", "none", [(3, 10), (6, 5)]),
    ("Charlie", "platinum", [(5, 2), (4, 6), (2, 2)]),
    ("Dana", "silver", [(1, 1), (3, 3), (6, 10)]),
]


def calc(o):
    global TAXRATE
    n = o[0]; t = o[1]; items = o[2]
    sub = 0.0; tax = 0.0
    print("Receipt for " + n + " (" + t + ")")
    print("-" * 40)
    for it in items:
        pi = it[0]; q = it[1]
        p = PRODUCTS[pi][1]; nm = PRODUCTS[pi][0]; cat = PRODUCTS[pi][2]
        line = p * q
        sub = sub + line
        if cat == "food":
            tax = tax + line * foodtax
        else:
            tax = tax + line * TAXRATE
        print(nm + " x" + str(q) + " = " + str(line))
    d = 0.0
    if t == "none":
        d = 0.0
    elif t == "silver":
        if sub > 100: d = sub * 0.05
        else: d = sub * 0.02
    elif t == "gold":
        if sub > 100: d = sub * 0.10
        else: d = sub * 0.05
    elif t == "platinum":
        if sub > 100: d = sub * 0.15
        else: d = sub * 0.10
    totalqty = 0
    for it in items:
        totalqty = totalqty + it[1]
    if totalqty >= 10:
        d = d + sub * 0.03
    total = sub - d + tax
    pts = 0
    if t == "none": pts = int(total // 10)
    elif t == "silver": pts = int(total // 10) * 2
    elif t == "gold": pts = int(total // 10) * 3
    elif t == "platinum": pts = int(total // 10) * 5
    print("-" * 40)
    print("Subtotal: " + str(round(sub, 2)))
    print("Discount: " + str(round(d, 2)))
    print("Tax: " + str(round(tax, 2)))
    print("Total: " + str(round(total, 2)))
    print("Points earned: " + str(pts))
    print("")
    return total


def legacy_main():
    grand = 0.0
    for o in ORDERS:
        grand = grand + calc(o)
    print("GRAND TOTAL (all orders): " + str(round(grand, 2)))


# ============================================================================== 
# BEHAVIOUR LOCK  —  DO NOT EDIT.
# ============================================================================== 
def capture(fn):
    """Run fn() and return everything it printed, as a string."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


GOLDEN_OUTPUT = capture(legacy_main)


# ============================================================================== 
# YOUR REFACTORED SOLUTION
# ============================================================================== 
TAX_RATE = 0.07
FOOD = "food"
DISCOUNT_LIMIT = 100
BULK_LIMIT = 10
BULK_RATE = 0.03
POINTS_STEP = 10


class Product:
    def __init__(self, name, price, category):
        if not name or price < 0:
            raise ValueError("Invalid product")
        self.name = name
        self.price = price
        self.category = category

    def tax(self, amount):
        if self.category == FOOD:
            return 0.0
        return amount * TAX_RATE


class OrderItem:
    def __init__(self, product, quantity):
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        self.product = product
        self.quantity = quantity

    def amount(self):
        return self.product.price * self.quantity


class Customer:
    def __init__(self, name):
        if not name:
            raise ValueError("Customer name is required")
        self.name = name

    def discount_rate(self, subtotal):
        return 0.0

    def points_multiplier(self):
        return 1

    def tier_name(self):
        return "none"


class Silver(Customer):
    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_LIMIT:
            return 0.05
        return 0.02

    def points_multiplier(self):
        return 2

    def tier_name(self):
        return "silver"


class Gold(Customer):
    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_LIMIT:
            return 0.10
        return 0.05

    def points_multiplier(self):
        return 3

    def tier_name(self):
        return "gold"


class Platinum(Customer):
    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_LIMIT:
            return 0.15
        return 0.10

    def points_multiplier(self):
        return 5

    def tier_name(self):
        return "platinum"


class Order:
    def __init__(self, customer, items):
        if not items:
            raise ValueError("Order needs at least one item")
        self.customer = customer
        self.items = items

    def subtotal(self):
        return sum(item.amount() for item in self.items)

    def discount(self):
        subtotal = self.subtotal()
        discount = subtotal * self.customer.discount_rate(subtotal)
        quantity = sum(item.quantity for item in self.items)
        if quantity >= BULK_LIMIT:
            discount += subtotal * BULK_RATE
        return discount

    def tax(self):
        return sum(item.product.tax(item.amount()) for item in self.items)

    def total(self):
        return self.subtotal() - self.discount() + self.tax()

    def points(self):
        return int(self.total() // POINTS_STEP) * self.customer.points_multiplier()

    def receipt(self):
        lines = [
            "Receipt for " + self.customer.name + " (" + self.customer.tier_name() + ")",
            "-" * 40,
        ]

        for item in self.items:
            lines.append(
                item.product.name + " x" + str(item.quantity) +
                " = " + str(item.amount())
            )

        lines.extend([
            "-" * 40,
            "Subtotal: " + str(round(self.subtotal(), 2)),
            "Discount: " + str(round(self.discount(), 2)),
            "Tax: " + str(round(self.tax(), 2)),
            "Total: " + str(round(self.total(), 2)),
            "Points earned: " + str(self.points()),
            "",
        ])
        return "\n".join(lines)


def make_products():
    return [
        Product("Laptop", 1200.0, "electronics"),
        Product("Headphones", 200.0, "electronics"),
        Product("Coffee Beans", 15.0, "food"),
        Product("Notebook", 5.0, "stationery"),
        Product("Water Bottle", 10.0, "food"),
        Product("Monitor", 300.0, "electronics"),
        Product("Pen", 2.0, "stationery"),
    ]


def make_customer(name, tier):
    classes = {
        "none": Customer,
        "silver": Silver,
        "gold": Gold,
        "platinum": Platinum,
    }
    return classes[tier](name)


def make_orders():
    products = make_products()
    result = []
    for name, tier, raw_items in ORDERS:
        customer = make_customer(name, tier)
        items = [OrderItem(products[index], quantity)
                 for index, quantity in raw_items]
        result.append(Order(customer, items))
    return result


def refactored_main():
    """Print every receipt and the grand total — same output as legacy_main()."""
    grand = 0.0
    for order in make_orders():
        print(order.receipt())
        grand += order.total()
    print("GRAND TOTAL (all orders): " + str(round(grand, 2)))


# ============================================================================== 
# SELF-TEST  —  DO NOT EDIT.
# ============================================================================== 
def _check():
    try:
        your_output = capture(refactored_main)
    except NotImplementedError:
        print("Solution not implemented yet.\n")
        print("Below is the TARGET output your refactor must reproduce exactly:\n")
        print(GOLDEN_OUTPUT)
        return

    if your_output == GOLDEN_OUTPUT:
        print("PASS - behaviour is unchanged. Your refactor is safe.\n")
    else:
        print("FAIL - the output changed, so this is not yet a valid refactor.\n")
        g = GOLDEN_OUTPUT.splitlines()
        y = your_output.splitlines()
        for i in range(max(len(g), len(y))):
            gl = g[i] if i < len(g) else "<no line>"
            yl = y[i] if i < len(y) else "<no line>"
            if gl != yl:
                print("First difference at line " + str(i + 1) + ":")
                print("  expected: " + repr(gl))
                print("  yours:    " + repr(yl))
                break


if __name__ == "__main__":
    _check()
