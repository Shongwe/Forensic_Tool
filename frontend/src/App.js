import React, { useState } from 'react';
import './App.css';
import UploadForm from './components/UploadForm';
import ResultCard from './components/ResultCard';
import FeatureChart from './components/FeatureChart';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div>
      <h1>AI Fingerprint Detector</h1>
      <UploadForm onResult={setResult} />
      <ResultCard result={result} />
          <div className="chart-container">
      <FeatureChart result={result} />
</div>

    </div>
  );
}

export default App;


