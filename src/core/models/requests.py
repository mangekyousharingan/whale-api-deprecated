from dataclasses import dataclass


@dataclass
class AddressWealthRequest:
    coin: str
    address: str
