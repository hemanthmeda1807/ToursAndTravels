import os
import django

# 1. Setup Django first!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_project.settings')
django.setup()

# 2. Now import models
from tours_app.models import Category, TourPackage
from django.conf import settings
from django.core.files import File

def populate():
    # 1. Create Categories
    cat_adventure, _ = Category.objects.get_or_create(
        name="Adventure",
        defaults={'description': 'Thrilling and exciting adventure tours.'}
    )
    cat_relax, _ = Category.objects.get_or_create(
        name="Relaxation",
        defaults={'description': 'Peaceful and relaxing getaways.'}
    )
    cat_cultural, _ = Category.objects.get_or_create(
        name="Cultural",
        defaults={'description': 'Immerse yourself in rich cultures.'}
    )

    print("Categories created or already exist.")

    # 2. Create Tour Packages
    packages = [
        {
            'category': cat_relax,
            'title': 'Bali Beach Paradise',
            'description': 'Enjoy the tropical sun and crystal clear waters of Bali.',
            'location': 'Indonesia',
            'price': 1200.00,
            'duration_days': 5,
            'image': 'tours/bali_beach.png',
            'featured': True,
        },
        {
            'category': cat_adventure,
            'title': 'Iceland Aurora Adventure',
            'description': 'Witness the magical Northern Lights in the heart of Iceland.',
            'location': 'Iceland',
            'price': 2500.00,
            'duration_days': 7,
            'image': 'tours/iceland_aurora.png',
            'featured': True,
        },
        {
            'category': cat_cultural,
            'title': 'Kyoto Heritage Tour',
            'description': 'Explore the ancient temples and shrines of Kyoto.',
            'location': 'Japan',
            'price': 1800.00,
            'duration_days': 5,
            'image': 'tours/kyoto.png',
            'featured': True,
        },
        {
            'category': cat_adventure,
            'title': 'Serengeti Wildlife Safari',
            'description': 'Experience the great migration in the Serengeti.',
            'location': 'Tanzania',
            'price': 1500.00,
            'duration_days': 8,
            'image': 'tours/serengeti_safari.png',
            'featured': True,
        },
    ]

    for pkg in packages:
        TourPackage.objects.get_or_create(
            title=pkg['title'],
            defaults=pkg
        )
    print("Tour Packages created or already exist.")

if __name__ == '__main__':
    populate()
