import React, { useState } from "react";
import { uploadAudio } from "../services/API";

const AudioInput = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [outputData, setOutputData] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = async () => {
    if (!selectedFile) {
      setError("Please select an audio file");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await uploadAudio(selectedFile);
      setOutputData(response); // Assuming your API response has data
    } catch (error) {
      setError(error.message || "Error processing audio");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <div className="container">
        <div className="left-container">
          <p>
            Currently, we are utilising Deepgram API for transcription <br />
            and OpenAI API for Psychological Insights.
          </p>
          
        </div>
        <div className="right-container">
          <div className="input-file">
            <input
              type="file"
              accept="audio/*"
              id="uploadFile"
              onChange={handleFileChange}
            />
            <label className="label" htmlFor="uploadFile">
              <i className="fa-solid fa-upload"></i>Upload File
            </label>
            <p
              style={
                selectedFile
                  ? { visibility: "visible" }
                  : { visibility: "hidden" }
              }
            >
              File Selected
            </p>
          </div>

          {selectedFile && (
            <button
              type="button"
              className="label"
              onClick={handleSubmit}
              disabled={isLoading}
            >
              {isLoading ? "Processing..." : "Submit "}
            </button>
          )}
        </div>
      </div>

      {isLoading && (
        <>
          <img src="gif.gif" alt="Loading gif" style={{ marginTop: "80px" }} />
          <p>Hang on tightly... AI is on doing its job</p>
        </>
      )}

      {error && (
        <>
          <div className="output-container">
            <p style={{ color: "red" }}>Error: {error} the data from backend</p>
          </div>
        </>
      )}

      {!isLoading && (
        <div className="output-container">
          {outputData && (
            <>
              <div className="deepgram">
                <h3>Conversation</h3>
                {outputData.conversation.split("\n").map((line, index) => (
                  <p key={index}>{line}</p>
                ))}
              </div>
              <div className="openAI">
                <h3>Insights</h3>
                {outputData.insights.map((part, index) => (
                  <div key={index}>
                    {part.map((line, i) => (
                      <p key={line}>{line}</p>
                    ))}
                  </div>
                ))}
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default AudioInput;
