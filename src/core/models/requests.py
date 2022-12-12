from dataclasses import dataclass


@dataclass
class AddressWealthRequest:
    coin: str
    address: str


@dataclass
class AddressTxsBalanceRequest:
    coin: str
    address: str
