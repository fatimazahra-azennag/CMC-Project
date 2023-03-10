# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activite(models.Model):
    idact = models.AutoField(db_column='IDAct', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=120)  # Field name made lowercase.
    typeact = models.IntegerField(db_column='TypeAct')  # Field name made lowercase.
    idcat = models.IntegerField(db_column='IDCat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activite'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Typeu(models.Model):
    id = models.SmallAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeu'


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


class Usertool(models.Model):
    iduser = models.AutoField(db_column='IDUser', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertool'


class UsertoolNotes(models.Model):
    idnote = models.AutoField(db_column='IDNote', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20)  # Field name made lowercase.
    share = models.IntegerField(db_column='Share')  # Field name made lowercase.
    nbmax = models.IntegerField(db_column='Nbmax')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    lastaccess = models.DateField(db_column='Lastaccess')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertool_notes'


class UsertoolParam(models.Model):
    idparam = models.AutoField(db_column='IDParam', primary_key=True)  # Field name made lowercase.
    paramname1 = models.CharField(db_column='Paramname1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paramvalue1 = models.CharField(db_column='Paramvalue1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description1 = models.CharField(db_column='Description1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname2 = models.CharField(db_column='Paramname2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paramvalue2 = models.CharField(db_column='Paramvalue2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description2 = models.CharField(db_column='Description2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname3 = models.CharField(db_column='Paramname3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paramvalue3 = models.CharField(db_column='Paramvalue3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description3 = models.CharField(db_column='Description3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname4 = models.CharField(db_column='Paramname4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paramvalue4 = models.CharField(db_column='Paramvalue4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description4 = models.CharField(db_column='Description4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertool_param'


class UsertoolSharenote(models.Model):
    idshare = models.AutoField(db_column='IDShare', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20)  # Field name made lowercase.
    idnote = models.IntegerField(db_column='IDNote')  # Field name made lowercase.
    dateshare = models.DateField(db_column='Dateshare')  # Field name made lowercase.
    lastaccess = models.DateField(db_column='Lastaccess')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertool_sharenote'


class Utilisateur(models.Model):
    idu = models.BigAutoField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    usager = models.CharField(db_column='Usager', max_length=70)  # Field name made lowercase.
    trace = models.IntegerField(db_column='Trace')  # Field name made lowercase.
    idtypeu = models.IntegerField(db_column='IDTypeU')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilisateur'
