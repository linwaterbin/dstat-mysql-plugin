### Author: linwaterbin@gmail.com
### UPDATE: 2014-2-24
### FUNCTION: analyze mysql temp table use

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
    Plugin for MySQL 5 Temp Table Usage.
    """

    def __init__(self):
        self.name = 'mysql5 tmp usage'
        #self.format = ('d',12,50)
        self.nick = ('mem', 'disk','mem-disk-pct',)
        self.vars = ('memory_tmp_tables', 'disk_tmp_tables','avg_mem_to_disk_pct',)
        self.type = 's'
        self.width = 12 
        self.scale = 50

    def check(self): 
        global MySQLdb
        import MySQLdb
        try:
            self.db = MySQLdb.connect(user=mysql_user,passwd=mysql_pwd,host=mysql_host,db=mysql_db)
        except:
            raise Exception, 'Cannot interface with MySQL server'


    def extract(self):
        try:
            query="""select sum(memory_tmp_tables) as memory_tmp_tables,sum(disk_tmp_tables) as disk_tmp_tables,avg(tmp_tables_to_disk_pct) as avg_mem_to_disk_pct from statements_with_temp_tables;"""
            cur = self.db.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(query)
            for record in cur.fetchall():
                  self.val['memory_tmp_tables'] =record['memory_tmp_tables']
                  self.val['disk_tmp_tables'] = record['disk_tmp_tables']
                  self.val['avg_mem_to_disk_pct'] = record['avg_mem_to_disk_pct'] 


            if step == op.delay:
                self.set1.update(self.set2)

        except Exception, e:
            for name in self.vars:
                self.val[name] = -1

# vim:ts=4:sw=4:et
