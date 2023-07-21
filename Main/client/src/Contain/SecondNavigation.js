import React from 'react'
import FirstNav from './FirstNav'
import {BrowserRouter as Router,Route,Link, Routes} from 'react-router-dom'
import First from './First'

function SecondNavigation() {
  return (
    <div>
       <Router>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <Link className="navbar-brand" to="Navbar" >Navbar</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div className="navbar-nav">
      <Link className="navbar-brand" to="Navbar" >bar</Link>
        
      </div>
    </div>
  </div>
</nav>
<Routes exact path="/" Component={First} />
<Routes path="/about" Component={FirstNav} />
</Router> 
    </div>
  )
}

export default SecondNavigation






