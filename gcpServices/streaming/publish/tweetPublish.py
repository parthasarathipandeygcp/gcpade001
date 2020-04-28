from google.cloud import pubsub_v1
import json 

project='upendar'
TOPIC='twitter_topic'
# Configure the connection
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project, TOPIC)

# Function to write data to
def write_to_pubsub(data):
    try:
        if data["lang"] == "en":
          
            # publish to the topic, don't forget to encode everything at utf8!
            publisher.publish(topic_path, data=json.dumps({
                "text": data["text"],
                "user_id": data["user_id"],
                "id": data["id"],
                "posted_at": datetime.datetime.fromtimestamp(data["created_at"]).strftime('%Y-%m-%d %H:%M:%S')
            }).encode("utf-8"), tweet_id=str(data["id"]).encode("utf-8"))
            
    except Exception as e:
        print(e)
        raise

def  write_to_topic(data):
    publisher.publish(topic_path,json.dumps(data).encode('utf-8'))