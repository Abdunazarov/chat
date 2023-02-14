# About
A simple asynchronously working chat application built with django channels by enabling WebSockets.


## Requirements
Using the pip package manager to install django-channels by running the following command:
```bash
pip install django-channels
```

## Walkthrough
Register a user in order to start using the app. A user has to add contacts (add existing users to contact list) in `Add contacts` section. You can search for the user you are looking or choose any random user shown below.
You can start conversation right after clicking to a user, which are automatically added to your contact list and can be found under `You contacts`.


### For Linux users
In order to get redis working on the project you should have redis-server running first, in order to install redis-server run:
```bash
sudo apt-get install redis-server
```
Afterwards, run:
```bash
sudo service redis-server start
```
Now, since the redis-server is running you shouldn't get any errors
