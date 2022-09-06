from dataclasses import dataclass, field
from typing import Optional

import uvicorn
from fastapi import FastAPI

from src.controllers.http import make_http_controller


@dataclass
class WhaleAPI:
    http_controller: Optional[FastAPI] = None
    config: dict = field(default_factory=dict)
    env: Optional[str] = None

    def load_config(self) -> None:
        print("Loading config...")

    def set_up(self) -> None:
        self.http_controller = make_http_controller()

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=80, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()
