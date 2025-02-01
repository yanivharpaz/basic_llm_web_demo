# AI Chat Interface with RAG Architecture

## Overview
This project implements a modern AI chat interface using a Retrieval-Augmented Generation (RAG) architecture, combining the power of GPT-4o with local context-aware information retrieval. The system is built using a microservices architecture with Docker, featuring a React frontend and a Flask backend.

## Architecture

### Frontend (React)
- **Technology Stack**:
  - React 17.0.2
  - Material-UI components
  - Modern CSS with blur effects and responsive design
  - Nginx for production serving
  - Docker containerization

- **Key Features**:
  - Real-time chat interface
  - Character-by-character hover animations
  - Context display for transparency
  - Responsive design with glass-morphism effects
  - Auto-focus input after responses
  - Loading states and error handling

### Backend (Flask)
- **Technology Stack**:
  - Flask 2.0+
  - FAISS for vector similarity search
  - Sentence Transformers for embeddings
  - OpenAI GPT-4o integration
  - Docker containerization

- **Key Components**:
  1. **Vector Store**: 
     - Uses FAISS for efficient similarity search
     - Sentence-BERT embeddings (all-MiniLM-L6-v2 model)
     - In-memory storage for quick retrieval

  2. **RAG Implementation**:
     - Context retrieval using vector similarity
     - Dynamic prompt construction
     - Hybrid responses (context + general knowledge)

  3. **API Endpoints**:
     - `/api/chat`: Main chat endpoint with context retrieval
     - `/api/add-text`: Endpoint for adding new context

## RAG Architecture Details

### 1. Document Processing
- Documents are processed into embeddings using Sentence Transformers
- FAISS indexes these embeddings for efficient similarity search
- Support for dynamic context addition through API

### 2. Retrieval Process
- Query embedding generation
- FAISS similarity search
- Top-K results selection
- Context assembly for prompt construction

### 3. Generation Process
- Context-aware prompt construction
- System prompt defines AI behavior and context usage
- Hybrid response generation combining:
  - Retrieved context information
  - Model's general knowledge
  - Dynamic response formatting

## Docker Configuration

### Frontend Container
```dockerfile
FROM node:16.14-alpine as builder
# Build stage for React application
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

FROM nginx:alpine
# Production stage with Nginx
COPY --from=builder /app/build /usr/share/nginx/html
```

### Backend Container
```dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential python3-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

### Network Architecture
- Frontend container (port 3000)
- Backend container (port 5000)
- Inter-container communication via Docker network
- Nginx reverse proxy for production

## Getting Started

### Prerequisites
- Docker and Docker Compose
- OpenAI API key
- At least 4GB RAM recommended

### Installation
1. Clone the repository:
```bash
git clone [repository-url]
cd ai-chat-interface
```

2. Create environment files:
```bash
# backend/.env
OPENAI_API_KEY=your_api_key_here
```

3. Build and run:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Development

### Adding Custom Context
Use the `/api/add-text` endpoint:
```bash
curl -X POST http://localhost:5000/api/add-text \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Your custom context here"]}'
```

### Modifying the RAG System
1. Update `vector_store.py` for embedding changes
2. Modify `app.py` for prompt engineering
3. Adjust `k` parameter in vector search for context amount

## Performance Considerations

### Vector Search
- FAISS uses L2 distance for similarity
- Default k=3 for context retrieval
- Embeddings dimension: 384 (all-MiniLM-L6-v2)

### Response Generation
- Context window optimization
- Prompt engineering for relevance
- Error handling and fallbacks

## Security Considerations
- CORS configuration
- Rate limiting (recommended for production)
- API key security
- Input sanitization

## Future Improvements
1. Persistent vector storage
2. User session management
3. Context history tracking
4. Advanced prompt engineering
5. Custom embedding models
6. Response streaming

## Contributing
Contributions are welcome! Please read our contributing guidelines and submit pull requests to our repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.