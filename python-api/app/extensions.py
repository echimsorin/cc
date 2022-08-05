from flaskext.mysql import MySQL
import pymysql

# Connector to MySQL instance
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
