# encoding: utf-8
"""
desc: 简易路由转换器
author: SixSeven
"""

from flask import Flask, request
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkfunctiongraph.v2 import FunctionGraphClient, InvokeFunctionRequest, InvokeFunctionResponse
from huaweicloudsdkfunctiongraph.v2.region.functiongraph_region import FunctionGraphRegion

from config import FunctionGraphConfig

app = Flask(__name__)


@app.route("/v1/chat/completions", methods=["POST"])
def chatgpt():
    headers = dict(request.headers)
    header_keys = ["Content-Type", "Authorization"]
    new_headers = dict([(key, headers.get(key, "")) for key in header_keys])

    fgs_body = {
        "headers": new_headers,
        "body": request.get_json()
    }
    return fgs(fgs_body)


def fgs(body):
    credentials = BasicCredentials(FunctionGraphConfig.ak, FunctionGraphConfig.sk)
    client = FunctionGraphClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(FunctionGraphRegion.value_of(FunctionGraphConfig.region)) \
        .build()

    try:
        func_request = InvokeFunctionRequest()
        func_request.function_urn = FunctionGraphConfig.function_urn
        func_request.body = body
        response: InvokeFunctionResponse = client.invoke_function(func_request)
        return response.result, response.status
    except Exception as e:
        return str(e), 500


def start_nginx():
    app.run("0.0.0.0", 5235, debug=True)


if __name__ == "__main__":
    start_nginx()
