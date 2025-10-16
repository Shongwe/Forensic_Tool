import React from 'react';

function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div className="result-card">
      <h2>Prediction: {result.label}</h2>
      <p>Confidence: {result.confidence.toFixed(2)}%</p>
      <h4>Top Contributing Features:</h4>
      <ul>
        {result.top_features.map((f, i) => (
          <li key={i}>{f.name}: {f.weight.toFixed(3)}</li>
        ))}
      </ul>
    </div>
  );
}

export default ResultCard;