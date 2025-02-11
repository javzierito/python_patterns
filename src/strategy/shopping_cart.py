from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class Item:
    name: str
    price: int


class ShippingStrategy(Protocol):
    def calculate_shipping_cost(self, items: list[Item]) -> int: ...


class StandardShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        total = sum(item.price for item in items)
        return 500 if total < 5000 else 0


class ExpressShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        total = sum(item.price for item in items)
        return 1000 if total < 5000 else 500


class OvernightShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        return 5000


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)

    def calculate_total_cost(self, shipping_strategy: ShippingStrategy) -> int:
        items_cost = sum(item.price for item in self.items)
        shipping_cost = shipping_strategy.calculate_shipping_cost(self.items)
        return items_cost + shipping_cost

    def add_item(self, item: Item) -> None:
        self.items.append(item)


def print_amount(amount: int) -> None:
    print(f"${amount/100:.2f}")


def main() -> None:
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Item(name="nice_pc", price=150000))
    shopping_cart.add_item(Item(name="logitech_mouse", price=3000))
    shopping_cart.add_item(Item(name="logi_keyboard", price=4000))
    print_amount(shopping_cart.calculate_total_cost(StandardShippingStrategy()))
    print_amount(shopping_cart.calculate_total_cost(ExpressShippingStrategy()))
    print_amount(shopping_cart.calculate_total_cost(OvernightShippingStrategy()))


if __name__ == "__main__":
    main()
