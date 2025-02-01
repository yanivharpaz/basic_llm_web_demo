import React from 'react';
import Chat from './components/Chat';
import './App.css';

function App() {
  const title = "[Innovation][hub][Israel][Demo]";
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          {title.split('').map((char, index) => (
            <span key={index} className="title-char">
              {char}
            </span>
          ))}
        </h1>
      </header>
      <main>
        <Chat />
      </main>
    </div>
  );
}

export default App;
