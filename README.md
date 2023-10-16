### LittleLemon Booking and Menu API

#### ⚙️ Environment Setup

After cloning the repository, follow these steps to set up your environment:

1. Change directory to the project folder:
   ```
   cd littlelemon
   ```

2. Activate the virtual environment:
   ```
   pipenv shell
   ```

3. Install the project's dependencies:
   ```
   pipenv install
   ```

#### API Routes

You can access the following API endpoints:

#### Home Route

- Home Page: `/resturant/menu/home`

#### Menu API

- Get all menu items or create a new menu item: `/resturant/menu/menu/`
- Update, delete, or patch a single menu item: `/resturant/menu/menu/pk`

#### Booking API Route

- Booking tables: `/resturant/booking/tables`

#### User Registration and Authentication

- Register a user: `/auth/users/`
- Get the current user: `/auth/users/me`
- Login: `/auth/token/login/`
- Logout: `/auth/token/logout/`
