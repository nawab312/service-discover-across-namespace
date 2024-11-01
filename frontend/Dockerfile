# frontend/Dockerfile
FROM node:14

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy application code
COPY app.js .

EXPOSE 80
CMD ["node", "app.js"]

