

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from CarDiary.auth_app.models import Profile
from CarDiary.web.models import Car

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'image': 'http://test.picture/url.png',
        'gender': Profile.MALE

    }

    VALID_CAR_DATA = {
        'make': 'Subaru',
        'model': 'Legacy',
        'type': Car.TYPE_SEDAN,
        'year': '2001',
        'transmission': Car.TRANSMISSION_MANUAL,
        'engine_size_cc': '2500',
        'current_km': '100000',
        'last_serviced_at_km': '120000',
        'horse_power': '150',
        'image_url': 'https://www.reviewofreligions.org/wp-content/uploads/2021/01/samurai-warrior-smalll-shutterstock_1345891196-1024x1024.jpeg',
        'description': 'AWD great condition',

    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def __create_car_for_user(self, user):

        car = Car.objects.create(
            **self.VALID_CAR_DATA,
            user=user,
        )

        return car

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile-details.html')

    def test_when_user_has_no_cars__cars_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()

        response = self.__get_response_for_profile(profile)
        self.assertListEqual(
            [],
            response.context['cars'],
        )

    def test_when_user_has_cars__expect_to_return_only_users_cars(self):
        user, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser2',
            'password': '12345qwe',
        }
        user2 = self.__create_user(**credentials)

        car = self.__create_car_for_user(user)

        self.__create_car_for_user(user2)

        response = self.__get_response_for_profile(profile)

        self.assertListEqual(
            [car],
            response.context['cars'],
        )



