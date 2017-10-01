# mastobots

Currently the code for @ImDad@botsin.space and @InspiroBot@botsin.space


# Running locally

To run the bots locally you need: 

- docker 
- the internet
- a mastodon application's client id, client secret, and access token 

There are two ways to pass in your client ids, secrets, and access tokens. 


### Way no.1: create an .env.local

Your specific bot's client keys will be sourced automatically from a `.env.local` file in the working directory, if it exists. Don't worry, .env.local is gitignored, so you won't accidentally commit your keys.

here's an example `.env.local` file: 

```
INSPIROBOT_CLIENT_ID=yourInspirobotClientKey
INSPIROBOT_CLIENT_SECRET=yourInspirobotClientSecret
INSPIROBOT_ACCESS_TOKEN=yourInspirobotAccessToken
DADBOT_CLIENT_ID=yourDadbotClientId
DADBOT_CLIENT_SECRET=yourDadbotClientSecret
DADBOT_ACCESS_TOKEN=yourDadbotAccessToken
```

To run the bots with the config, simply: 

```sh
docker build -t mastobots .
docker run docker run -it mastobots
```

The .env.local will be copied into the image when `docker build` runs, and will be applied during startup.

### Way no.2: pass secrets directly into the docker container

```sh
docker build -t mastobots .
docker run docker run \
  -e INSPIROBOT_CLIENT_ID=yourInspirobotClientKey \
  -e INSPIROBOT_CLIENT_SECRET=yourInspirobotClientSecret \
  -e INSPIROBOT_ACCESS_TOKEN=yourInspirobotAccessToken \
  -e DADBOT_CLIENT_ID=yourDadbotClientId \
  -e DADBOT_CLIENT_SECRET=yourDadbotClientSecret \
  -e DADBOT_ACCESS_TOKEN=yourDadbotAccessToken \
  -it mastobots
```
