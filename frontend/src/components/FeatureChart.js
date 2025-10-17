import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

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

  const options = {
    responsive: true,
    scales: {
      x: {
        type: 'category',
        title: {
          display: true,
          text: 'Feature'
        }
      },
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Weight'
        }
      }
    }
  };

  return (
    <div style={{ width: '400px', margin: 'auto' }}>
      <Bar data={data} options={options} />
    </div>
  );
}

export default FeatureChart;