# -*- coding: utf-8 -*-

# Scrapy settings for Tengxun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Tengxun'

SPIDER_MODULES = ['Tengxun.spiders']
NEWSPIDER_MODULE = 'Tengxun.spiders'

#自定义变量
#定义日志级别
#LOG_LEVEL=""
#输出文件
#LOG_FILE='文件名.log'
#导出数据时的编码
#FEED_EXPORT_ENCODING = 'utf-8' 

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Tengxun (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'User_Agent': 'Mozilla/5.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Tengxun.middlewares.TengxunSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Tengxun.middlewares.TengxunDownloaderMiddleware': 543,
##   注册自定义中间件
#    'Testmiddleware.middlewares.RandomUAmiddleware' : 300,
#    'Testmiddleware.middlewares.RandomProxyMiddleware':200,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Tengxun.pipelines.TengxunPipeline': 300,
   #'Daomu.pipelines.MongoPipeline': 300,
   'Tengxun.pipelines.MysqlPipeline':300,
}

MYSQL_HOST='192.168.3.3'
MYSQL_USER='root'
MYSQL_PWD='123456'
MySQL_DB='Tencent'

##MONGODB_HOST='192.168.3.3'
##MONGODB_PORT=27017
##MONGODB_DB='Daomu'
##MONGODB_SET='book'


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

##分布式原理(共享爬取队列)scrapy_redis
##指纹存储在redis，数据可以存储在其他地方
##重新配置各模块
##    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
##去重
##    DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
##保持调度器队列，断点续爬（不会清空指纹）
##    SCHEDULER_PERSIST = True
##管道：数据处理
##    ITEM_PIPELINES = {
##        'scrapy_redis.pipelines.RedisPipeline': 400,
##    }
##配置redis数据库链接地址
##    REDIS_HOST='127.0.0.1'
##    REDIS_PORT=6379













