from django.db import models

class cryptotable (models.Model):

    id = models.IntegerField(primary_key=True)
    Crypto_Name  = models.CharField(("Crypto Name") , max_length=255)
    Price = models.CharField(("Price"), max_length=255)
    Change_24_H = models.CharField(("Changes 24H"), max_length=255)
    Change_7_D = models.CharField(("Changes 7D"), max_length=255)
    Change_30_D = models.CharField(("Changes 30D"), max_length=255)
    Change_1_Y = models.CharField(("Changes 1Y"), max_length=255)
    Marketcap = models.CharField(("Market Cap") , max_length=255)
    Volume = models.CharField(("Volume 24H") , max_length=255)
    Supply = models.CharField(("Available Supply") , max_length=255)

class predicttable (models.Model):

    id = models.IntegerField(primary_key=True)
    
    Crypto_Name  = models.CharField(("Crypto Name") , max_length=255)
    Price = models.CharField(("Price"), max_length=255)
    Marketcap = models.CharField(("Market Cap") , max_length=255)


