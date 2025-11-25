from src.di import build_container

if __name__ == "__main__":
    container = build_container()
    container["cli_app"].run()
