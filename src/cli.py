import argparse
from src.main import run_pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--query", required=True)

    args = parser.parse_args()

    run_pipeline(args.pdf, args.query)


if __name__ == "__main__":
    main()
