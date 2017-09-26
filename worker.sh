
# Generate Dadbot config
echo "
[ImDadBot]
class = dadbot.ImDadBot.ImDadBot
client_id = $DADBOT_CLIENT_ID
client_secret = $DADBOT_CLIENT_SECRET
access_token = $DADBOT_ACCESS_TOKEN
" >> config.cfg


# Generate Inspirobot config
echo "
[InspiroBot]
class = inspirobot.InspiroBot.InspiroBot
client_id = $INSPIROBOT_CLIENT_ID
client_secret = $INSPIROBOT_CLIENT_SECRET
access_token = $INSPIROBOT_ACCESS_TOKEN
" >> config.cfg

ananas config.cfg
