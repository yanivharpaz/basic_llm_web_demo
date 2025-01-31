FROM node:16.14-alpine

WORKDIR /app

# Install create-react-app globally
RUN npm install -g create-react-app@4.0.3

# Copy package files
COPY package*.json ./

# Install dependencies with specific flags
RUN npm install --legacy-peer-deps --production=false

COPY . .

EXPOSE 3000

# Start the application
CMD ["npm", "start"] 