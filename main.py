import argparse
from confluent_kafka import Producer, Consumer


def produce_message(kafka, topic, message):
    producer = Producer({'bootstrap.servers': kafka})
    producer.produce(topic, value=message)
    producer.flush()
    print(f"Сообщение '{message}' отправлено в топик '{topic}'.")


def consume_messages(kafka, topic):
    consumer = Consumer({
        'bootstrap.servers': kafka,
        'group.id': 'python_consumer_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([topic])
    print(f"Подписан на топик '{topic}'. Ожидание сообщений...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Ошибка: {msg.error()}")
            else:
                print(f"Получено сообщение: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Kafka producer and consumer.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Подкоманда produce
    produce_parser = subparsers.add_parser("produce", help="Send a message to Kafka.")
    produce_parser.add_argument("--message", required=True, help="Message to send.")
    produce_parser.add_argument("--topic", required=True, help="Kafka topic.")
    produce_parser.add_argument("--kafka", required=True, help="Kafka broker address.")

    # Подкоманда consume
    consume_parser = subparsers.add_parser("consume", help="Consume messages from Kafka.")
    consume_parser.add_argument("--topic", required=True, help="Kafka topic.")
    consume_parser.add_argument("--kafka", required=True, help="Kafka broker address.")

    args = parser.parse_args()

    # Выполнение соответствующей подкоманды
    if args.command == "produce":
        produce_message(args.kafka, args.topic, args.message)
    elif args.command == "consume":
        consume_messages(args.kafka, args.topic)
