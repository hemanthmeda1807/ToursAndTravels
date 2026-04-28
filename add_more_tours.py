import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_project.settings')
django.setup()

from tours_app.models import Category, TourPackage

def populate():
    luxury, _ = Category.objects.get_or_create(name='Luxury')
    adventure, _ = Category.objects.get_or_create(name='Adventure')
    cultural, _ = Category.objects.get_or_create(name='Cultural')

    TourPackage.objects.get_or_create(
        title='Bali Beach Paradise',
        category=luxury,
        location='Bali, Indonesia',
        price=1800.00,
        duration_days=7,
        description='Experience the ultimate luxury in Bali with private beachfront villas, spa treatments, and breathtaking sunsets.',
        featured=True,
        image='tours/bali_beach.png'
    )

    TourPackage.objects.get_or_create(
        title='Iceland Aurora Borealis',
        category=adventure,
        location='Reykjavik, Iceland',
        price=2200.00,
        duration_days=5,
        description='Chase the magical Northern Lights across the snowy mountains and glaciers of Iceland.',
        featured=True,
        image='tours/iceland_aurora.png'
    )

    TourPackage.objects.get_or_create(
        title='Serengeti Safari Adventure',
        category=adventure,
        location='Tanzania',
        price=3100.00,
        duration_days=8,
        description='Witness the majestic wildlife of the Serengeti National Park during the golden hour.',
        featured=False,
        image='tours/serengeti_safari.png'
    )

    TourPackage.objects.get_or_create(
        title='Kyoto Spring Blossoms',
        category=cultural,
        location='Kyoto, Japan',
        price=2400.00,
        duration_days=10,
        description='Immerse yourself in Japanese culture and witness the stunning cherry blossoms in ancient Kyoto.',
        featured=True,
        image='tours/kyoto_spring.png'
    )

    print("More tours added successfully!")

if __name__ == '__main__':
    populate()
