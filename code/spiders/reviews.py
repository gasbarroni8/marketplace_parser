import json
import logging
import os
from datetime import date

import scrapy
from decouple import config

from .utils import get_parse_date


class ReviewsSpider(scrapy.Spider):
    url = config('API_REVIEWS_URL')
    headers = {
        "Accept": "application/json, text/*", "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru,en;q=0.9,kk;q=0.8,es;q=0.7,ba;q=0.6", "Connection": "keep-alive",
        "Host": "kaspi.kz", "Cache-Control": "no-cache, no-store, max-age=0"
    }

    def __init__(self, category):
        super().__init__()
        today = str(date.today())
        reviews_dir = '../data/reviews'
        products_dir = '../data/products'

        self.category = category
        self.parse_date = get_parse_date(products_dir, today)
        self.parse_list = f'{products_dir}/{self.parse_date}/{category}-list.json'

        self.output_dir = f'{reviews_dir}/{today}/{category}'
        os.makedirs(self.output_dir, exist_ok=True)

        self.log(f"Parser for {self.category} has been started.")

    def start_requests(self):
        with open(self.parse_list) as products_json:
            products = json.load(products_json)
            for product in products:
                yield scrapy.Request(
                    url=self.url.format(product['id'], 4000),  # link is like /product/1001/reviews?limit=5
                    headers=self.headers,
                    callback=self.parse_reviews,
                    cb_kwargs={'product_id': product['id'], 'actual_reviews_quantity': product['reviewsQuantity']}
                )

    def parse_reviews(self, response, product_id, actual_reviews_quantity):
        reviews_json = response.body_as_unicode()
        with open(f'{self.output_dir}/{product_id}.json', 'w') as f:
            f.write(reviews_json)

        reviews = json.loads(reviews_json)
        parsed_reviews_quantity = len(reviews['data'])

        if actual_reviews_quantity != parsed_reviews_quantity:
            self.logger.warning(
                f'Product with id={product_id} received {parsed_reviews_quantity} reviews, '
                f'but has {actual_reviews_quantity}'
            )


class BeautySpider(ReviewsSpider):
    name = "beauty-reviews"
    category = "beauty"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class BigHomeAppSpider(ReviewsSpider):
    name = "bha-reviews"
    category = "big-home-appl"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class SmallHomeAppSpider(ReviewsSpider):
    name = "sha-reviews"
    category = "small-home-appl"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class KitchenHomeAppSpider(ReviewsSpider):
    name = "kha-reviews"
    category = "kitchen-home-appl"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class ClimateEquipmentSpider(ReviewsSpider):
    name = "climate-reviews"
    category = "climate-equipment"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class BooksSpider(ReviewsSpider):
    name = "books-reviews"
    category = "books"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class HeadphonesSpider(ReviewsSpider):
    name = "headphones-reviews"
    category = "headphones"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class PerfumesSpider(ReviewsSpider):
    name = "perfumes-reviews"
    category = "perfumes"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class CarAudioSpider(ReviewsSpider):
    name = "car-audio-reviews"
    category = "car-audio"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class CarElectronicsSpider(ReviewsSpider):
    name = "car-electronics-reviews"
    category = "car-electronics"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class MemoryCardsSpider(ReviewsSpider):
    name = "memory-cards-reviews"
    category = "memory-cards"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class PowerBanksSpider(ReviewsSpider):
    name = "power-banks-reviews"
    category = "power-banks"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class TiresSpider(ReviewsSpider):
    name = "tires-reviews"
    category = "tires"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class WatchesSpider(ReviewsSpider):
    name = "watches-reviews"
    category = "watches"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class WearablesSpider(ReviewsSpider):
    name = "wearables-reviews"
    category = 'wearables'
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class SmartphonesSpider(ReviewsSpider):
    name = "smartphones-reviews"
    category = "smartphones"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)


class PortableSpeakersSpider(ReviewsSpider):
    name = "portable-speakers-reviews"
    category = "portable-speakers"
    custom_settings = {
        'LOG_FILE': f'logs/{date.today()}{name}.log'
    }
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        super().__init__(self.category)
