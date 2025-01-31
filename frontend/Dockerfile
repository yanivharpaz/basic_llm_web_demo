FROM node:16.14-alpine

WORKDIR /app

# Install chokidar globally
RUN npm install -g chokidar

COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

COPY . .

EXPOSE 3000

# Start the application
CMD ["npm", "start"] 