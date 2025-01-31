FROM node:16.14-alpine

WORKDIR /app

COPY package*.json ./

# Install dependencies in a specific order
RUN npm install watchpack-chokidar2 && \
    npm install chokidar && \
    npm install --legacy-peer-deps

COPY . .

EXPOSE 3000

# Start the application
CMD ["npm", "start"] 