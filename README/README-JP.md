
# サーバーレスリファレンスアーキテクチャ: リアルタイムのストリーム処理

[AWS Lambda](http://aws.amazon.com/lambda/) および Amazon Kinesis を使用して、アプリケーションのアクティビティ追跡、トランザクション注文処理、クリックストリーム分析、データクレンジング、メトリックス生成、ログフィルタリング、インデックス作成、ソーシャルメディア分析、および IoT デバイスデータテレメトリと測定のリアルタイムストリーミングデータを処理できます。この [図](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) に示すアーキテクチャは、AWS CloudFormation テンプレートを使用して作成できます。

[テンプレート](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
 は以下を実行します。

-   Kinesis Stream を作成する

-   &lt;stackname&gt;-EventData という名前の DynamoDB テーブルを作成する

-   Lambda 関数 1 (&lt;stackname&gt;-DDBEventProcessor) を作成する
    (この関数は Kinesis からレコードを受け取り、レコードを 
    DynamoDB テーブルに書き込みます)

-   IAM ロールとポリシーを作成し、イベントを処理する Lambda 
    関数による Kinesis Stream からの読み取りと DynamoDB テーブルへの書き込みを許可する

-   ユーザーが API クライアントで使用する認証情報とともに、イベントを Kinesis ストリームに
    配置するアクセス権限を持つ IAM ユーザーを作成する

## 手順

ステップ 1 - AWS CloudFormation スタックを [
テンプレート](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template) で作成します。AWS CloudFormation テンプレートが、アプリケーションのすべてのコンポーネントの構築、デプロイ、および設定を完全に自動化します。

ステップ 2 - AWS CloudFormation スタックが正常に作成されたら、[Outputs] タブを選択し、次のステップのデモ Twitter クライアントで必要な AWS パラメーターを表示できます。

ステップ 3 - サンプルアプリケーションを実行するには、AWS および Twitter 情報でコードを更新する必要があります。テキストエディターで twitter2kinesis.py を開きます。

ステップ 4 - Twitter API にアクセスするには、[アクセストークン](https://dev.twitter.com/oauth/overview/application-owner-access-tokens) を取得する必要があります。これらが利用可能であることを確認し、次のパラメーターに情報を入力します。

Twitter API のパラメーター
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

ステップ 5 - AWS 認証情報および Amazon Kinesis ストリーム名に値を入力します。これは、ステップ 2 で取得した CloudFormation テンプレートの [Outputs] タブからの情報です。

AWS のパラメーター - CloudFormation テンプレートの [Outputs] タブから
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

ステップ 6 - 最後に、サンプルコードを実行する前に、Python モジュール boto3 と TwitterAPI とともに [Python](https://www.python.org/) がインストールされている必要があります。すでにモジュールがない場合は、[pip](http://pip.readthedocs.org/en/stable/installing/) を使用してインストールします。

```
pip install boto3 TwitterAPI
```

## テスト

ステップ 1 - コマンドラインから twitter2kinesis.py Python アプリケーションを実行し、Kinesis ストリームへのツィートの送信を開始します。

```
python twitter2kinesis.py
```

ステップ 2 - Amazon DynamoDB 管理コンソールで、&lt;stackname&gt;-EventData というテーブルを選択し、レコードを調べます。

## クリーンアップ

作成されたすべてのリソースを削除するには、AWS CloudFormation スタックを削除します。
