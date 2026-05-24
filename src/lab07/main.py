from app import LibraryApp
from cli import CLI


def main() -> None:
    """Точка входа в приложение."""
    app = LibraryApp()
    cli = CLI(app)
    cli.run()


if __name__ == "__main__":
    main()