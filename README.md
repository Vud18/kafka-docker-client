# Kafka Producer & Consumer

Этот проект предоставляет Python-скрипт для взаимодействия с Apache Kafka. Скрипт позволяет:
- Отправлять сообщения в Kafka (`produce`).
- Подписываться на топик Kafka и читать сообщения (`consume`).

## Функциональность
1. **Отправка сообщения в топик** с помощью команды `produce`.
2. **Чтение сообщений из топика** с помощью команды `consume`.

Проект также включает конфигурацию Docker Compose для развертывания Kafka и Zookeeper.

---

## Требования

- Docker и Docker Compose
- Python 3.11 (для локального запуска)

---

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/Vud18/kafka-docker-client
cd kafka-docker-client
```

### 2. Сборка Docker-образа и запуск

```bash
docker build -t kafka-client:latest .
docker-compose up
```

## Использование

### 1. Отправка сообщения в топик Kafka

Используйте команду produce для отправки сообщения в Kafka:

```bash
docker-compose run --rm app produce --message 'Hello World!' --topic 'hello_topic' --kafka 'kafka:9092'
```

### 2. Чтение сообщений из Kafka

```bash
docker-compose run app consume --topic 'hello_topic' --kafka 'kafka:9092'
```

### 3. Завершение работы
Чтобы остановить сервисы, используйте:
```bash
docker-compose stop
```
