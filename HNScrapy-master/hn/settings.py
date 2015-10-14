BOT_NAME = 'hn'

SPIDER_MODULES = ['hn.spiders']
NEWSPIDER_MODULE = 'hn.spiders'

DATABASE = {'drivername': 'mysql',
            'username': 'root',
            'password': '060901',
            'database': 'content'}

ITEM_PIPELINES = {
    'hn.pipelines.HnPipeline':300
}
