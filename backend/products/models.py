from django.db import models

class Product(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", blank=True)
    code = models.CharField("Código del producto", max_length=50, unique=True)
    category = models.CharField("Categoría", max_length=50)  # Ej. tornillos, pintura, herramientas
    brand = models.CharField("Marca", max_length=50, blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stock disponible")
    unit = models.CharField("Unidad de medida", max_length=20, default="unidad")  # Ej. unidad, metro, litro
    is_active = models.BooleanField("Está activo", default=True)
    is_taxable = models.BooleanField("Gravado con IVA", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
