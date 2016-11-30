# author: G. Alomar

import os
class Config: pass
import logging
logging.basicConfig()
global config
config = Config()

try:
    config.nodePort = os.environ['NODE_PORT']
    logging.info('NODE_PORT: %s', config.nodePort)
except KeyError:
    logging.warn('using default NODE_PORT 9042')
    config.nodePort = 9042

try:
    config.contact_names = os.environ['CONTACT_NAMES'].split(",")
    logging.info('CONTACT_NAMES: %s', str.join(" ", config.contact_names))
except KeyError:
    logging.warn('using default contact point localhost')
    config.contact_names = ['localhost']
if 'cluster' not in globals():
    global cluster, session
    if 'TESTING' in os.environ:
        class clusterMock: pass
        class sessionMock: pass

        cluster = clusterMock()
        session = sessionMock()

    else:
        from cassandra.cluster import Cluster
        logging.info('Initializing global session')
        cluster = Cluster(contact_points=config.contact_names, port=config.nodePort)
        session = cluster.connect()
        session.execute(
            "CREATE KEYSPACE IF NOT EXISTS hecuba WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3 }")
        session.execute(
            'CREATE TABLE IF NOT EXISTS hecuba.blocks (blockid text, block_classname text,storageobj_classname text, tkns list<bigint>, ' +
            'entry_point text , port int, ksp text , tab text , dict_name text , obj_type text, PRIMARY KEY(blockid))')
try:
    config.execution_name = os.environ['EXECUTION_NAME']
    logging.info('EXECUTION_NAME: %s', config.execution_name)
except KeyError:
    config.execution_name = 'hecuba_app'
    logging.warn('using default EXECUTION_NAME: %s', config.execution_name)

try:
    config.tasks_per_worker = int(os.environ['TASKS_PER_WORKER'])
    logging.info('TASKS_PER_WORKER: %s', config.tasks_per_worker)
except KeyError:
    config.tasks_per_worker = 8
    logging.warn('using default TASKS_PER_WORKER: %s', config.tasks_per_worker)

try:
    config.ranges_per_block = os.environ['RANGES_PER_BLOCK']
    logging.info('RANGES_PER_BLOCK: %s', config.ranges_per_block)
except KeyError:
    config.ranges_per_block = 32
    logging.warn('using default RANGES_PER_BLOCK: %s', config.ranges_per_block)

try:
    config.cache_activated = os.environ['CACHE_ACTIVATED'].lower() == 'true'
    logging.info('CACHE_ACTIVATED: %s', config.cache_activated)
except KeyError:
    config.cache_activated = True
    logging.warn('using default RANGES_PER_BLOCK: %s', config.cache_activated)

try:
    config.batch_size = os.environ['BATCH_SIZE']
    logging.info('BATCH_SIZE: %s', config.batch_size)
except KeyError:
    config.batch_size = 100
    logging.warn('using default BATCH_SIZE: %s', config.batch_size)

try:
    config.max_cache_size = os.environ['MAX_CACHE_SIZE']
    logging.info('MAX_CACHE_SIZE: %s', config.max_cache_size)
except KeyError:
    config.max_cache_size = 100
    logging.warn('using default MAX_CACHE_SIZE: %s', config.max_cache_size)

try:
    config.repl_factor = os.environ['REPLICA_FACTOR']
    logging.info('REPLICA_FACTOR: %s', config.repl_factor)
except KeyError:
    config.repl_factor = 1
    logging.warn('using default REPLICA_FACTOR: %s', config.repl_factor)

try:
    config.repl_class = os.environ['REPLICATION_STRATEGY']
    logging.info('REPLICATION_STRATEGY: %s', config.repl_class)
except KeyError:
    config.repl_class = "SimpleStrategy"
    logging.warn('using default REPLICATION_STRATEGY: %s', config.repl_class)

try:
    config.statistics_activated = os.environ['STATISTICS_ACTIVATED'].lower() == 'true'
    logging.info('STATISTICS_ACTIVATED: %s', config.statistics_activated)
except KeyError:
    config.statistics_activated = True
    logging.warn('using default STATISTICS_ACTIVATED: %s', config.statistics_activated)


try:
    query = "CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : \'%s\', 'replication_factor' : %d};"\
            % (config.execution_name,config.repl_class,config.repl_factor)
    session.execute(query)
except Exception as e:
    print "Cannot create keyspace", e



