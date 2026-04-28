import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_project.settings')
django.setup()

from tours_app.models import Category, TourPackage

def populate():
    # Categories
    adventure, _ = Category.objects.get_or_create(name='Adventure', description='Thrilling experiences for adrenaline junkies.')
    luxury, _ = Category.objects.get_or_create(name='Luxury', description='Premium stays and exclusive services.')
    family, _ = Category.objects.get_or_create(name='Family', description='Plan the perfect trip for all ages.')
    cultural, _ = Category.objects.get_or_create(name='Cultural', description='Immerse yourself in local traditions.')

    # Packages
    TourPackage.objects.get_or_create(
        title='Himalayan Trekking Expedition',
        category=adventure,
        location='Nepal',
        price=1200.00,
        duration_days=10,
        description='A breathtaking trek through the heart of the Himalayas. Experience the majesty of Everest and Annapurna.',
        featured=True
    )

    TourPackage.objects.get_or_create(
        title='Santorini Luxury Escape',
        category=luxury,
        location='Greece',
        price=3500.00,
        duration_days=7,
        description='Stay in white-washed villas with private infinity pools overlooking the Aegean Sea.',
        featured=True
    )

    TourPackage.objects.get_or_create(
        title='Swiss Alps Family Winter',
        category=family,
        location='Switzerland',
        price=2800.00,
        duration_days=6,
        description='Skiing, boarding, and cozy fireside evenings in the beautiful Swiss Alps.',
        featured=True
    )

    TourPackage.objects.get_or_create(
        title='Ancient Wonders of Egypt',
        category=cultural,
        location='Egypt',
        price=1500.00,
        duration_days=8,
        description='Visit the Pyramids of Giza, the Sphinx, and cruise the Nile in this historic journey.',
        featured=False
    )

    print("Population complete.")

if __name__ == '__main__':
    populate()
