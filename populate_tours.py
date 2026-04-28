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
            'category': cat_adventure,
            'title': 'Himalayan Trekking Expedition',
            'description': 'A 10-day rigorous trek through the majestic Himalayas.',
            'location': 'Nepal',
            'price': 1200.00,
            'duration_days': 10,
            'image': 'tours/himalayas.jpg',
            'featured': True,
        },
        {
            'category': cat_relax,
            'title': 'Maldives Beach Retreat',
            'description': 'Relax on the pristine beaches of the Maldives for a week.',
            'location': 'Maldives',
            'price': 2500.00,
            'duration_days': 7,
            'image': 'tours/maldives.jpg',
            'featured': True,
        },
        {
            'category': cat_cultural,
            'title': 'Kyoto Heritage Tour',
            'description': 'Explore the ancient temples and shrines of Kyoto.',
            'location': 'Japan',
            'price': 1800.00,
            'duration_days': 5,
            'image': 'tours/kyoto.jpg',
            'featured': False,
        },
        {
            'category': cat_adventure,
            'title': 'Amazon Rainforest Safari',
            'description': 'Discover the exotic wildlife of the Amazon rainforest.',
            'location': 'Brazil',
            'price': 1500.00,
            'duration_days': 8,
            'image': 'tours/amazon.jpg',
            'featured': False,
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
