
from django.db import models

class Menu(models.Model):
    nomi = models.CharField(max_length=100,help_text='Menyu nomini kiriting...')
    def __str__(self):
        return self.nomi
    
    

    class Meta:
        verbose_name = 'Menyu '
        verbose_name_plural = 'Menyular '
        


class Mahsulot(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,help_text='Mahsulot turini tanlang')
    nomi = models.CharField(max_length=200,help_text='Mahsulot nomini kiriting...')
    mahsulot_haqida = models.TextField(help_text='Mahsulot haqida ma`lumot')
    rasm = models.ImageField(upload_to='mahsulotlar')
    narx = models.IntegerField(help_text='Mahsulot narxini kiriting')
    
    def __str__(self):
        return self.nomi
    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar '      
