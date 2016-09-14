
# 無伺服器參考架構：即時串流處理

您可以使用 [AWS Lambda](http://aws.amazon.com/lambda/) 與 Amazon Kinesis 處理即時串流資料以進行應用程式活動追蹤、交易訂單處理、點擊流分析、資料淨化、指標產生、日誌過濾、建立索引、社交媒體分析，以及 IoT 裝置資料遙測與計量。使用 AWS CloudFormation 範本可建立此 [示意圖](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) 所描述的架構。

[範本](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
執行以下項目：

-   建立 Kinesis Stream

-   建立名為 &lt;stackname&gt;-EventData 的 DynamoDB 資料表

-   建立 Lambda Function 1 (&lt;stackname&gt;-DDBEventProcessor)
    可接收來自 Kinesis 的紀錄並將記錄寫入至
    DynamoDB 資料表

-   建立 IAM 角色與政策以允許事件處理 Lambda
    功能讀取 Kinesis Stream 以及寫入至 DynamoDB 資料表

-   建立具備可將事件放入 Kinesis stream 的權限的 IAM 使用者
    以及使用者的登入資料以便在 API 用戶端中使用

## 說明

步驟 1 - 使用 [
範本](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template) 建立 AWS CloudFormation 堆疊。AWS CloudFormation 範本會完全自動建立、部署及設定應用程式的所有元件。

步驟 2 - 一旦成功建立 AWS CloudFormation 堆疊之後，您可以選擇 Outputs 索引標籤並查看以下步驟中的示範 Twitter 用戶端所需要的 AWS 參數。

步驟 3 - 若要執行範例應用程式，您必須更新 AWS 的程式碼及 Twitter 資訊。在文字編輯器中開啟 twitter2kinesis.py。

步驟 4 - 若要存取 Twitter API，您必須取得 [存取符記](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)。請確定您已備妥上述資料，然後在以下參數中輸入資訊：

Twitter API 參數
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

步驟 5 - 輸入 AWS 登入資料與 Amazon Kinesis stream 名稱的值。這些資訊來自您在步驟 2 取得的 CloudFormation 範本的 Outputs 索引標籤。

AWS 參數 - 來自 CloudFormation 範本的 Outputs 索引標籤
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

步驟 6 - 最後，在執行範本程式碼之前，您必須安裝 [Python](https://www.python.org/) 以及 Python 模組 boto3 與 TwitterAPI。如果您還沒有這些模組，請使用 [pip](http://pip.readthedocs.org/en/stable/installing/) 進行安裝：

```
pip install boto3 TwitterAPI
```

## 測試

步驟 1 - 從命令列執行 twitter2kinesis.py Python 應用程式以開始將推文傳送至 Kinesis stream。

```
python twitter2kinesis.py
```

步驟 2 - 在 Amazon DynamoDB 管理主控台中選擇名為 &lt;stackname&gt;-EventData 的資料表，然後探索其紀錄。

## 清除

若要移除所有已建立的資源，請刪除 AWS CloudFormation 堆疊。
