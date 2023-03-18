# -*- coding:utf-8 -*-
"""
desc: 华为云FunctionGraph访问chatgpt开放API
author: SixSeven
"""
import json

import requests


def handler(event, context):
    return {
        "status": 200,
        "result": chatgpt_api(event)
    }


def chatgpt_api(request_dict: dict):
    try:
        if "headers" not in request_dict:
            return "The key \"headers\" is required."

        if "body" not in request_dict:
            return "The key \"body\" is required."

        headers = request_dict["headers"]
        body = request_dict["body"]
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(body))

        if response.ok:
            return response.text
        else:
            response.raise_for_status()
    except Exception as e:
        return str(e)
