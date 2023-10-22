# internship-api
# 1- clone the project
git clone https://github.com/sadekOmrane/internship-api.git
# 2- enter directory 
cd internship-api
# 3- activate envirenements
source venv/bin/activate
# 4- install required packages
pip install -r requirements.txt
# 5- enter project directory
cd backend
# 6- make migrations
python manage.py makemigrations
python manage.py migrate
# 7- run server
python manage.py runserver
