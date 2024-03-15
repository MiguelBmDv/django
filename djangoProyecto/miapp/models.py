from django.db import models


    
class Article(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    image=models.ImageField(default='null', upload_to="articles")
    public=models.BooleanField()
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=['id']
    def __str__(self):
        if self.public:
            publico = "(Publicado)"
        else:
            publico="(Privado)"
        return f"{self.id}. {self.title} :: {publico}"

class Category(models.Model):
    name=models.CharField(max_length=110)
    description=models.CharField(max_length=250)
    create_date=models.DateField()

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=['id']
    def __str__(self):
        return f"{self.id}. {self.name}"