from dataclasses import dataclass, field


@dataclass
class AddressWealthResponse:
    address: str
    value: float
    coin: str = field(init=False)
