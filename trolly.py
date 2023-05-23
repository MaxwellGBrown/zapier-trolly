"""Simple WSGI server backing a Zapier integration to emulate an event bus."""
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


class ConfigBuilder:
    """Builder class to construct a pyramid.Configurator."""

    def __init__(self):
        self.config = Configurator()

    def __call__(self):
        self.config.add_route('hello', '/')
        self.config.add_view(lambda r: Response("Hello world"), route_name='hello')

        return self.config.make_wsgi_app()


def app():
    """Build WSGI App mapping environmental settings to ConfigBuilder."""
    config_builder = ConfigBuilder()
    return config_builder()


if __name__ == "__main__":
    server = make_server('0.0.0.0', 6543, app())
    server.serve_forever()
