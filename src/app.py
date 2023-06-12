from fastapi import FastAPI


class WhaleAPI:
    http_controller: FastAPI

    def _set_up(self):
        pass

    def _create_controller(self):
        pass

    def _start_service(self):
        pass

    def set_up_and_start_service(self):
        self._set_up()
        self._create_controller()
        self._start_service()
