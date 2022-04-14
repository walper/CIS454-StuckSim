import React, { useContext, useState, useEffect } from "react"
import { auth } from '../firebase'

const AuthContext = React.createContext()

//this component provides authentication related services

export function useAuth(){
    return useContext(AuthContext)
}

export function AuthProvider({ children }) {

    const [currentUser, setCurrentUser] = useState()
    const [loading, setLoading] = useState(true)

    // account registration function
    function signup(email, password){    
        return auth.createUserWithEmailAndPassword (email, password)
    }

    // login function
    function login(email, password){    
        return auth.signInWithEmailAndPassword (email, password)
    }

    // logout function
    function logout(){
        return auth.signOut()
    }

    // pw reset function
    function resetPassword(email){
        return auth.sendPasswordResetEmail(email)
    }

    // profile update functions
    // done individually because of how firebase works
    function updateEmail(email){
        currentUser.updateEmail(email)
    }
    function updatePassword(password){
        currentUser.updatePassword(password)
    }

    useEffect(() => {
        
        const unsubscribe = auth.onAuthStateChanged(user => {
            setCurrentUser(user)
            setLoading(false)
        })

        return unsubscribe
   
    }, [])

    const value = {
        currentUser,
        login,
        signup,
        logout,
        resetPassword,
        updateEmail,
        updatePassword
    }

    return (
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>
      )
}

