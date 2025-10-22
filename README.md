# IY4103 Example Flask App

### Database

To run the initial migration:

flask db init
flask db migrate -m "Create users, places, comments, likes"
flask db upgrade

This is a useful website for debugging your database. You can see the contents, perform basic CRUD operations on it without fear of breaking your website database. 

https://inloop.github.io/sqlite-viewer/