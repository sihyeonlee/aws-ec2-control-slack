# aws-ec2-control-slack

## About
aws-ec2-control-slack은 Slack에서 AmazonWebService EC2 Instance를 제어하기 위해 만든 봇 입니다.

해당 봇을 이용하여 Slack에서 Instance 시작 또는 정지 시키거나, 상태를 불러 올 수 있습니다.

start / stop / status 3가지 명령어를 통해 제어할 수 있습니다.

## System_Info
### Dev_System
- OS : `Windows 10`
- Python Version : `3.7.2`
- Python Package : `venv(requirements.txt 참조)`

### Run_System
- AWS EC2 Instance Type : `t2.micro`
- OS : `Amazon Linux 2018.03`
- Python Version : `3.5.6`
- Python Package : `requirements.txt 참조`

## Source_Tree
- slack_bot.py
    - get_message()
        - RTM api를 사용하여, 계속해서 Slack에서 발생되는 메세지를 불러옵니다.
        - 명령에 대한 결과물을 받으면 메세지로 지정된 채널에 Post 합니다.
    - filter_message(message_json)]
        - str형식의 message_json을 json으로 변형 합니다.
        - 발생되는 여러 메세지 중에, 실질적인 명령어만 인식하여 작동하도록 합니다.
        - 명령이후 발생한 message를 return 시킵니다.
        
- aws_control.py
    - server_start()
        - 지정된 Instance에 start 명령을 전달 후, InstantStatuses와 type return 합니다. [type == sever_start]
    - server_stop()
        - 지정된 Instance에 stop 명령을 전달 후, InstantStatuses와 type을 return 합니다. [type == server_stop]
    - server_status()
        - 지정된 Instance의 Statuses와 type을 return 합니다. [type == server_status]
    - return_status(type, response)
        - 앞서 실행된 sever_*에서 return된 type을 기반으로 response를 파싱합니다.
        - 파싱된 response의 데이터(Instance_Statues_Name)을 return 합니다.

- call_instance.py
    - return_instance()
        - Instance-id를 return 합니다.
    - return_client()
        - Instance 종류 및 지역을 리스트로 return 합니다. [ex) ['ec2', 'us-ease-1']]

- call_token.py
    - return_token(call_name)
        - call_name에 해당하는 token 값을 return 합니다.
        
## Dev-Log
- 2019-01-12 중대한 오류[#1 #2 #3] 수정 및 예외 처리 추가
- 2019-01-11 v0.1(start / stop / status) 구현
- 2019-01-10 개발 시작

## Refer
- [Boto3 API](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Slack API](https://api.slack.com/methods)
- [Slack Bot Python Example - @Corikachu](https://corikachu.github.io/articles/python/python-slack-bot-slacker)
