from dataclasses import dataclass, field


@dataclass
class AddressWealthResponse:
    address: str
    value: float
    coin: str = field(init=False)


@dataclass
class AddressTxsBalanceResponse:
    coin: str = field(init=False)
    address: str = field(init=False)
    txs: int
    value_in: float
    value_out: float
    difference: float
