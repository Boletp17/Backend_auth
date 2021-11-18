from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, repassword=None): #Cuando se usa un SELF en una funcion, esta se convierte en un metodo de una clase
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if password == repassword:    
            user = self.model(username=username)#el model viene de BaseUserManager y la variable username pertenese a ese model(constructor)
            user.set_password(password)
            user.save(usign=self._db)#guarda en las bases de datos configuradas en el proyecto
            return user

class User(AbstractBaseUser, PermissionsMixin):#Se hace herencia de los models seleccionados
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    cedula = models.CharField('id', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=100, unique=True)
    phone = models.CharField('Telefono', max_length=10)
    password = models.CharField('Password', max_length=256)
    repassword = models.CharField('RePassword', max_length=256)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)#Se encripta la password
        super().save(**kwargs)#Guarda la contraseña encriptada

    objects = UserManager()
    USERNAME_FIELD = 'email'