import React from 'react'
import { Container } from 'react-bootstrap'
import { AuthProvider } from '../contexts/AuthContext'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
// After adding new component/pages, add import statement below to use them
import Signup from './Signup'
import Dashboard from './Dashboard'
import Login from './Login'
import PrivateRoute from './PrivateRoute'
import ForgotPassword from './ForgotPassword'
import UpdateProfile from './UpdateProfile'

function App() {
  return (

    <Container
      className="d-flex align-items-center justify-content-center"
      style={{ minHeight: "100vh" }}
    >
      <div className="w-100" style={{ maxWidth: "400px" }}>
        <Router>
          <AuthProvider>
             
             {/*
               add new routes here to add different pages to the website

               and import it as seen by the comment indicated above
             */} 
             <Routes>

              
              {/* 
                private routing needs to be wrapped, else error
              */}
              <Route exact path="/" 
                      element={ <PrivateRoute>
                        <Dashboard/>
                      </PrivateRoute>}
              />
              <Route path="/update-profile" 
                      element={ <PrivateRoute>
                        <UpdateProfile/>
                      </PrivateRoute>}
              />
              <Route path="/signup" element={ <Signup/> }/>
              <Route path="/login" element={ <Login/> }/>
              <Route path="/pw-recovery" element={ <ForgotPassword/> }/>
            </Routes>
          </AuthProvider>
        </Router>
      </div>
    </Container>
  )
}

export default App;
