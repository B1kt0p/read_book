from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name='Наименование категории'
                            )
    description = models.TextField(verbose_name='Краткое описание')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'



class Good(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Наименование товара'
                            )
    description = models.TextField(verbose_name='Описание товара')
    in_stock = models.BooleanField(default=True,
                                   db_index=True,
                                   verbose_name='В наличии'
                                   )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0, verbose_name='Цена')

    def __str__(self):
        s = self.name
        if not self.in_stock:
            return s + '(нет в наличии)'
        return s

    def get_is_stock(self):
        if self.in_stock:
            return '+'
        else:
            return ''

    class Meta:
        ordering = ['-price', 'name']
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'