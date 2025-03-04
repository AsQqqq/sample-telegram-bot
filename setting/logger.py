from cololog import cololog
import os

logger = cololog("__name__", path_print=False, log_to_file=True, log_dir="logs")


def clear() -> None:
    """
    Очищает консоль на Windows и Unix-подобных системах.
    """

    os.system('cls' if os.name == 'nt' else 'clear')