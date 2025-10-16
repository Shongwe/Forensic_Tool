import React, { useState } from 'react';
import axios from 'axios';

function UploadForm({ onResult }) {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    try {
      const res = await axios.post('http://localhost:5000/predict', formData);
      onResult(res.data);
    } catch (err) {
      console.error('Prediction failed:', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button type="submit">Analyze Image</button>
    </form>
  );
}

export default UploadForm;