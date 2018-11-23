from config import Config
base_config=Config()

base_config.MAX_THREAD=50
base_config.FILE_NUM=300
base_config.SYSTEM_NAME='whatever'


print base_config

redis_config=Config()
redis_config.HOST='localhost'
redis_config.PORT=3336