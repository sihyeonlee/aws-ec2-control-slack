import boto3
from call_instance import *


client = boto3.client(return_client()[0], return_client()[1])


def return_status(type, response):
    instance_status = None

    if type == 'server_start':
        if response == 0:
            return 'Please wait stopping process'

        instance_status = response['StartingInstances'][0]['CurrentState']['Name']

    elif type == 'server_stop':
        instance_status = response['StoppingInstances'][0]['CurrentState']['Name']
    elif type == 'server_status':
        instance_status = response['Reservations'][0]['Instances'][0]['State']['Name']
    else:
        pass

    return instance_status


def server_start():
    n_status = server_status()

    if n_status == 'stopping':
        response = 0

        return return_status('server_start', response)

    response = client.start_instances(InstanceIds=[return_instance()])

    return return_status('server_start', response)


def server_stop():
    response = client.stop_instances(InstanceIds=[return_instance()])
    return return_status('server_stop', response)


def server_status():
    response = client.describe_instances(
        Filters=[],
        InstanceIds=[return_instance()]
    )

    return return_status('server_status', response)
