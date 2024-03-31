
import React from "react";
import AudioInput from "./components/AudioInput";
import "./styles/App.css";

function App() {
  return (
    <div className="App">
      <div className="title">
      <div className="brand">
          <img src="logo.webp" alt="logo" />
          <h1>Alindor </h1></div>

        <p>
          This App lets you analyze the <span>'Conversation' </span> along with
          psychological insights.
        </p>
        <hr style={{ width: "50%" }} />
      </div>
      <AudioInput />
    </div>
  );
}

export default App;
