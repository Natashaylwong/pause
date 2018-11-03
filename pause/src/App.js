import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Webcam from "react-webcam";
import { Wave, Random } from 'react-animated-text';
import hour from './hour.svg';

const ExampleOne = () => (
  <Wave text="EXAMPLE TEXT" />
);

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={hour} className="App-logo" alt="logo"/>
        </header>
        <body className = "App-body">
          <div style={{marginTop: 50}}>
            <Wave text="P A U S E" effect="fadeOut" effectChange={10.0} effectDelay={5.0} />
          </div>
          <div style={{marginTop: 100, marginBottom: 50}}>
            <Webcam />
          </div>
        </body>
      </div>
    );
  }
}

export default App;
