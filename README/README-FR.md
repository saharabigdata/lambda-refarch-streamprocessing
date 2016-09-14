
# Architecture de référence sans serveur : Traitement de flux en temps réel

Vous pouvez utiliser [AWS Lambda](http://aws.amazon.com/lambda/) et Amazon Kinesis pour traiter des données de diffusion (streaming) en temps réel pour le suivi d'activité d'application, le traitement de l'ordre de transactions, l'analyses des flux de clics, le nettoyage de données, la génération de métriques, le filtrage de journal, l'indexation, l'analyse des réseaux sociaux, et la télémesure et la mesure de données d'appareil IoT. L'architecture décrite dans ce [diagramme](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) peut être créée avec un template AWS CloudFormation.

[Le template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
exécute les opérations suivantes :

-   Il crée un flux Kinesis

-   Il crée une table DynamoDB appelée &lt;stackname&gt;-EventData

-   Il crée une fonction Lambda 1 (&lt;stackname&gt;-DDBEventProcessor)
    qui reçoit des enregistrements de Kinesis et les écrit dans la
    table DynamoDB

-   Il crée un rôle IAM et une politique qui autorise la fonction Lambda de
    traitement d'événement à lire dans le flux Kinesis et à écrire dans la table DynamoDB

-   Il crée un utilisateur IAM autorisé à placer des événements dans le flux Kinesis avec les
    informations d'identification (credentials) pour l'utilisateur à utiliser dans un client d'API

## Instructions

Étape 1 - Créer une stack AWS CloudFormation avec [le
template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template). Le template AWS CloudFormation automatise entièrement la création, le déploiement et la configuration de tous les composants de l'application.

Étape 2 - Une fois que la stack AWS CloudFormation a été créée avec succès, vous pouvez sélectionner l'onglet Outputs et voir les paramètres AWS nécessaires dans le client Twitter de démonstration dans les étapes ci-dessous.

Étape 3 - Pour exécuter l'exemple d'application, vous devez mettre à jour le code avec AWS et les informations de Twitter. Ouvrez twitter2kinesis.py dans un éditeur de texte.

Étape 4 - Pour accéder à l'API Twitter, vous devez extraire les [jetons d'accès](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Vérifiez qu'ils sont disponibles et entrez les informations dans les paramètres suivants :

Les paramètres de l'API Twitter
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Étape 5 - Entrez les valeurs pour les informations d'identification (credentials) AWS et le nom de flux Amazon Kinesis. Il s'agit des informations issues de l'onglet Outputs du template CloudFormation que vous avez obtenu à l'étape 2 :

Paramètres AWS - issus de l'onglet Outputs du template CloudFormation
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Étape 6 - Pour finir, avant d'exécuter l'exemple de code, vous avez besoin que [Python](https://www.python.org/) soit installé avec les modules Python boto3 et TwitterAPI. Si ces n'avez pas déjà ces module, installez-les à l'aide de [pip](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Test

Étape 1 - Exécutez l'application Python twitter2kinesis.py à partir de la ligne de commande pour commencer à envoyer des tweets dans le flux Kinesis.

```
python twitter2kinesis.py
```

Étape 2 - Sur la console de gestion Amazon DynamoDB, sélectionnez la table appelée &lt;stackname&gt;-EventData et explorez les enregistrements.

## Nettoyage

Pour supprimer toutes les ressources créées, supprimez la stack AWS CloudFormation.
