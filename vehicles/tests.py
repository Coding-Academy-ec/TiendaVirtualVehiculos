from django.test import TestCase
from django.urls import reverse
from vehicles.models import Vehicle

class VehicleViewsTestCase(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(name='Test Vehicle', year=2022, price=10000)

    def test_vehicle_list_view(self):
        response = self.client.get(reverse('vehicle_list'))
        self.assertEqual(response.status_code, 200)  # Verificar que se obtenga una respuesta exitosa
        self.assertTemplateUsed(response, 'vehicle_list.html')  # Verificar que se esté utilizando la plantilla correcta

    def test_vehicle_detail_view(self):
        response = self.client.get(reverse('vehicle_detail', args=[self.vehicle.id]))
        self.assertEqual(response.status_code, 200)  # Verificar que se obtenga una respuesta exitosa
        self.assertTemplateUsed(response, 'vehicle_detail.html')  # Verificar que se esté utilizando la plantilla correcta

    def test_add_vehicle_view(self):
        response = self.client.post(reverse('add_vehicle'), data={'name': 'New Vehicle', 'year': 2022, 'price': 15000})  # Añadido un valor para el campo price
        self.assertEqual(response.status_code, 200)  # Verificar que se redirija después de agregar un vehículo

    def test_edit_vehicle_view(self):
        response = self.client.post(reverse('edit_vehicle', args=[self.vehicle.id]), data={'name': 'Edited Vehicle', 'year': 2022, 'price': 15000})
        self.assertEqual(response.status_code, 200) # Verificar que se redirija después de editar un vehículo

    def test_delete_vehicle_view(self):
        response = self.client.post(reverse('delete_vehicle', args=[self.vehicle.id]))
        self.assertEqual(response.status_code, 302)  # Verificar que se redirija después de eliminar un vehículo
