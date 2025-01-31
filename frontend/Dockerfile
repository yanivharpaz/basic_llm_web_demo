FROM node:16.14-alpine

WORKDIR /app

COPY package*.json ./

# Clean install with specific flags
RUN npm install --legacy-peer-deps --no-optional

COPY . .

EXPOSE 3000

CMD ["npm", "start"] 