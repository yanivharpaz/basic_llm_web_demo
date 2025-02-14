FROM node:16.14-alpine as builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
# RUN npm install --legacy-peer-deps
RUN npm install --legacy-peer-deps && \
    npm install --save-dev @babel/core@latest


# Copy source files
COPY . .

# Build the application
RUN npm run build

# Production environment
FROM nginx:alpine

# Copy built assets from builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Add nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"] 