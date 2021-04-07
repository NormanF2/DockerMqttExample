# DockerMqttExample
This is a small example of communication between microservices with docker and docker-compose.

---
# **Mqtt Publisher Container Build** #

In the 'mqtt_publisher' folder you will find basic python implementation of an mqtt publisher microservice, with the relative requirements file.

**Build:** Build the image and give it a name, or tag:
```
docker build -t mqtt-publisher .
```

Or, to ignore cached layers, use:
```
docker build --no-cache=true -t mqtt-publisher .
```

WARNING! The trailing dot "." is very important! Don't forget it!

Tag the image with a repo name \<username\>/\<reponame\>:\<version\>

```
docker tag mqtt-publisher <your-username-on-dockerhub>/mqtt-publisher:<x>
```

**Upload:** Push it to the docker-hub
```
docker push <your-username-on-dockerhub>/mqtt-publisher:<x>
```

**docker-compose run:** Then move to the root directory and run:
```
docker-compose up
```


## **Bonus - look inside a running container** ##

Enter into the running application container with:
```
docker exec -it mqtt-publisher bash
```

Then look at the os version:
```
cat /etc/os-release
```
---
# **Connection to Microservices** #
## **Mqtt Subscriber** ##
In the root folder, you will find a basic python implementation of an mqtt subscriber (mqtt_subscriber.py), it is set up to connect to the same topic on which the publisher is writing.

# **Bonus & Exercise: MQTT Authentication** #
You will find the scripts needed to set up an MQTT message handler with authentication in the mosquito-authentication folder.
Now try to edit the python scripts and rebuild the containers to connect to the new MQTT handler.
Don't forget to provide credentials to both the scripts and the MQTT handler.