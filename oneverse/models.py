from django.db import models

from oneverse.manage import VerseManager, GcmRegisterManager, SecretManager


class Verse(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    push_date = models.DateField(default=None, null=True)
    verse = models.CharField(max_length = 255, default=None)
    source = models.CharField(max_length = 100, default=None)
    detail = models.TextField(default=None, null=True)

    class Meta:
        ordering = ['-push_date']

    # the full mailling address
    def __str__(self):
        return u'%s, %s, %s' % (self.push_date, self.verse, self.source)


    objects = VerseManager()


class GcmRegister(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gcmToken = models.CharField(max_length = 255, default=None)
    deviceId = models.CharField(max_length = 100, default=None)

    class Meta:
        ordering = ['-created']

    # the full mailling address
    def __str__(self):
        return u'%s, %s, %s' % (self.gcmToken, self.deviceId, self.create)


    objects = GcmRegisterManager

class Secret(models.Model):
    api_key = models.CharField(max_length = 100, default=None)

    class Meta:
        ordering = ['-id']

    # the full mailling address
    def __str__(self):
        return u'%s, %s' % (self.id, self.api_key)

    objects = SecretManager