import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from flask_mqtt import Mqtt
from json import loads

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

app.config["MQTT_BROKER_URL"] = "mqtt.24mm2.com"
app.config["MQTT_BROKER_PORT"] = 1883
app.config["MQTT_KEEPALIVE"] = 5  # Set KeepAlive time in seconds
app.config["MQTT_TLS_ENABLED"] = False  # If your server supports TLS, set it True
topic = os.getenv("TOPIC")
# print(topic)
# exit()

mqtt_client = Mqtt(app)
sensor_data = ""


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # print("%s %s" % (msg.topic, msg.payload))
        domino4 = request.form["domino4"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helful assistant that helps with sensor data as provided. You can assist with calculating other values based on the sensor data. You can put the sensor data into context.",
                },
                {"role": "user", "content": generate_prompt(domino4)},
                {"role": "assistant", "content": sensor_data},
            ],
        )
        return redirect(
            url_for("index", result=response["choices"][0]["message"]["content"])
        )

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(domino4):
    pmt = f"Based on this info: {sensor_data} (All in standard expected metric values), can you answer this: {domino4.capitalize()}"
    print(pmt)
    # return pmt
    return domino4.capitalize()


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        mqtt_client.subscribe(topic)  # subscribe topic
    else:
        print("Bad connection. Code:", rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    s = loads(message.payload.decode())
    global sensor_data
    sensor_data = ""
    for key, value in s.items():
        if key not in ["weather","light"]:
            continue
        if isinstance(value, dict):
            for key, value in value.items():
                if type(value) in [int, float]:
                    sensor_data = (sensor_data + f"{key}: {round(value, 2) }\n")
    print(sensor_data)
