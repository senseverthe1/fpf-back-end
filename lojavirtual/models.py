from django.db import models


class Produto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Categoria(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('category_name',)

    def __str__(self):
        return self.category_name
