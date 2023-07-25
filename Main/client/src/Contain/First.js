import React, { useEffect, useState } from 'react'
import Second from './Second';
import Third from './Third';

function First() {
    
    const [products,setProducts] = useState();
    
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
    <div>
    {products ? (
      products.map((product) => (
        <div key={product.id}>
           <table style={{textAlign:"center"}} className=' .table-striped table table-striped'   >
      <tbody >
      <tr style={{ borderRadius:"23px", background:"transparent"}} >
    <th scope="row" style={{background:"transparent"}}  className='width-auto'  >
          <h2 style={{ fontFamily: "Piazzolla",display:"flex",margin:"none",padding:"none" ,textAlign:"justify",justifyContent:"left"}} className='text-center monu Success my-4 mx-3' >{ product.symbol}</h2>   
    </th>
    <th scope="row" style={{background:"transparent"}} className='width-auto' >
        <Third name={product.symbol}/>
    </th>
    <th scope="row" style={{background:"transparent"}} className='width-auto'>
          <Second high={product.high} volume = {product.volume}/>
    </th>
  </tr> 
        </tbody>
        </table>
        </div>
      ))
      ) : (
        <h1>Loading...</h1>
        )}
        
  </div>
</>
  )
}

export default First