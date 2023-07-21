import React, { useEffect, useState, useRef } from 'react';
import { ColorType, createChart } from 'lightweight-charts';


function Third(props) {
  const chartContainerRef = useRef();
  const [products, setProducts] = useState();

  console.log(props.name);

  useEffect(() => {
    const getProducts = async () => {
      const response = await fetch(`http://localhost:80/getSample/name/${props.name}`);
      const data = await response.json();
      setProducts(data);
    };
    getProducts();
  }, [props.name]);

  useEffect(() => {
    if (products && products.length > 0) {
      // Filter out any invalid data that does not have the 'year' property
      const validData = products.filter(item => item.tradeDate !== undefined && item.tradeDate !== null);
  
      const initialData = validData.map(item => {
       
        const parts = item.tradeDate.split('-');
        const year = parts[2];
        const month = parts[1];
        const day = parts[0];
        const formattedDate = `${year}-${month}-${day}`;
  
        return {
          time: formattedDate, // Make sure 'time' is the correct property name, adjust if needed
          open: item.open,
          high: item.high,
          low: item.low,
          close: item.close,
        };
      });

      const chart = createChart(chartContainerRef.current, {
        layout: {
          background: { type: ColorType.Solid, color: "rgb(242,242,242,1)" },
          textColor: 'green',
        },
        width: 500,
        height: 100,
      });

      const newSeries = chart.addCandlestickSeries({
        topColor: '#2962FF',
        bottomColor: 'rgba(41,98,255,0.28)',
      });

      newSeries.setData(initialData);

      return () => chart.remove();
    }
  }, [products]);

  return <div style={{ background: 'transparent' }} ref={chartContainerRef}></div>;
}

export default Third;
