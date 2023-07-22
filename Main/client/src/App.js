import './App.css';
// import CandlestickGraph from './Contain/CandlestickGraph';
import Dashboard from './Contain/Dashboard';
// import Dashboard from './Contain/Dashboard';
import First from './Contain/First';
import FirstNav from './Contain/FirstNav';
import Navigation from './Contain/Navigation';
import {
  BrowserRouter as Router,
  Routes,
  Route
}
  from 'react-router-dom';


function App() {
  return (
    <div className="App">
      
     <Router>
       <Navigation/>
       <FirstNav/>
         <Routes>
           <Route path="/" element={<First />} />
           <Route path="/dash" element={ <Dashboard/> } />
           <Route path="/dash" element={ <RealTime/> } />
         </Routes>
       </Router>
    
      
    </div>
  );
}

export default App;
