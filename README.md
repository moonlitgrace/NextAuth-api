## NextAuth - a secure and powerful authentication system
NextAuth is using httpOnly cookies for authentication, so this is more secure than authentication with localStorage <br />
It has Google and Github social authentication too... And it comes with awesome UI ...

### Major packages used
[django](https://www.djangoproject.com/) - for backend <br />
[dj-rest-auth](https://github.com/iMerica/dj-rest-auth) - for Simple JWT authentication with httpOnly cookies <br />
[django-allauth](https://github.com/pennersr/django-allauth) - for social authentication <br />
[djangorestframework](https://github.com/encode/django-rest-framework) - for making Rest Api's <br />
[djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) - for making JWT token based authentication <br />

> Checkout the frontend for this [NextAuth-frontend](https://github.com/suneethsunx/NextAuth-frontend)

## Getting Started
Clone this repo and `cd <repo name>/` <br />
First, install the required packages( recommended in virtual env ):

```bash
pip install -r requirements.txt
```
Then start development server by:
```bash
python manage.py runserver
# or
python3 manage.py runserver
# or
./manage.py runserver
```
Server will be run in `http://localhost:8000`

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result. <br />
That's all, you can modify this backend and feel free make a pull request


## Deployed on Render

This backend is deployed on render, yeah it's live ! <br />
[https://nextauth-backend.onrender.com](https://nextauth-backend.onrender.com) <br />
> It feels slow, because it was on free plan !
