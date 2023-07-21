import './App.css';
import Dashboard from './Contain/Dashboard';
import First from './Contain/First';
import FirstNav from './Contain/FirstNav';
import Navigation from './Contain/Navigation';

function App() {
  return (
    <div className="App">
      <Navigation/>
      <FirstNav/>
      
      <First/>

      <Dashboard/>
      
    </div>
  );
}

export default App;
