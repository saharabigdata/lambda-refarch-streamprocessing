
# Arquitectura de referencia sin servidor: Procesamiento de streaming en tiempo real

Puede usar [AWS Lambda](http://aws.amazon.com/lambda/) y Amazon Kinesis para procesar el streaming de datos en tiempo real para el seguimiento de actividades de una aplicación, procesamiento de pedidos de transacciones, análisis de secuencias de clics, limpieza de datos, generación de métricas, filtrado de logs, indexación, análisis de redes sociales, y telemetría y medición de datos de dispositivos IoT. La arquitectura descrita en este [diagrama](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) se puede crear con una plantilla de AWS CloudFormation.

[La plantilla](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
hace lo siguiente:

-   Crea un flujo de Kinesis

-   Crea una tabla de DynamoDB llamada &lt;stackname&gt;-EventData

-   Crea la función Lambda 1 (&lt;stackname&gt;-DDBEventProcessor)
    que recibe registros de Kinesis y escribe registros en la
    tabla de DynamoDB

-   Crea un rol y una política de IAM para permitir que la función Lambda de procesamiento
    de eventos lea el flujo de Kinesis y escriba en la tabla de DynamoDB

-   Crea un usuario de IAM con permiso para colocar eventos en el flujo de Kinesis
    junto con credenciales para el usuario para su uso en un cliente de la API

## Instrucciones

Paso 1: Cree una pila de AWS CloudFormation con [la
plantilla](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template). La plantilla de AWS CloudFormation automatiza por completo la creación, implementación y configuración de todos los componentes de la aplicación.

Paso 2: Una vez creada correctamente la pila de AWS CloudFormation, puede seleccionar la pestaña Outputs y ver los parámetros de AWS necesarios en el cliente de Twitter de demostración en los pasos que se incluyen a continuación.

Paso 3: Para ejecutar la aplicación de ejemplo necesita actualizar el código con información de AWS y Twitter. Abra twitter2kinesis.py en un editor de texto.

Paso 4: Para acceder a la API de Twitter necesita obtener [tokens de acceso](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Asegúrese de que dispone de estos tokens e introduzca la información en los siguientes parámetros:

Los parámetros de la API de Twitter
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Paso 5: Introduzca los valores de las credenciales de AWS y el nombre de flujo de Amazon Kinesis. Esta es la información de la pestaña Outputs de la plantilla de CloudFormation que obtuvo en el paso 2:

Parámetros de AWS: de la pestaña Outputs de la plantilla de CloudFormation
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Paso 6: Por último, antes de ejecutar el código de ejemplo, necesita que [Python](https://www.python.org/) esté instalado junto con los módulos de Python boto3 y TwitterAPI. Si aún no tiene los módulos, instálelos mediante [pip](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Prueba

Paso 1: Ejecute la aplicación Python twitter2kinesis.py desde la línea de comando para empezar a enviar tweets al flujo de Kinesis.

```
python twitter2kinesis.py
```

Paso 2: En la consola de administración de Amazon DynamoDB, seleccione la tabla llamada &lt;stackname&gt;-EventData y examine los recursos.

## Borrado

Para eliminar todos los recursos creados, borre la pila de AWS CloudFormation.
