from django.db import models


# Create your models here


class Transition(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilisateur = models.CharField(db_column='Utilisateur', max_length=70)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=120)  # Field name made lowercase.
    attribut = models.CharField(db_column='Attribut', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    heure = models.TimeField(db_column='Heure')  # Field name made lowercase.
    delai = models.TimeField(db_column='Delai', blank=True, null=True)  # Field name made lowercase.
    reftran = models.BigIntegerField(db_column='RefTran', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transition'
        unique_together = (('id', 'utilisateur'),)


class Userfiles(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=70)  # Field name made lowercase.
    idforum = models.BigIntegerField(db_column='IDForum', blank=True, null=True)  # Field name made lowercase.
    idmsg = models.BigIntegerField(db_column='IDMsg')  # Field name made lowercase.
    filenameo = models.CharField(db_column='Filenameo', max_length=70)  # Field name made lowercase.
    filenamer = models.CharField(db_column='Filenamer', max_length=20)  # Field name made lowercase.
    filetype = models.CharField(db_column='Filetype', max_length=5, blank=True, null=True)  # Field name made lowercase.
    filesize = models.CharField(db_column='Filesize', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dateupload = models.DateField(db_column='Dateupload')  # Field name made lowercase.
    timeupload = models.TimeField(db_column='Timeupload')  # Field name made lowercase.
    date_la = models.DateField(db_column='Date_la', blank=True, null=True)  # Field name made lowercase.
    time_la = models.TimeField(db_column='Time_la', blank=True, null=True)  # Field name made lowercase.
    nbdownload = models.BigIntegerField(db_column='Nbdownload', blank=True, null=True)  # Field name made lowercase.
    filestatus = models.IntegerField(db_column='Filestatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userfiles'



