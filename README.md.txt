## Amadeo's Miotto Blog!
### Instructions
**Clone the project and change branch**

`git clone https://github.com/1507amadeo/amadeo_miotto_blog.git

cd Entrega_Final_Arcenilla_Miotto
`cd Entrega_Final_Arcenilla_Miotto`

**Install text editor**

`pip install django-ckeditor`

**Create and activate  virtual environment(Windows)**

`C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat`

**Create and activate  virtual environment (Linux)**

`python3 -m venv venv
source venv/bin/activate`

**Create and activate  virtual environment (Linux)**

`export SECRET_KEY='4e8&y0ygfox1cg7f3owcku9$hv_(nu7t3ku$p637-+!so2jlvs'
export DEBUG='True'
export ALLOWED_HOSTS='*,'`

**or create the file Entrega_Final_Arcenilla_Miotto/.env with the following content**

`SECRET_KEY=4e8&y0ygfox1cg7f3owcku9$hv_(nu7t3ku$p637-+!so2jlvs
DEBUG=True
ALLOWED_HOSTS=*,`

**Install project's dependencies**

`pip install -r requirements.txt`

**Create data base from migrations**

`python manage.py migrate`

**Crearte super-user**
 
`python manage.py createsuperuser`

The options to add publications is available for Superuser's profiles, editors or admins(The Reader profile is the default whenever an user is registered) 
if you are the superuser or the user who created the publications editing the publication is going to be availabe as well as adding an image to it and/or delete it. if not , checking the details of the publications and leaving a comment are the options available.

**Execute Project**

`python manage.py runserver`

On the github repository you can find a video on how to run the project, thank you for taking your time to at least taking a look at my project and considering it as a the gate for more challening projects to come.
