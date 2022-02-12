# Running Instructions

First go into the frontend directory and run dependencies using `npm install`

Once you have this installed build the frontend by typing in the command `npm run build`

Your frontend should be fully build now. Now you must create a key for this to work. Change your directory to backend and run `python generate_key.py` on windows or `python3 generate_key.py` if on Mac/Linux. Finally you can run the server by writing `python manage.py runserver`

# Google Key

In order to run an API key go to the google cloud api and get your key, then create a file called "google_key.js" and then write the following code

```javascript
export default API_KEY = "YOUR_API_KEY";
```