import React from 'react'
import { Link } from 'react-router-dom'

function FirstNav() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <Link className="nav-link active navbar-brand" to="/">Home</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div className="navbar-nav">
        <Link className="nav-link active" aria-current="page" to="/dash">Dashboard</Link>
        
      </div>
      <div className="navbar-nav">
        <Link className="nav-link active" aria-current="page" to="/real">Real Time Chart</Link>
        
      </div>
    </div>
  </div>
</nav>
    </div>
  )
}

export default FirstNav
