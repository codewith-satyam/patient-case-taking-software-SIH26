from django.db import models
class Patient(models.Model):
    GENDER_CHOICE = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    name=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICE)
    mobile=models.CharField(max_length=15)
    chief_complaint=models.TextField(blank=True,help_text="Maim problem reported by the Patient")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.age}"
    
