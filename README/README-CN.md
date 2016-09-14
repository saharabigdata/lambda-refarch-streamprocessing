
# 无服务器参考架构：实时流处理

您可以使用 [AWS Lambda](http://aws.amazon.com/lambda/) 和 Amazon Kinesis 处理应用程序活动跟踪、交易订单处理、点击流分析、数据清理、指标生成、日志筛选、索引、社交媒体分析以及 IoT 设备数据遥测和计量的实时流数据。可以使用 AWS CloudFormation 模板创建在此 [示意图](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) 中介绍的架构。

使用 [模板](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
可执行以下操作：

-   创建 Kinesis 流

-   创建名为 &lt;stackname&gt;-EventData 的 DynamoDB 表

-   创建 Lambda 函数 1 (&lt;stackname&gt;-DDBEventProcessor)，
    以便从 Kinesis 接收记录并将记录写入到
    DynamoDB 表

-   创建一个 IAM 角色和策略，以允许事件处理 Lambda
    函数从 Kinesis 流中读取并写入到 DynamoDB 表

-   创建一个 IAM 用户，该用户有权将 Kinesis 流中的事件
    与该用户的凭证放在一起，以便在 API 客户端中使用

## 说明

步骤 1 - 使用 [
模板](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template) 创建一个 AWS CloudFormation 堆栈。AWS CloudFormation 模板会完全自动执行应用程序的所有组件的构建、部署和配置操作。

步骤 2 - 一旦成功创建 AWS CloudFormation 堆栈，您就可以选择“输出”选项卡，然后查看在后续步骤的演示 Twitter 客户端中所需的 AWS 参数。

步骤 3 - 运行您需要用来通过 AWS 和 Twitter 信息更新代码的示例应用程序。在文本编辑器中打开 twitter2kinesis.py。

步骤 4 - 要访问 Twitter API，您需要获取 [访问令牌](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)。确保您可以使用这些令牌，并在下面的参数中输入信息：

Twitter API 参数
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

步骤 5 - 输入 AWS 凭证和 Amazon Kinesis 流名称的值。这是您在步骤 2 中获得的 CloudFormation 模板“Outputs”选项卡中提供的信息：

AWS 参数 - 来自 CloudFormation 模板的“Outputs”选项卡
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

步骤 6 - 最后，在运行示例代码之前，您需要安装 [Python](https://www.python.org/) 以及 Python 模块 boto3 和 TwitterAPI。如果您还没有这些模块，请使用 [pip](http://pip.readthedocs.org/en/stable/installing/) 来安装：

```
pip install boto3 TwitterAPI
```

## 测试

步骤 1 - 从命令行运行 twitter2kinesis.py Python 应用程序，开始将推文发送到 Kinesis 流。

```
python twitter2kinesis.py
```

步骤 2 - 在 Amazon DynamoDB 管理控制台中，选择名为 &lt;stackname&gt;-EventData 的表并浏览记录。

## 清理

要删除所有创建的资源，请删除 AWS CloudFormation 堆栈。
