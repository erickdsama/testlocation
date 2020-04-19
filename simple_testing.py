import unittest
from uuid import uuid4

locations = [
    {
        "latitude": "31.638173",
        "longitude": "-106.426264"
    },
    {
        "latitude": "20.659698",
        "longitude": "-103.349609"
    },
    {
        "latitude": "19.432608",
        "longitude": "-99.133209"
    },
    {
        "latitude": "25.686613",
        "longitude": "-100.316116"
    },
    {
        "latitude": "20.603446",
        "longitude": "-100.408160"
    },
]


class UnitTests(unittest.TestCase):
    username = "testing_{}@domain.com".format(uuid4())
    password = "123456"
    user_id = None
    vehicle_id = None
    jwt = None

    def test_1_create_user(self):
        from main import app
        with app.test_client() as c:
            rv = c.post('/api/v1/user', json={
                'username': self.username,
                'email': self.username,
                'password': self.password,
                'full_name': 'Testing Name'
            })
            json_data = rv.get_json()
            UnitTests.user_id = json_data.get("id")
            self.assertEqual(rv.status_code, 201)

    def test_2_auth(self):
        from main import app
        with app.test_client() as c:
            rv = c.post('/api/v1/auth', json={
                'username': self.username, 'password': self.password
            })
            json_data = rv.get_json()
            UnitTests.jwt = json_data.get("jwt")
            self.assertIsNotNone(self.jwt)

    def test_3_create_vehicle(self):
        from main import app
        with app.test_client() as c:
            rv = c.post('/api/v1/vehicle', headers={'Authorization': 'Bearer {}'.format(self.jwt)}, json={
                "vin": "ABCDEF67890",
                "plate": "ABC-129-9",
                "user_id": self.user_id
            })
            json_data = rv.get_json()
            UnitTests.vehicle_id = json_data.get("id")
            self.assertEqual(rv.status_code, 201)

    def test_4_create_coordinates(self):
        from main import app
        with app.test_client() as c:
            for location in locations:
                rv = c.post(
                    '/api/v1/location',
                    headers={
                        'Authorization': 'Bearer {}'.format(self.jwt)
                    },
                    json={
                        "latitude": location.get("latitude"),
                        "longitude": location.get("longitude"),
                        "vehicle_id": self.vehicle_id
                    })
            self.assertEqual(rv.status_code, 201)

    def test_5_last_location(self):
        from main import app
        with app.test_client() as c:
            rv = c.get(
                '/api/v1/vehicle/{}/last-location'.format(self.vehicle_id),
                headers={
                    'Authorization': 'Bearer {}'.format(self.jwt)
                })
            json_data = rv.get_json()
            last_latitude = json_data.get("latitude")
            last_longitude = json_data.get("longitude")
            location = locations[4]
            self.assertEqual(last_latitude, location.get("latitude"))
            self.assertEqual(last_longitude, location.get("longitude"))


if __name__ == '__main__':
    unittest.main()

"""
kulu@c6793593327e:/opt/project$ python simple_testing.py  -v
test_1_create_user (__main__.UnitTests) ... ok
test_2_auth (__main__.UnitTests) ... ok
test_3_create_vehicle (__main__.UnitTests) ... ok
test_4_create_coordinates (__main__.UnitTests) ... ok
test_5_last_location (__main__.UnitTests) ... ok
----------------------------------------------------------------------
Ran 5 tests in 1.695s

OK
"""
