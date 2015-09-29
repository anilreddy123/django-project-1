import csv
import sqlite3
from os.path import abspath,dirname
from django.db import models

from mptt.models import TreeForeignKey, MPTTModel #third party import

# model for creating cornerstoneuserprofile


class CornerstoneUserProfile(MPTTModel):

    guid= models.UUIDField(unique=True, blank=False)
    user_id = models.IntegerField(blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    parent= TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True )  # parent is nothing but manager_id
    manager_guid = models.UUIDField(blank=False)

    def import_from_csv(self, file_name):  #importing the csv file
        file_name= file_name
        file_extension='.csv'
        pwd= abspath(dirname(__file__))
        file_path= pwd+'/data/'+file_name+file_extension
        users = csv.reader(open(file_path))

        con = None

        try:
            con = sqlite3.connect('db.sqlite3')

            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS CornerstoneUserProfile")
            cur.execute("CREATE TABLE CornerstoneUserProfile(guid uuid, user_id int, first_name char, last_name char,parent int,  manager_guid uuid)")
            cur.executemany("INSERT INTO CornerstoneUserProfile VALUES(?,?,?,?,?,?)", users)
            con.commit()

        finally:
            if con:
                con.close()






