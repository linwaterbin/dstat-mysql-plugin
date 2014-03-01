### Author: linwaterbin@gmail.com
### UPDATE: 2014-2-28
### FUNCTION: monitor MySQL query cache usage

# init MySQL authority
global mysql_user
mysql_user = os.getenv('DSTAT_MYSQL_USER')
global mysql_pwd
mysql_pwd = os.getenv('DSTAT_MYSQL_PWD')
global mysql_host
mysql_host = os.getenv('DSTAT_MYSQL_HOST')
global mysql_db
mysql_db = os.getenv('DSTAT_MYSQL_DB')


class dstat_plugin(dstat):
    """
    Plugin for MySQL query cache Usage.
    """

    def __init__(self):
        self.name = 'mysql QC'
        self.nick = ('qhit', 'qins','qlow','qnot',)
        self.vars = ('Qcache_hits', 'Qcache_inserts','Qcache_lowmem_prunes','Qcache_not_cached',)
        self.type = 'd'
        self.width = 7 
        self.scale = 1000

    def check(self): 
        global MySQLdb
        import MySQLdb
        try:
            self.db = MySQLdb.connect(user=mysql_user,passwd=mysql_pwd,host=mysql_host,db=mysql_db)
        except:
            raise Exception, 'Cannot interface with MySQL server'


    def extract(self):
        try:
            v_sql = "show global status like 'Qcache_%';"
            cur = self.db.cursor()
            cur.execute(v_sql)
            row = cur.fetchall()
            c = 8
            while c: 
              self.val['Qcache_hits'] = float(row[2][1])
              self.val['Qcache_inserts'] = float(row[3][1])
              self.val['Qcache_lowmem_prunes'] = float(row[4][1])
              self.val['Qcache_not_cached'] = float(row[5][1])
              c = c-1

            if step == op.delay:
                self.set1.update(self.set2)

        except Exception, e:
            for name in self.vars:
                self.val[name] = -1

        finally:
          cur.close()

# vim:ts=4:sw=4:et
