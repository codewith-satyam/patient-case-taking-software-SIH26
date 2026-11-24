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

    medical_history = models.TextField(
    blank=True,
    help_text="Previous medical history of the patient"
)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.age}"

class Doctor(models.Model):

    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
        ('On Leave', 'On Leave'),
    ]

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='Available'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
