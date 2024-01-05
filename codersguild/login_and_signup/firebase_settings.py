
# Import Firebase REST API library
import pyrebase


# Firebase configuration

firebase_config={
  "apiKey": "AIzaSyBU1NjGLLYywNErl5pcNFxRzi6pC2mcguA",

  "authDomain": "codersguild13.firebaseapp.com",

  "projectId": "codersguild13",

  "storageBucket": "codersguild13.appspot.com",

  "messagingSenderId": "955174174447",

  "appId": "1:955174174447:web:fe9699b60eac51da26e51a",

  "measurementId": "G-4S9578RXTX",
  "databaseURL" : ""

}
firebase=pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
