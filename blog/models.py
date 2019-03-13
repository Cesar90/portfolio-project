from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    # Pub_date
    # body
    # image    

# Add the Blog app to the settings

# Create a migrate

# Migrate

# Add to the admin