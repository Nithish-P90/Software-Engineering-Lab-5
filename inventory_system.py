"""Inventory system with basic add/remove, persistence, and reports."""

import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

# Global in-memory store
stock_data: dict[str, int] = {}


def add_item(item: str = "default", qty: int = 0, logs=None) -> None:
    """Add qty of an item (can be negative). Appends a human log entry."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int) or not item:
        raise ValueError("item must be non-empty str and qty must be int")
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("added %s of %s (new qty=%s)", qty, item, stock_data[item])


def remove_item(item: str, qty: int) -> None:
    """Remove qty of an item; delete key if qty <= 0; warn if item missing."""
    if not isinstance(item, str) or not isinstance(qty, int):
        raise ValueError("invalid types for item/qty")
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("removed %s entirely (qty <= 0)", item)
    except KeyError:
        logging.warning("attempted to remove missing item: %s", item)


def get_qty(item: str) -> int:
    """Return current quantity for item (0 if missing)."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load inventory from JSON file into stock_data."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("inventory file is not a JSON object")
        stock_data.clear()
        stock_data.update({str(k): int(v) for k, v in data.items()})
        logging.info("data loaded from %s", file)
    except FileNotFoundError:
        logging.warning("file %s not found; starting with empty stock", file)


def save_data(file: str = "inventory.json") -> None:
    """Persist stock_data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, ensure_ascii=False, indent=2)
    logging.info("data saved to %s", file)


def print_data() -> None:
    """Pretty-print the inventory."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> list[str]:
    """Return items whose qty is below threshold."""
    return [i for i, q in stock_data.items() if q < threshold]


def main() -> None:
    """Demo run for the inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    try:
        # This will now raise a clear ValueError (type check)
        add_item(123, "ten")  # type: ignore[arg-type]
    except ValueError as exc:
        logging.error("bad add_item call: %s", exc)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Removed insecure eval(); no equivalent needed here.


if __name__ == "__main__":
    main()
