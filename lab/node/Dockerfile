FROM node:14-alpine

WORKDIR /app

# Copy package files first
COPY app/package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY app/ ./

# Expose port
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]