from django.db import models
from django.urls import reverse

class Orders(models.Model):
    address=models.TextField()
    kg=models.DecimalField(default=0, max_digits=5, decimal_places=2)
    price=models.DecimalField(max_digits=20, decimal_places=1)
    debt=models.BooleanField(default=False)
    give=models.DecimalField(max_digits=20, decimal_places=1, default=0)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        if len(self.address)>=15:
            self.address=self.address[:15]+"..."
        return f"{self.address}: {self.kg}-kg {self.price}-sum"
    
    def get_absolute_url(self):
        return reverse("ShopApp:detail", kwargs={"pk": self.pk})
    class Meta:
        verbose_name="Zakazlar"
        verbose_name_plural="Zakazlar"
        
    
    