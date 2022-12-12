from dataclasses import dataclass, field


@dataclass
class AddressWealthResponse:
    address: str
    value: float
    coin: str = field(init=False)


@dataclass
class AddressTxsBalanceResponse:
    value_in: float
    value_out: float
    difference: float
