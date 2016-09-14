
# Architettura di riferimento senza server: elaborazione dei flussi in tempo reale

È possibile utilizzare [AWS Lambda](http://aws.amazon.com/lambda/) e Amazon Kinesis per elaborare i flussi di dati in tempo reale per monitorare l'attività dell'applicazione, elaborare l'ordine delle transazioni, analizzare il flusso dei clic, eliminare i dati, generare parametri, filtrare i registri, indicizzare, analizzare i social media ed eseguire misurazione e telemetria dei dati dei dispositivi di IoT. Questa architettura, descritta in questo [diagramma](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf), può essere creata con un modello di AWS CloudFormation.

[Il modello](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
svolge le operazioni seguenti:

-   Creazione di un flusso Kinesis

-   Creazione di una tabella di DynamoDB nominata &lt;stackname&gt;-EventData

-   Creazione della funzione 1 di Lambda (&lt;stackname&gt;-DDBEventProcessor)
    che riceve i record da Kinesis e scrive i record nella
    tabella di DynamoDB

-   Creazione di un ruolo e di una policy IAM per consentire alla funzione di Lambda di elaborazione degli eventi
    di leggere dal flusso Kinesis e di scrivere nella tabella di DynamoDB

-   Creazione di un utente IAM con autorizzazione a inserire eventi nel flusso Kinesis
    e credenziali che l'utente può utilizzare in un client API

## Istruzioni

Passaggio 1: creare uno stack di AWS CloudFormation con [il
modello](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template). Il modello di AWS CloudFormation automatizza completamente la creazione, la distribuzione e la configurazione di tutti i componenti dell'applicazione.

Passaggio 2: una volta creato lo stack di AWS CloudFormation, è possibile selezionare la scheda Outputs e visualizzare i parametri di AWS necessari nel client Twitter dimostrativo nei passaggi seguenti.

Passaggio 3: per eseguire l'applicazione esempio, è necessario aggiornare il codice con le informazioni di AWS e Twitter. Aprire twitter2kinesis.py in un editor di testo.

Passaggio 4: per accedere all'API di Twitter, è necessario disporre dei [token di accesso](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Accertarsi di esserne in possesso e inserire le informazioni nei parametri seguenti:

Parametri dell'API di Twitter
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Passaggio 5: inserire i valori per le credenziali di AWS e il nome del flusso di Amazon Kinesis. Queste sono le informazioni della scheda Outputs del modello di CloudFormation ottenute nel passaggio 2:

Parametri di AWS: dalla scheda Outputs del modello di CloudFormation
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Passaggio 6: infine, prima di eseguire il codice esempio, è necessario installare [Python](https://www.python.org/) con i moduli Python boto3 e TwitterAPI. Se non si dispone già dei moduli, installarli utilizzando [pip](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Test

Passaggio 1: eseguire l'applicazione Python twitter2kinesis.py dalla riga di comando per iniziare a inviare Tweet nel flusso Kinesis.

```
python twitter2kinesis.py
```

Passaggio 2: nella console di gestione di Amazon DynamoDB, selezionare la tabella nominata &lt;stackname&gt;-EventData ed esaminare i record.

## Eliminazione

Per eliminare tutte le risorse create, eliminare lo stack di AWS CloudFormation.
