class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers:
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for customer_name, purchases in self.customers.items():
            total = self.calculate_total_with_tax(purchases)
            print(customer_name)
            self.print_discount_status(total)
            self.print_customer_priority(total)

    def calculate_total_with_tax(self, purchases):
        total = 0
        for purchase in purchases:
            price = purchase['price']
            total += self.apply_tax(price)
        return total

    def apply_tax(self, price):
        if price > self.tax_threshold:
            return price * (1 + self.tax_rate)
        return price

    def print_discount_status(self, total):
        if total > self.discount_threshold:
            print("Eligible for discount")
        elif total > 300:
            print("Potential future discount customer")
        else:
            print("No discount")

    def print_customer_priority(self, total):
        if total > 1000:
            print("VIP Customer!")
        elif total > 800:
            print("Priority Customer")

    def calculate_shipping_fee(self, purchases):
        return 50 if self.has_heavy_item(purchases) else 20

    def has_heavy_item(self, purchases):
        return any(p.get('weight', 0) > 20 for p in purchases)


def calculate_shipping_fee_for_heavy_items(purchases):
    return 50 if any(p.get('weight', 0) > 20 for p in purchases) else 20

def calculate_shipping_fee_for_fragile_items(purchases):
    return 60 if any(p.get('fragile', False) for p in purchases) else 25


# Removed: flat_tax = 0.2  # Unused
