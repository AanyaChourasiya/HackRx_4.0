import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

const CandlestickGraphComponent = ({ selectedCompany }) => {
  const [companyData, setCompanyData] = useState([]);

  // Fetch candlestick data for the selected company from the API
  const fetchData = async (symbol) => {
    try {
      const response = await axios.get(`http://localhost:80/getSample?symbol=${symbol}`);
      const data = response.data;
      return data.slice(0, 57); // Take the first 57 data points for the selected company
    } catch (error) {
      console.error('Error fetching data:', error);
      return [];
    }
  };

  // Update the candlestick graph with new data when the selected company changes
  useEffect(() => {
    if (selectedCompany) {
      fetchData(selectedCompany).then((data) => {
        setCompanyData(data);
      });
    }
  }, [selectedCompany]);

  // Update the candlestick graph with new data
  const layout = {
    xaxis: {
      type: 'category',
      tickangle: -45,
    },
    yaxis: {
      title: 'Price',
    },
  };

  return (
    <div>
      {selectedCompany && (
        <Plot
          data={[
            {
              x: companyData.map((data) => data.tradeDate),
              open: companyData.map((data) => data.open),
              high: companyData.map((data) => data.high),
              low: companyData.map((data) => data.low),
              close: companyData.map((data) => data.close),
              type: 'candlestick',
              increasing: { line: { color: 'green' } },
              decreasing: { line: { color: 'red' } },
            },
          ]}
          layout={layout}
          style={{ width: '90%', height: '500px' }}
        />
      )}
    </div>
  );
};

const CandlestickGraph = () => {
  const [companyNames, setCompanyNames] = useState([]);
  const [selectedCompany, setSelectedCompany] = useState('');

  // Fetch all unique company names from the API
  const fetchCompanyNames = async () => {
    try {
      const response = await axios.get('http://localhost:80/getSample');
      const data = response.data;
      const uniqueCompanyNames = [...new Set(data.map((item) => item.symbol))];
      setCompanyNames(uniqueCompanyNames);
    } catch (error) {
      console.error('Error fetching company names:', error);
    }
  };

  // Fetch data for the selected company and company names on component mount
  useEffect(() => {
    fetchCompanyNames();
  }, []);

  return (
    <div>
      {/* Dropdown for company selection */}
      <select
        style={{ borderRadius: '6px', border: '2px solid black' }}
        className='py-1 px-1 '
        value={selectedCompany}
        onChange={(e) => setSelectedCompany(e.target.value)}
      >
        <option value=''>Select a Company</option>
        {companyNames.map((companyName) => (
          <option key={companyName} value={companyName}>
            {companyName}
          </option>
        ))}
      </select>

      {selectedCompany && <CandlestickGraphComponent selectedCompany={selectedCompany} />}
    </div>
  );
};

export default CandlestickGraph;
