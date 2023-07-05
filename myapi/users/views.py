from django.http import JsonResponse
from django.db.models import Q
from users.models import User
import requests

def user_search(request):
    first_name = request.GET.get('first_name')

    # Search for users in the local database
    users = User.objects.filter(first_name__istartswith=first_name)

    if users:
        # Users found in the local database, return them as JSON response
        data = {'users': list(users.values())}
        return JsonResponse(data)
    else:
        # Call the dummyjson.com API and save the resulting users to the database
        url = f'https://dummyjson.com/users/search?q={first_name}'
        response = requests.get(url)
        json_data = response.json()

        for user_data in json_data:
            user = User(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                age=user_data['age'],
                gender=user_data['gender'],
                email=user_data['email'],
                phone=user_data['phone'],
                birth_date=user_data['birth_date']
            )
            user.save()

        # Return the newly added users as JSON response
        data = {'users': json_data}
        return JsonResponse(data)
