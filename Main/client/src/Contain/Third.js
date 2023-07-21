import React, { useEffect, useState } from 'react'
import {ColorType,createChart } from 'lightweight-charts'
function Third(props) {

    const chartContainerRef = useRef();
    const[products,setProducts] = useState();

    console.log(props.name);

    useEffect(()=>{
        const getProducts = async ()=>{
            const response = await fetch(`http://localhost:80/getSample/name${props.name}`);
            const data = await response.json();
            setProducts(data);
        };
        getProducts();
    },[props.name]);

    useEffect(()=>{
        if(products && products.length > 0){
            const validData = products.filter(item => item.tradeDate !== undefined && item.tradeDate !== null);

            const initialData = validData.map(item => {
                const parts = items.tradeDate.split
            })
        }
    })

  return (
    <div>
      
    </div>
  )
}

export default Third
