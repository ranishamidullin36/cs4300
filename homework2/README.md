## Make sure you are in the environment

1. Running the server:
    1. inside the invironment, run this command: python3 manage.py runserver 0.0.0.0:3000
    2. In the browser, type in in the URL: localhost:3000
        • in the movies main page, you can select any movie that is currently available 
        • choose a seat that is currently available to reserve a seat, then click on the "Book Seat" or "Back to Movies" to return to the movie selection page
        • in the "Booking History" tab, you can view all your booked movies history

2. managing and/or adding more movies and seats
    1. Make sure you have an superuser setup
    2. Type into the URL: localhost:3000/admin
    3. login with the superuser acoount (admin)
    4. click on "add" next to "Movies" or "Seats" to add movies or seats respectfully
        • for movies, fill out all the boxes and when done, click "SAVE" or "Save and add another" to continue to add more movies.
        • for seats, select the movie and type the seat number to add the seat to the movie.
    5. by pressing the actual button "Bookings," "Movies," and "Seats," you can edit or delete any of the items inside.
        • to delete, select a box(s), and in the "Action:" area on top, select "Delete selected [items]" then press "Go", and select "Yes, I'm sure"


3. Running tests:
    1. go to movie_theater_booking directory.
    2. run this command for testing: python manage.py test





## AI Disclosure

AI tools (GitHub Copilot) were used to assist with code generation, debugging, and writing tests for this project.