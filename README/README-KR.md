
# 서버 없는 레퍼런스 아키텍처: 실시간 스트림 처리

[AWS Lambda](http://aws.amazon.com/lambda/)와 Amazon Kinesis를 사용하여 애플리케이션 활동 추적, 트랜잭션 요청 처리, 클릭 스트림 분석, 데이터 정리, 측정치 생성, 로그 필터링, 인덱싱, 소셜 미디어 분석 및 IoT 장치 데이터 측정 및 계측을 위해 실시간 스트리밍 데이터를 처리할 수 있습니다. 이 [diagram](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf)에 설명된 아키텍처는 AWS CloudFormation 템플릿을 사용하여 만들 수 있습니다.

[The template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)으로
다음을 수행할 수 있습니다.

-   Kinesis 스트림 생성

-   이름이 &lt;stackname&gt;-EventData인 DynamoDB 테이블 생성

-   Lambda 함수 1(&lt;stackname&gt;-DDBEventProcessor) 생성
    이 함수는 Kinesis로부터 레코드를 수신하여 레코드를
    DynamoDB 테이블에 기록합니다.

-   이벤트 처리 Lambda 함수가 Kinesis 스트림으로부터 읽고
    DynamoDB 테이블에 쓸 수 있도록 허용하는 IAM 역할 및 정책 생성

-   Kinesis 스트림에 이벤트를 추가할 수 있는 권한과
    사용자가 API 클라이언트에서 사용할 수 있는 자격 증명이 있는 IAM 사용자 생성

## 지침

1단계 - [the
template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template)으로 AWS CloudFormation 스택을 만듭니다. AWS CloudFormation 템플릿은 모든 애플리케이션 구성 요소의 구축, 배포 및 구성을 완전 자동화합니다.

2단계 - AWS CloudFormation 스택이 생성되면 Outputs 탭을 선택하여 아래 단계의 데모 Twitter 클라이언트에 필요한 AWS 파라미터를 볼 수 있습니다.

3단계 - 예제 애플리케이션을 실행하려면 AWS 및 Twitter 정보로 코드를 업데이트해야 합니다. 텍스트 편집기에서 twitter2kinesis.py를 엽니다.

4단계 - Twitter API에 액세스하려면 [access tokens](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)이 있어야 합니다. 해당 토큰을 사용할 수 있는지 확인하고 다음 파라미터에 정보를 입력합니다.

Twitter API 파라미터
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

5단계 - AWS 자격 증명과 Amazon Kinesis 스트림 이름의 값을 입력합니다. 이 정보는 2단계에서 얻은 CloudFormation 템플릿의 Outputs 탭에 있는 정보입니다.

AWS 파라미터 - CloudFormation 템플릿의 Outputs 탭에 있음
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

6단계 - 마지막으로, 예제 코드를 실행하기 전에 [Python](https://www.python.org/)과 Python의 boto3 및 TwitterAPI 모듈이 설치되어 있어야 합니다. 아직 모듈이 없는 경우 [pip](http://pip.readthedocs.org/en/stable/installing/)을 사용하여 설치합니다.

```
pip install boto3 TwitterAPI
```

## 테스트

1단계 - 명령줄에서 twitter2kinesis.py Python 애플리케이션을 실행하여 Kinesis 스트림에 트윗을 전송합니다.

```
python twitter2kinesis.py
```

2단계 - Amazon DynamoDB 관리 콘솔에서 이름이 &lt;stackname&gt;-EventData인 테이블을 선택하고 레코드를 살펴봅니다.

## 정리

생성된 모든 리소스를 제거하려면 AWS CloudFormation 스택을 삭제합니다.
