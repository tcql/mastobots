# mastobots

Currently the code for [@ImDad@botsin.space](https://botsin.space/@ImDad) and [@InspiroBot@botsin.space](https://botsin.space/@InspiroBot). Both bots are built using https://github.com/Chronister/ananas


# Running locally

To run the bots locally you need: 

- docker 
- the internet
- a mastodon application's client id, client secret, and access token 

<details>
  <summary><strong>Click here if you don't know how to get client ids, secrets, and access tokens</strong></summary>

Bot accounts start out as regular old Mastodon accounts. Be careful what instance you create a bot account on though; many instances don't allow bots. I'd recommend  using https://botsin.space, since it's intended specifically for hosting bots.

_Don't just create an application on your normal mastodon account; the bots will start posting as you when you run them!_ For development purposes, it's probably best to create a single testing/throwaway account. 

1. Register the account, just like you normally would
2. Once you're logged in, click **Edit Profile**
3. In the settings side-menu, click **Development**
4. Click **New Application**. Anything that externally interacts with mastodon is an "Application", including Bots.
5. Fill out the application form:
   - Give your bot application a name. I would just use the same name as your bot. For our example, I'd use _ReplyBot_. 
   - Website and Redirect URI aren't important for us
   - Ensure you've got the scopes enabled. You should only need _read_ and _write_, but there's no harm in having _follow_ enabled too
6. Make note of the `client key`, `client secret` and `access token` that are shown once you save the application, you'll need those soon!
</details>
<br />


There are two ways to pass in your client ids, secrets, and access tokens. 


## Way no.1: create an .env.local

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

## Way no.2: pass secrets directly into the docker container

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
