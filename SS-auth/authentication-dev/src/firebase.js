 import firebase from 'firebase/compat/app';
 import 'firebase/compat/auth';

 const app = firebase.initializeApp({
   apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
   authDomain: process.env.REACT_APP_FIREBASE_authDomain,
   projectId: process.env.REACT_APP_FIREBASE_projectId,
   storageBucket: process.env.REACT_APP_FIREBASE_storageBucket,
   messagingSenderId: process.env.REACT_APP_FIREBASE_messagingSenderID,
   appId: process.env.REACT_APP_FIREBASE_appId,
   measurementId: process.env.REACT_APP_measurementID
 })

 export const auth = app.auth()
 export default app

/*
REACT_APP_FIREBASE_API_KEY = AIzaSyA90UDE3JwCx4aLQk4mlyFgDUx-PwcXxRs
REACT_APP_FIREBASE_authDoman = stocksim-dev.firebaseapp.com
REACT_APP_FIREBASE_projectId = stocksim-dev
REACT_APP_FIREBASE_stroageBucket = stocksim-dev.appspot.com
REACT_APP_FIREBASE_messagingSenderID = 714581849158
REACT_APP_FIREBASE_appId = 1:714581849158:web:ab09a0648703c0f01f0647
REACT_APP_FIREBASE_measurementID = G-JSG6SXW8YC
 */