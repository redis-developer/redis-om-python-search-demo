# Redis OM Python Search Demo

This repository contains a basic demonstration of the object modeling and search capabilities of the [Redis OM Python client](https://github.com/redis/redis-om-python) for [Redis](https://redis.io).  Watch a video of me presenting this demo on [YouTube](https://youtu.be/DFNKmbGKa5w?t=410) at a Redis Montly Live event (sign up for these [here](https://meetups.redis.com).

The demo requires you to have [RediSearch](https://oss.redis.com/redisearch/) 2.2 or higher installed on your Redis server.  The easiest way to get this in order to try out the code here is to use the supplied `docker-compose.yml` file, so you'll want to have [Docker Desktop](https://www.docker.com/get-started) installed.  

You'll also require a reasonably up to date version of Python 3 - I think you need 3.8 or better.  I've tested this on the following version of Python on macOS Big Sur 11.6.1:

```bash
$ python3 --version
Python 3.9.5
```

## Overview

We'll take a look at how to model domain objects in Python using Redis OM.  You'll find the model in `adoptable.py`.  These objects can then be persisted to [Redis Hashes](https://www.youtube.com/watch?v=-KdITaRkQ-U) by calling `save()` on them.  By defining which fields should be indexed and how to index them, we can tell Redis OM to build and maintain a RediSearch index for us. This allows us to leverage the fluent querying API to retrieve objects matching multiple search criteria.

In this example, we'll use a small data set of dogs and cats that are available for adoption at an animal shelter.  This data is in the file `animal_data.csv`.

## Setup

To try the code out, you'll want to clone the repo, create a Python virtual environment, install dependencies and start Redis using Docker:

```bash
$ git clone https://github.com/simonprickett/redis-om-python-search-demo.git
$ cd redis-om-python-search-demo
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

Then, in a second terminal:

```bash
$ cd redis-om-python-search-demo
$ docker-compose up
```

## Loading the Data into Redis and Indexing it

Now it's time to load the data into Redis and setup the RediSearch index:

```bash
$ python load_adoptables.py
```

You should see output showing the name and Redis key of each animal loaded from `animal_data.csv`.

## Running the Code

To query the data, run `query_adoptables.py`:

```bash
$ python query_adoptables.py
```

You can change which query runs by editing the final four lines of `query_adoptables.py` to add/remove comments as needed.

The example queries are as follows:

* `find_by_name`: Find all animals whose `name` field is `Luna`
* `find_male_dogs`: Find all animals where `sex` is `m` and `species` is `dog`
* `find_dogs_in_age_range`: Find all animals where `species` is `dog` and `age` is 9 or 10
* `find_cats_good_with_children`: Final all animals where `species` is `cat` and `children` (good with children) is `y` and where the free text `description` field does not contain `anxious` or `nervous` but does contain words similar to `play` e.g. `play`, `playful`

## Shutting Down

When you're done with the demo, shut down the Redis server:

```bash
$ cd redis-om-python-search-demo
$ docker-compose down
```
