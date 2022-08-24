##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel, Field
from typing import List
from unskript.connectors.aws import aws_get_paginator
import pprint
from beartype import beartype

class InputSchema(BaseModel):
    tag_key: str = Field(
        title='Tag Key',
        description='The key of the tag.')
    tag_value: str = Field(
        title='Tag Value',
        description='The value of the key.')
    region: str = Field(
        title='Region',
        description='AWS Region.')

@beartype
def aws_filter_ec2_by_tags_printer(output):
    if output is None:
        return
    pprint.pprint({"Instances": output})


@beartype
def aws_filter_ec2_by_tags(handle, tag_key: str, tag_value: str, region: str) -> List:
    """aws_filter_ec2_by_tags Returns an array of instances matching tags.

        :type nbParamsObj: object
        :param nbParamsObj: Object containing global params for the notebook.

        :type credentialsDict: dict
        :param credentialsDict: Dictionary of credentials info.

        :type inputParamsJson: string
        :param inputParamsJson: Json string of the input params.

        :rtype: Array of instances matching tags.
    """
    # Input param validation.

    ec2Client = handle.client('ec2', region_name=region)
    res = aws_get_paginator(ec2Client, "describe_instances", "Reservations",
                            Filters=[{'Name': 'tag:' + tag_key, 'Values': [tag_value]}])

    result = []
    for reservation in res:
        for instance in reservation['Instances']:
            result.append(instance['InstanceId'])
    return result
