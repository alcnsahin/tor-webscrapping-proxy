# Tor Webscrapping Proxy

These notes are for MacOS

### Install & Configure Tor Service on Mac
```
$ brew install tor
```

Hash your password that you will send a signal to renew IP address
```
$ tor --hash-password <your-password>
16:7C1F66AE245D65236...
```

Create a torcc file under the /opt/homebrew/etc/tor path
```
touch /opt/homebrew/etc/tor/torrc
```

Paste the following configurations to torrc file. Do not forget to paste your hashed password.
```
## The port on which Tor will listen for local connections from Tor
## controller applications, as documented in control-spec.txt.
ControlPort 9051
## If you enable the controlport, be sure to enable one of these
## authentication methods, to prevent attackers from accessing it.
HashedControlPassword <your-hashed-control-password>
#CookieAuthentication 0
```
Stop & start the tor service if it is running already
```
brew services stop tor
brew services start tor
```

Run the python script to see IP changes