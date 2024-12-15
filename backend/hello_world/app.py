"""/hello系API"""

from typing import Any
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import CORSConfig
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

# GitHub Actions の動作確認用のコミットのためのコメント

# TODO: ローカル環境用に CORS すべて許可しているので環境変数などで制御できるようにする
cors_config = CORSConfig(allow_origin="*")
app = APIGatewayRestResolver(cors=cors_config)
tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")


@app.get("/hello")
@tracer.capture_method
def hello() -> dict[str, str]:
    """
    hello

    :return: dict[str, str]
    """
    # adding custom metrics
    # See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/
    metrics.add_metric(name="HelloWorldInvocations", unit=MetricUnit.Count, value=1)

    # structured log
    # See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/
    logger.info("Hello world API - HTTP 200")
    return {"message": "hello world"}


# Enrich logging with contextual information from Lambda
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# Adding tracer
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/
@tracer.capture_lambda_handler
# ensures metrics are flushed upon request completion/failure and capturing ColdStart metric
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict[Any, Any], context: LambdaContext) -> dict[str, Any]:
    """
    lambda_handler

    :param event: dict[Any, Any] dict
    :param context: LambdaContext LambdaContext
    :return: dict[str, Any]
    """
    return app.resolve(event, context)
