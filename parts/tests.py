from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Part

class PartAPITests(TestCase):
    def setUp(self):
        Part.objects.all().delete()

        self.client = APIClient()
        self.part_data = {
            'name': 'Test Part',
            'sku': 'TEST1234',
            'description': 'This is a test part',
            'weight_ounces': 8,
            'is_active': True
        }
        self.part = Part.objects.create(
            name='Heavy coil',
            sku='SDJDDH8223DHJ',
            description='Tightly wound nickel-gravy alloy spring',
            weight_ounces=3,
            is_active=True
        )

    def test_get_all_parts(self):
        """Test retrieving all parts"""
        response = self.client.get(reverse('part-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_part(self):
        """Test creating a new part"""
        response = self.client.post(
            reverse('part-list'),
            self.part_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 2)
        self.assertEqual(Part.objects.get(sku='TEST1234').name, 'Test Part')

    def test_get_single_part(self):
        """Test retrieving a specific part"""
        response = self.client.get(reverse('part-detail', args=[self.part.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Heavy coil')

    def test_update_part(self):
        """Test updating a part"""
        updated_data = {
            'name': 'Updated Part',
            'sku': self.part.sku,
            'description': self.part.description,
            'weight_ounces': self.part.weight_ounces,
            'is_active': self.part.is_active
        }
        response = self.client.put(
            reverse('part-detail', args=[self.part.id]),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Part')
        self.part.refresh_from_db()
        self.assertEqual(self.part.name, 'Updated Part')

    def test_partial_update_part(self):
        """Test partially updating a part"""
        response = self.client.patch(
            reverse('part-detail', args=[self.part.id]),
            {'name': 'Partially Updated Part'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.part.refresh_from_db()
        self.assertEqual(self.part.name, 'Partially Updated Part')

    def test_delete_part(self):
        """Test deleting a part"""
        response = self.client.delete(reverse('part-detail', args=[self.part.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Part.objects.count(), 0)

    def test_common_words(self):
        """Test the common words endpoint"""
        Part.objects.create(
            name='Part 1',
            sku='SKU1',
            description='This is a test part with common words',
            weight_ounces=5,
            is_active=True
        )
        Part.objects.create(
            name='Part 2',
            sku='SKU2',
            description='This is another test part with common words',
            weight_ounces=8,
            is_active=True
        )

        response = self.client.get(reverse('part-common-words'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        # Check if 'words' and 'is' are in the top 5 (they should be)
        words = [item['word'] for item in response.data]
        self.assertTrue('words' in words or 'is' in words or 'part' in words)