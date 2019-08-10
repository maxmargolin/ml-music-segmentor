import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\User\\Documents\\skipper.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://skipper-63ddb.firebaseio.com/'
})

# Save data
ref = db.reference('/times/')

print(ref.get())
