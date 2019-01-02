#!/usr/bin/env python3

import time

import connexion
import logging
from apscheduler.schedulers.background import BackgroundScheduler

import clien_bot.log
from clien_bot import encoder
from clien_bot.services.bot_service import Bot
from flask_env import Environments
from clien_bot.services.crawl_service import CrawlService


def crawl_job(mongo_uri):
    service = CrawlService(mongo_uri)
    service.get_latest_articles()


def main():
    clien_bot.log.configure_logger()
    logger = logging.getLogger('main')
    app = connexion.App(__name__, specification_dir='./swagger/')
    env = Environments(app.app)
    env.from_yaml('config.yml')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Clien notification bot'})

    mongo_uri = app.app.config['MONGO_URI']
    bot = Bot(app.app.config['TELEGRAM_BOT_TOKEN'], mongo_uri)
    bot.run()

    scheduler = BackgroundScheduler()
    scheduler.start()
    logger.info('Background scheduler started.')
    scheduler.add_job(func=crawl_job, trigger='interval', args=[mongo_uri], minutes=1)

    app.run(port=8080)

    # 종료시 bot, scheduler 종료 (shutdown 하지 않으면 bot에서 hang 걸림)
    logger.info('Shutdown...')
    bot.shutdown()
    logger.info('Shutdown bot.')
    scheduler.remove_all_jobs()
    scheduler.shutdown(wait=False)
    logger.info('Shutdown scheduler.')


if __name__ == '__main__':
    main()