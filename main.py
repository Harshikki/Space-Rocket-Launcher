from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName
broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/iot'

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client
#Define the first page of the web application
@app.route('/')
def index():
	return render_template('index.html')
#Define the button page of the web application
@app.route('/main', methods=['POST'])
def main():
	return render_template('main.html')
#Define the Release Orbital Arm button and connect with MQTT server
@app.route('/1', methods=['POST'])
def release():
	release_test()
	return render_template('1.html')
def release_test():
	client = connect_mqtt()
	client.loop_start()
	send_release_data(client)
def send_release_data(client):
	message = '1'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')
#Define the Main Engine Test button and connect with MQTT server
@app.route('/2', methods=['POST'])
def engine():
	engine_test()
	return render_template('2.html')
def engine_test():
	client = connect_mqtt()
	client.loop_start()
	send_engine_data(client)
def send_engine_data(client):
	message = '2'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')
#Define the Activate Hydrogen button and connect with MQTT server
@app.route('/3', methods=['POST'])
def activate():
	activate_hydrogen()
	return render_template('3.html')
def activate_hydrogen():
	client = connect_mqtt()
	client.loop_start()
	send_hydrogen_data(client)
def send_hydrogen_data(client):
	message = '3'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')
#Define the Main Engine Ignite button and connect with MQTT server
@app.route('/4', methods=['POST'])
def ignite():
	engine_ignite()
	return render_template('4.html')
def engine_ignite():
	client = connect_mqtt()
	client.loop_start()
	send_ignite_data(client)
def send_ignite_data(client):
	message = '4'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')
#Define the Hydrogen Vent Arm button and connect with MQTT server
@app.route('/5', methods=['POST'])
def vent():
	vent_arm()
	return render_template('5.html')
def vent_arm():
	client = connect_mqtt()
	client.loop_start()
	send_vent_data(client)
def send_vent_data(client):
	message = '5'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')
#Define the Ignite both SRB's button and connect with MQTT server
@app.route('/6', methods=['POST'])
def srb():
	ignite_srb()
	return render_template('6.html')
def ignite_srb():
	client = connect_mqtt()
	client.loop_start()
	send_srb_data(client)
def send_srb_data(client):
	message = '6'
	result = client.publish(topic, message)
	status = result[0]
	if status == 0:
		print('Send `{message}` to topic `{topic}`')

if __name__ == "__main__":
    app.run(port=5001)




