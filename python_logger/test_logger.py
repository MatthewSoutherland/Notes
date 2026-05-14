# test_logger.py

import logging
import pathlib
import json
import logging.config
import threading
import time

logger = logging.getLogger("my_app")


def setup_logging():
    config_file = pathlib.Path("config/logging_config.json")

    with open(config_file) as f:
        config = json.load(f)

    logging.config.dictConfig(config)


def test_basic_levels():
    print("\n=== BASIC LEVEL TEST ===")

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


def test_extra_fields():
    print("\n=== EXTRA FIELD TEST ===")

    logger.info("user logged in", extra={"user_id": 123, "ip_address": "127.0.0.1", "device": "desktop"})

    logger.warning("database timeout", extra={"user_id": 123, "db_host": "localhost", "retry_count": 5})


def test_exception_logging():
    print("\n=== EXCEPTION TEST ===")

    try:
        x = 1 / 0
    except ZeroDivisionError:
        logger.exception("division failed", extra={"operation": "division", "input_value": 0})


def test_stack_info():
    print("\n=== STACK INFO TEST ===")

    logger.warning("stack test", stack_info=True)


def worker(thread_id):
    for i in range(3):
        logger.info(f"thread message {i}", extra={"thread_test_id": thread_id})
        time.sleep(0.1)


def test_multithreading():
    print("\n=== THREAD TEST ===")

    threads = []

    for i in range(3):
        t = threading.Thread(target=worker, args=(i,), name=f"worker-{i}")

        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def test_large_message():
    print("\n=== LARGE MESSAGE TEST ===")

    logger.warning("X" * 50)


def main():
    setup_logging()

    test_basic_levels()

    test_extra_fields()

    test_exception_logging()

    test_stack_info()

    test_multithreading()

    test_large_message()

    print("\n=== TEST COMPLETE ===")


if __name__ == "__main__":
    main()
