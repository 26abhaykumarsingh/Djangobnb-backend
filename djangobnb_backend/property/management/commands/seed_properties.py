import random
import requests
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.utils.text import slugify
from faker import Faker
from property.models import Property

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Generates 100 random properties using Faker and downloads matching images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting property generation (this may take a few minutes as it downloads 100 images)...')

        # 1. Get or create your landlord account matching your exact Custom User model
        landlord, created = User.objects.get_or_create(
            email='26abhaykumarsingh@gmail.com',
            defaults={
                'name': 'Abhay Kumar Singh',
                'is_staff': True,
                'is_superuser': True,  # Making you a superuser so you can access admin
                'is_active': True,
                'avatar': ''  # Satisfies your model requirement since null=True is absent
            }
        )
        if created:
            landlord.set_password('password123')
            landlord.save()
            self.stdout.write(self.style.SUCCESS('Created landlord account for 26abhaykumarsingh@gmail.com'))
        else:
            self.stdout.write(self.style.SUCCESS('Found existing landlord account.'))

        # 2. Define matched data sets
        countries = {
            "US": "United States", "CA": "Canada", "GB": "United Kingdom", 
            "FR": "France", "JP": "Japan", "AU": "Australia", 
            "DE": "Germany", "IT": "Italy", "ES": "Spain", "IN": "India"
        }

        # Thematic image pools
        category_data = {
            "Cabin": [
                "https://images.unsplash.com/photo-1542718145-4299b9cfac7a",
                "https://images.unsplash.com/photo-1587061949409-02df41d5e562",
                "https://images.unsplash.com/photo-1449844908441-8829872d2607"
            ],
            "Villa": [
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9",
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750",
                "https://images.unsplash.com/photo-1580587771525-78b9dba3b914"
            ],
            "Apartment": [
                "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688",
                "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
                "https://images.unsplash.com/photo-1493809842364-78817add7ffb"
            ],
            "Beach House": [
                "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2",
                "https://images.unsplash.com/photo-1510798831971-661eb04b3739",
                "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4"
            ]
        }

        # 3. Generate 100 properties
        properties_created = 0
        for i in range(1, 101):
            category = random.choice(list(category_data.keys()))
            image_url = random.choice(category_data[category])
            
            city = fake.city()
            title = f"{city} {category} Retreat"
            description = fake.paragraph(nb_sentences=5)
            
            country_code = random.choice(list(countries.keys()))
            country = countries[country_code]
            
            bedrooms = random.randint(1, 5)
            
            prop = Property(
                title=title,
                description=description,
                price_per_night=random.randint(50, 800),
                bedrooms=bedrooms,
                bathrooms=random.randint(1, bedrooms),
                guests=bedrooms * 2,
                country=country,
                country_code=country_code,
                category=category,
                landlord=landlord
            )

            try:
                response = requests.get(image_url + "?w=800&q=80", headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    file_name = f"{slugify(title)}-{i}.jpg"
                    prop.image.save(file_name, ContentFile(response.content), save=False)
                    prop.save()
                    properties_created += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Failed to download image for {title}: {e}"))

            if i % 10 == 0:
                self.stdout.write(f"Processed {i}/100 properties...")

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {properties_created} properties!'))
