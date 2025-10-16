import React from 'react';
import { Bar } from 'react-chartjs-2';

function FeatureChart({ result }) {
  if (!result) return null;

  const data = {
    labels: result.top_features.map(f => f.name),
    datasets: [{
      label: 'Feature Weight',
      data: result.top_features.map(f => f.weight),
      backgroundColor: 'rgba(75, 192, 192, 0.6)',
    }]
  };

  return (
    <div style={{ width: '400px', margin: 'auto' }}>
      <Bar data={data} />
    </div>
  );
}

export default FeatureChart;