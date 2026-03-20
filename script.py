import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Program started")

    # Check for command-line arguments
    if len(sys.argv) < 2:
        logging.warning("No arguments provided.")
        print("Usage: python script.py <your_name>")
        sys.exit(1)

    name = sys.argv[1]
    logging.debug(f"Received argument: {name}")

    print(f"Hello, {name}!")
    logging.info("Program finished successfully")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)