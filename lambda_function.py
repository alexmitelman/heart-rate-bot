import json
import os
from typing import Any

import requests
from aws_lambda_powertools.utilities.typing import LambdaContext

from heart_rate_bot.math import calculate_heart_rate

BOT_TOKEN = os.environ["BOT_TOKEN"]
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text: str, chat_id: str) -> None:
    url = f"{URL}/sendMessage?text={text}&chat_id={chat_id}"
    requests.get(url)


def lambda_handler(
    event: dict[str, Any], context: LambdaContext
) -> dict[str, int]:
    message = json.loads(event["body"])
    chat_id = message["message"]["chat"]["id"]
    text = message["message"]["text"]
    if text == "/start":
        send_message("Hi!", chat_id)
        return {"statusCode": 200}
    params = text.split()
    age = int(params[0])
    reasting_heart_rate = int(params[1])
    result = calculate_heart_rate(age, reasting_heart_rate)
    response_text = (
        f"Your target heart rate range between {result[0]} and {result[1]}"
    )
    send_message(response_text, chat_id)
    return {"statusCode": 200}
