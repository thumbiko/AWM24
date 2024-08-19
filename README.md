# AWM24
App where users can search and find local car meets with time and details, they have an option of saving to favourites list.
The application features user registration and login, a location search tool with interactive maps, and comprehensive geographic coverage of towns and cities in Ireland using Leaflet.js and PostGIS.

## Technologies Used
* Django & GeoDjango: Backend framework with geographic capabilities.
* PostgreSQL with PostGIS: Database with spatial extensions to handle geographic data.
* Leaflet.js: JavaScript library for interactive maps.
* Bootstrap 4: Frontend framework for responsive design.

## Database Setup
The database is configured using PostgreSQL with PostGIS extension enabled. The sample data includes towns and cities from all counties in Ireland, alphabetically ordered for ease of management.

## Sample Data
The included locations represent a wide range of Irish towns and cities, ensuring that users can find meetups in various regions. Each location is precisely mapped with latitude and longitude coordinates.

## How to Run
Install the required dependencies.
Set up the PostgreSQL database with PostGIS extensions.
Run migrations to set up the database schema.
Populate the database with sample locations using the provided management command.
Start the development server and access the application.


## Main Features
* User Authentication: Secure login and registration system using Django's built-in authentication.
* Location Search: Users can search for towns and cities across Ireland to find meetup locations. The app uses OpenStreetMap with Leaflet.js for interactive maps.
* Geospatial Data: Leveraging GeoDjango and PostGIS, the app allows for precise location tracking and querying of geographic data.
* The app includes locations from every county in Ireland, ensuring all major towns and cities are represented.
