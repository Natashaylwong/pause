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
  setRef = webcam => {
    this.webcam = webcam;
  };

  capture = () => {
    const imageSrc = this.webcam.getScreenshot();
  };
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
          <Webcam
            audio={false}
            ref={this.setRef}
            screenshotFormat="image/jpeg"
          />
          <div>
            <button onClick={this.capture}>Capture photo</button>
          </div>
          </div>
        </body>
      </div>
    );
  }
}

export default App;
