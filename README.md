<h1 align="center">NFT Social Hub Django Rest Framework API - Project Portfolio 5</h1>

![GitHub last commit](https://img.shields.io/github/last-commit/bodthegod/thebod-drf-api?color=blue&style=for-the-badge)

![GitHub contributors](https://img.shields.io/github/contributors/bodthegod/thebod-drf-api?color=green&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/bodthegod/thebod-drf-api?color=orange&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/bodthegod/thebod-drf-api?color=brown&style=for-the-badge)
## - By Christopher Faherty

### [View the live project here](https://ci-nft-social-hub.herokuapp.com/) #
### [View the deployed API here](http://ci-nft-social-hub-api.herokuapp.com/) #
### [View the API repository here](https://github.com/Chrisfaherty/ci-nft-social-hub-api) #


# Table of Contents:
1. [User Stories](#user-stories)
2. [Database Model Structure](#database-model-structure)
3. [Languages and Technologies Used](#languages-used)
4. [Testing](#testing)
    - [Validation](#validation)
5. [Bugs and fixes](#known-bugs)
6. [Credits](#credits)


## User Stories

From the backend perspective of this API, the user stories are CRUD focused and authentication focused.
1. As an admin, I want create functionality of all profiles, posts, likes, comments and subscriptions.
2. As an admin, I want update functionality of all profiles, posts, likes and comments so that I can edit any content I choose to.
3. As an admin, I want delete functionality of all profiles, posts, likes and comments so that I can delete any content that may be deemed as harmful.

## Database Model Structure

<img src="">

### Profile Model

- This model is directly linked in a one to one relationship with the User model, imported from django-allauth.
- The Profile model contains all fields that are associated with a profile when a user creates one. These fields are as such:
1. owner = OneToOne with User field
2. created_at = DateTimeField
3. updated_at = DateTimeField
4. name = CharField
5. content = TextField
6. image = ImageField with default profile image

### User Model

- This model is imported from django-allauth, and is integrated within all functional model classes.
- The User model contains multiple fields associated with all foreign models within my app:
1. Profile model = owner field holds OneToOne relationship with User
2. Posts model = owner field holds ForeignKey relationship with User
3. Likes model = owner field holds ForeignKey relationship with User
4. Followers model = owner & followed fields hold ForeignKey relationship with User which are related to following & followed
5. Comments model = owner field holds ForeignKey relationship with User

### Post Model

- The Post model contains all fields that are associated with a post when a logged in user creates one. These fields are as such:
1. owner = ForeignKey with User field
2. created_at = DateTimeField
3. updated_at = DateTimeField
4. title = CharField
5. category = CharField
6. content = TextField
7. image = ImageField with default post image
8. website = URLField
9. social = URLField
10. marketplace = URLField 

### Follower Model

- The Follower model contains all fields that are associated when a logged in user attempts to follow another profile, as such:
1. owner = ForeignKey with User field
2. followed = ForeignKey between User field and followed field
3. created_at = DateTimeField

### Like Model

- The Like model contains all fields that are associated when a logged in user attempts to like a created post, as such:
1. owner = ForeignKey with User field
2. post = ForeignKey between Post model field and likes field
3. created_at = DateTimeField

### DisLike Model

- The DisLike model contains all fields that are associated when a logged in user attempts to dislike a created post, as such:
1. owner = ForeignKey with User field
2. post = ForeignKey between Post model field and likes field
3. created_at = DateTimeField

### Comment Model

- The Comment model contains multiple fields associated with content related to comments, as such:
1. owner = owner field holds ForeignKey relationship with User model
2. post = post field holds ForeignKey relationship with Post model
3. content = TextField for comment input
4. created_at = DateTimeField
5. updated_at = DateTimeField

### Subscribers Model

- The Subscribers model contains multiple fields associated with content related to subscriptions, as such:
1. fullname = CharField
2. email = EmailField
3. date = DateTimeField

### SubscribersMessage Model

- The SubscribersMessage model contains multiple fields associated with content related to subscription messages, as such:
1. fullname = CharField
2. email = EmailField
3. date = DateTimeField
4. title = CharField
5. message = TestField

## Languages and Technologies Used

- This project was created using the python programming language, 

- The API for this project was created using Django. The batteries included nature of this framework allowed for rapid development of the API.

### Tools Used

- [Gitpod](https://gitpod.io/) my preferred coding environment.
- [GitHub](https://github.com/) to store my code repositories.
- [Git](https://git-scm.com/) was used to commit and push the code changes.
- [Heroku](https://dashboard.heroku.com/apps) used to host the  repositories and deploy the API.
- [Django Rest Framework](https://www.django-rest-framework.org/) was used in many instances to add features to the API.
- [Django API Testing](https://www.django-rest-framework.org/api-guide/testing/) was used to create tests and run them to test the API.
- [Cloudinary](https://cloudinary.com/) was used to store the static files.
- [PostgreSQL](https://www.postgresql.org/) was used to store the data inside my relational database.
- [Pillow](https://python-pillow.org/) was used for image input validation (resolution and dimension filtering).
- [Psycopg2](https://pypi.org/project/psycopg2/) database adapter for Python.

## Testing

## Testing

### Manual testing

A series of manual tests were carried out for each end point using the Django Rest Framework HTML interface running on the local server and using the deployed database. Please see the separate [testing.md]() document for details.

All the features of the deployed API were tested as part of testing/acceptance criteria for each of the React frontend user stories. These tests are documented in the [read-me]() for that project.

Testing on the frontend revealed a number of bugs which had not been detected while testing the API in isolation, and led to the implementation of several additional features for consumption by the React app. The bugs are detailed in the bugs section below, and the following additional features were added as a result of front-end testing:

- T
- U
- T
- P
- A
- A
- A

### Automated tests


- Test 
- Test
- Test
- Test
- Test


### Python validation

Code errors and style issues were detected using the Pylance linter in VSCode, and immediately fixed throughout development.
All files containing custom Python code were then validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/):

- `contacts/admin.py`: no errors found
- `contacts/models.py`: no errors found
- `contacts/tests.py`: no errors found
- `contacts/serializers.py`: no errors found
- `contacts/urls.py`: no errors found
- `contacts/views.py`: no errors found

- `profiles/admin.py`: no errors found
- `profiles/models.py`: no errors found
- `profiles/serializers.py`: no errors found
- `profiles/urls.py`: no errors found
- `profiles/views.py`: no errors found  


### Resolved bugs

#### Bugs found while testing the API in isolation
- D
- T
- T


#### Bugs found while testing the React front-end
- W
- A
- A
- D
- T
- F
- A
- F 

### Unresolved bugs
- T


## Deployment
The NFT Social Hub API is deployed to Heroku, using an ElephantSQL Postgres database.
To duplicate deployment to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user profile images.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Login to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Name the 'plan' and select the 'Tiny Turtle (free)' plan.
- Select 'select region'.
- Choose the nearest data centre to your location.
- Click 'Review'.
- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
- Copy the ElephantSQL database URL to your clipboard (this starts with `postgres://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your ElephantSQL postgres database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
    - `ALLOWED_HOST`: *the url of your Heroku app (but without the `https://` prefix)*
- Select the 'Deploy' tab at the top.
- Select 'GitHub' from the deployment options and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed API to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your API will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits
- T [Cloudinary](),
- A [StackOverflow article](),


In addition, the following documentation was extensively referenced throughout development:

- [Django documentation](https://www.djangoproject.com)
- [Django Rest Framework documentation](https://www.django-rest-framework.org)
- [django-filter documentation](https://django-filter.readthedocs.io/en/stable/)
- [django-recurrence documentation](https://django-recurrence.readthedocs.io/en/latest/)
- [Python datetime documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil documentation](https://dateutil.readthedocs.io/en/stable/index.html)