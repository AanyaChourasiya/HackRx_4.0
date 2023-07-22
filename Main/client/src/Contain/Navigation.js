import React, { useEffect, useState } from 'react'


function Navigation() {

  const [products, setProducts] = useState();

  useEffect(() => {
    const getProducts = async () => {
      const response = await fetch(
        'http://localhost:80/getSample/28-06-2023'
      );
      const data = await response.json();
      setProducts(data);
    };
    getProducts();
  }, []);

  console.log(products);

  return (
    <>
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    {/* <a className="navbar-brand" href="#">Navbar</a> */}
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="molo nav-link active" aria-current="page" target='blank' href="https://www.moneycontrol.com/india/stockpricequote/finance-nbfc/bajajfinance/BAF"><strong>NIFTY 50</strong></a>
        </li>
        <div className="Success">
        <li className="nav-item">
          <a className=" colo nav-link " href="#">19,745.00</a>
        </li>
        </div>
        <li className="nav-item">
          <a className="nav-link rolo  " href="#">-234.15(1.17%) </a>
        </li>
        
        <li className="nav-item">
          <a className="molo nav-link active" aria-current="page" target='blank' href="https://www.moneycontrol.com/india/stockpricequote/finance-nbfc/bajajfinance/BAF"> <strong>SENSEX</strong> </a>
        </li>
        <div className="Success">
        <li className="nav-item">
          <a className="colo nav-link " href="#">66,684.26</a>
        </li>
        </div>
        <li className="nav-item rolo ">
          <a className="nav-link " href="#">-887.64(1.31%)</a>
        </li>
       
      </ul>

    </div>
  </div>
</nav>


    </>
  )
}

export default Navigation
