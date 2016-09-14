
# Serverlose Referenzarchitektur: Stream-Verarbeitung in Echtzeit

Sie können mithilfe von [AWS Lambda](http://aws.amazon.com/lambda/) und Amazon Kinesis Streaming-Daten in Echtzeit verarbeiten, um Anwendungsaktivitäten zu verfolgen, Bestellungstransaktionen abzuwickeln, Clickstream-Analysen durchzuführen, Daten zu bereinigen, Metriken zu generieren, Protokolle zu filtern, Indizierungen durchzuführen, Social-Media-Aktivitäten zu analysieren und die Telemetrie und Messung von IoT-Gerätedaten durchzuführen. Die in diesem [Diagramm](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) beschriebene Architektur kann mithilfe einer AWS CloudFormation-Vorlage erstellt werden.

[Die Vorlage](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
führt folgende Aktionen durch:

-   Erstellen eines Kinesis-Streams

-   Erstellen einer DynamoDB-Tabelle namens "&lt;stackname&gt;-EventData"

-   Erstellen der Lambda-Funktion 1 (&lt;stackname&gt;-DDBEventProcessor),
    die Datensätze von Kinesis empfängt und Datensätze in die
    DynamoDB-Tabelle schreibt

-   Erstellen einer IAM-Rolle und -Richtlinie, um zu gestatten, dass die ereignisverarbeitende
    Lambda-Funktion aus dem Kinesis-Stream liest und in die DynamoDB-Tabelle schreibt

-   Erstellen eines IAM-Benutzers mit der Berechtigung, Ereignisse in den Kinesis-Stream zu schreiben,
    sowie der Anmeldeinformationen, die der Benutzer in einem API-Client verwenden soll

## Anweisungen

Schritt 1 -   Erstellen Sie mithilfe [der
Vorlage](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template) einen AWS CloudFormation-Stapel. Die AWS CloudFormation-Vorlage automatisiert die Erstellung, Bereitstellung und Konfiguration aller Komponenten einer Anwendung zur Gänze.

Schritt 2 – Sobald der AWS CloudFormation-Stapel erfolgreich erstellt wurde, können Sie die AWS-Parameter, die in den folgenden Schritten im Twitter-Democlient benötigt werden, auf der Registerkarte "Outputs" sehen.

Schritt 3 – Um die Beispielanwendung auszuführen, müssen Sie den Code dahingehend ändern, dass er die AWS- und Twitter-Informationen enthält. Öffnen Sie die Anwendung "twitter2kinesis.py" in einem Text-Editor.

Schritt 4 – Um auf die Twitter-API zuzugreifen, benötigen Sie [Zugangs-Token](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Vergewissern Sie sich, dass Sie über die Zugangs-Token verfügen, und geben Sie die Informationen in die folgenden Parameter ein:

Parameter der Twitter-API
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Schritt 5 – Geben Sie die AWS-Anmeldeinformationen und den Amazon Kinesis-Stream-Namen ein. Diese Informationen finden Sie auf der Registerkarte "Outputs" der CloudFormation-Vorlage, die Sie in Schritt 2 erhalten haben:

AWS-Parameter – von der Registerkarte "Outputs" der CloudFormation-Vorlage
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Schritt 6 – Bevor Sie schließlich den Beispielcode ausführen, muss [Python](https://www.python.org/) gemeinsam mit den Python-Modulen "boto3" und "TwitterAPI" installiert werden. Wenn Sie die Module nicht bereits installiert haben, installieren Sie sie mithilfe von [PIP](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Test

Schritt 1 – Führen Sie die Python-Anwendung "twitter2kinesis.py" über die Befehlszeile aus, um mit dem Senden von Tweets in den Kinesis-Stream zu beginnen.

```
python twitter2kinesis.py
```

Schritt 2 – Wählen Sie in der Verwaltungskonsole von Amazon DynamoDB die Tabelle "&lt;stackname&gt;-EventData" aus und sehen Sie sich die Datensätze an.

## Bereinigung

Um alle erstellten Ressourcen zu entfernen, löschen Sie den AWS CloudFormation-Stapel.
