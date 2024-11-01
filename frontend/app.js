// frontend/app.js
const express = require('express');
const axios = require('axios');
const app = express();
const BACKEND_URL = process.env.BACKEND_URL || 'http://backend-service.backend.svc.cluster.local:5000';

app.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${BACKEND_URL}/data`);
        res.send(`<h1>Data from Backend: ${response.data.data}</h1>`);
    } catch (error) {
        res.send('<h1>Could not retrieve data from backend.</h1>');
    }
});

const PORT = process.env.PORT || 80;
app.listen(PORT, () => {
    console.log(`Frontend service running on port ${PORT}`);
});

