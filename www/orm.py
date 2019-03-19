import asynico, logging
import aiomysql

@asynico.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield.from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306)
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset','utf8'),
        autocommit = kw.get('maxsize',10),
        minsize = kw.get('minsize',1)
        loop = loop
    )

    @asynico.coroutine
    def select(sql, args, size = None):
        log(sql,args)
        global __pool
        with (yield from __pool) as sonn:
        cur = yield from conm.cursor(aiomysql.DicCursor)
        yield from cur.execute(sql.replace('?','%s'))
        if size: 
            rs = yield from cur.fetchmany(size)
            else:
            rs = yield from cur.fetchall()

            yield from cur.close()
            logging.info('rows returned: %s' % len(rs))
            return rs

