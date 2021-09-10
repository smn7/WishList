from django.db import models

class Product(models.Model):
    """ Таблица с товарами
    Идентификатор
    Ниаменование
    Цена
    Дата и время создания   
    
    """
    title = models.CharField(max_length=20)
    link = models.URLField()
    price = models.IntegerField()
    creat_at = models.DateTimeField(auto_created=True)

    ## Будет выводить кратконаименование в качестве title
    def __str__(self):
        return self.title


