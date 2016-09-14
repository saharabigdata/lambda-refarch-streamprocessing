
# Эталонная бессерверная архитектура: обработка потока в реальном времени

С помощью [AWS Lambda](http://aws.amazon.com/lambda/) и Amazon Kinesis вы можете в реальном времени обрабатывать потоковые данные для отслеживания работы приложения, обработки заказов, анализа посещаемости, очистки данных, создания метрик, фильтрации журналов, индексации, анализа социальных сетей и обработки данных телеметрии устройств IoT. Архитектуру, описанную на этой [схеме](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf), можно создать с помощью шаблона AWS CloudFormation.

[Шаблон](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
выполняет следующие действия:

- создает поток Kinesis;

- создает таблицу DynamoDB с именем &lt;stackname&gt;-EventData;

- создает функцию Lambda 1 (&lt;stackname&gt;-DDBEventProcessor),
    которая получает записи из Kinesis и размещает их в
    таблице DynamoDB;

- создает роль и политику IAM, чтобы позволить функции Lambda, обрабатывающей события,
    читать данные из потока Kinesis и записывать их в таблицу DynamoDB;

- создает пользователя IAM с разрешением для добавления событий в поток Kinesis
    вместе с данными для доступа, которые будут использоваться в клиенте API.

## Инструкции

Шаг 1. Создайте стек AWS CloudFormation с помощью
[шаблона](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template). Этот шаблон AWS CloudFormation полностью автоматизирует создание, развертывание и настройку всех компонентов приложения.

Шаг 2. После успешного создания стека AWS CloudFormation вы можете открыть вкладку «Outputs» и просмотреть параметры AWS, необходимые для примера клиента Twitter, описанного далее.

Шаг 3. Для запуска примера приложения вам необходимо добавить в код данные AWS и Twitter. Откройте twitter2kinesis.py в текстовом редакторе.

Шаг 4. Для доступа к Twitter API вам потребуются [маркеры доступа](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Убедитесь, что они у вас есть, и укажите значения для следующих параметров.

Параметры Twitter API
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Шаг 5. Введите данные для доступа AWS и имя потока Amazon Kinesis. Это сведения с вкладки «Outputs» шаблона CloudFormation, которую вы открывали на шаге 2.

Параметры AWS – это сведения с вкладки «Outputs» шаблона CloudFormation.
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Шаг 6. Наконец, перед запуском примера кода необходимо установить [Python](https://www.python.org/) с модулями boto3 и TwitterAPI. Если у вас нет этих модулей, установите их с помощью [pip](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Тестирование

Шаг 1. Запустите Python-приложение twitter2kinesis.py из командной строки, чтобы начать отправлять твиты в поток Kinesis.

```
python twitter2kinesis.py
```

Шаг 2. В консоли управления Amazon DynamoDB выберите таблицу &lt;stackname&gt;-EventData и просмотрите записи.

## Очистка

Чтобы удалить все созданные ресурсы, удалите стек AWS CloudFormation.
