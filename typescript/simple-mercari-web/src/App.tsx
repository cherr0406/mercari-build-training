import { useState } from 'react';
import './App.css';
import { ItemList } from './components/ItemList';
import { Listing } from './components/Listing';

function App() {
  // reload ItemList after Listing complete
  const [reload, setReload] = useState(true);
  return (
    <div className="App">
      <header className="Title">
        <h1>Simple Mercari</h1>
      </header>
      <main className="Main">
        <Listing onListingCompleted={() => setReload(true)} />
        <ItemList reload={reload} onLoadCompleted={() => setReload(false)} />
      </main>
    </div>
  );
}

export default App;
