from django.contrib.auth.models import User

class UserHelper:
    def validate_data(self,request):
        errors = {}

        if 'username' in request.data and request.data['username'] == '':
            errors['username'] =  'Username should not be empty'

        if 'email' in request.data and request.data['email'] == '':
            errors['email'] =  'Email should not be empty'

        if 'password' in request.data and request.data['password'] == '':
            errors['password'] =  'Password should not be empty'

        ############## Check if Existing ####################
        if request.data['username'] and User.objects.filter(username=request.data["username"]).count() != 0:
            errors['username'] = 'Username is already used'

        if request.data['email'] and User.objects.filter(email=request.data["email"]).count() != 0:
            errors['email'] = 'Email has already been used'

        return errors
    
    def validate_user(self,request):
        errors = {}

        if request.user.is_anonymous:
            errors['user'] = 'User is not logged in'
            return errors