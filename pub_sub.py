from google.cloud import pubsub_v1

project_id = 'ageless-granite-273208'
topic_id = 'mils_pubsub_2'
subscription_name = ''

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print("Topic created: {}".format(topic))

# subscriber = pubsub_v1.SubscriberClient()
# subscription_path = subscriber.subscription_path(project, subscription_name)