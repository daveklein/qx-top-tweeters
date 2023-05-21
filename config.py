kafka_config = { 
    "bootstrap.servers": "localhost:29092",
}

credentials = {
    "consumer.key": "FRoPZuAt3RCzkEkPrALX2sSg9",
    "consumer.secret": "Tv9Z52hXcBNniFR3W72w6uP2fXcC65RgyJqOcWzwdjOGZTGx6F",
    "access.token": "8678702-KoR0Envx1UlqNqVo1aAHRyCqPWvweVe1LIo366zx1j",
    "access.token_secret": "EyjbA4i7S2u1ZasKTQcHwHzbznbU7EZ8CiHcgRZnJrhLn"
}

tp_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "conf-tweets"
}

td_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "top-tweeters"
}

topics = {
    "input": "conf-tweets",
    "output": "top-tweeters",
    "hashtag": "pyconit"
}
