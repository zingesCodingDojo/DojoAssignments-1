# -*- text -*-

Assignment: Landing Page

Create a flask project capable of handling the following routes.
- localhost:5000/
  - This route should serve a view file called "index.html"
    and display a greeting. This will be considered our 'root route'.
- localhost:5000/ninjas
  - This route should serve a view file called "ninjas.html"
    and display information about ninjas.
- localhost:5000/dojos/new
  - This route should serve a view file called "dojos.html"
    and have a form.
  - Don't worry where the form should be sent to for now,
    you can simply set your action blank, like: action=''

Next Steps
Create a folder inside of your project labeled static.
This static folder will be used to serve all of our static content, such as stylesheets, images, and javascript files!
Now place a stylesheet in the static folder and referencing it in our view files (templates).
