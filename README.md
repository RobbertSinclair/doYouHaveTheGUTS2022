# Running Instructions

Create a key for this to work. Change your directory to backend and run `python generate_key.py` on windows or `python3 generate_key.py` if on Mac/Linux. Finally you can run the server by writing `python manage.py runserver`

# Google Key

In order to run an API key go to the google cloud api and get your key, then create a file called "google_key.js" and then write the following code

```javascript
export default API_KEY = "YOUR_API_KEY";
```

# In case of current git clones

Models currently have some dependencies and it is currently easiest to create a superuser, then build UserProfiles, Events, then User event bridge to successfully navigate the website.
