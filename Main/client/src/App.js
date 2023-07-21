import './App.css';
import First from './Contain/First';
import Navigation from './Contain/Navigation';
import SecondNavigation from './Contain/SecondNavigation';

function App() {
  return (
    <div className="App">
      <Navigation/>
      <SecondNavigation/>
      <First/>
    </div>
  );
}

export default App;
