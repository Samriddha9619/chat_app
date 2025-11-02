# chat_app# 🚀 Real-Time Chat Application

A full-featured real-time chat application built with **Django**, **FastAPI**, and **WebSockets**. Supports private messaging, group chats, and anonymous rooms with live message delivery.

---

## ✨ Features

### 🔐 Authentication
- User registration and login with JWT tokens
- Secure password hashing
- Token-based authentication

### 💬 Chat Types
- **Private Chats**: One-on-one conversations
- **Group Chats**: Multi-user chat rooms
- **Anonymous Rooms**: Chat without registration

### ⚡ Real-Time Features
- Instant message delivery via WebSockets
- Live typing indicators
- User online/offline status
- Message read receipts
- Real-time notifications

### 🎨 User Interface
- Modern, responsive design
- Dark/light theme support
- Emoji picker integration
- Message search and filtering
- File attachments support

### 🛠️ Advanced Features
- Message editing and deletion
- User blocking/reporting
- Chat room management
- Message history
- Cross-platform support (Web, Mobile-ready)

---

## 🏗️ Tech Stack

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API endpoints
- **FastAPI** - WebSocket server
- **PostgreSQL** - Database (Supabase)
- **JWT** - Authentication
- **Channels** - WebSocket support

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript (ES6+)** - Interactive functionality
- **WebSocket API** - Real-time communication

### DevOps
- **Docker & Docker Compose** - Containerization
- **Render** - Cloud deployment
- **Gunicorn** - WSGI server
- **Uvicorn** - ASGI server
- **Whitenoise** - Static file serving

---

## 📦 Installation

### Prerequisites
- Python 3.13+
- Docker & Docker Compose
- PostgreSQL (or use Supabase)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Samriddha9619/chat_app.git
   cd chat_app
   ```

2. **Create `.env` file**
   ```bash
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   CORS_ALLOWED_ORIGINS=http://localhost:8001
   ```

3. **Run with Docker Compose**
   ```bash
   docker compose up --build
   ```

4. **Access the application**
   - Django UI: http://localhost:8001
   - FastAPI WebSocket: http://localhost:8000

### Manual Setup (Without Docker)

1. **Create virtual environment**
   ```bash
   python -m venv .Sam
   source .Sam/bin/activate  # On Windows: .Sam\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Django server**
   ```bash
   python manage.py runserver 8001
   ```

6. **Run FastAPI WebSocket server (separate terminal)**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

---

## 🐳 Docker Deployment

### Using Docker Compose

```bash
docker compose up -d
```

### Individual Services

**Django:**
```bash
docker build -t chat-app-django -f Dockerfile .
docker run -p 8001:8000 --env-file .env chat-app-django
```

**FastAPI:**
```bash
docker build -t chat-app-fastapi -f Dockerfile.fastapi .
docker run -p 8000:8000 --env-file .env chat-app-fastapi
```

---

## ☁️ Production Deployment (Render)

### 1. Deploy Django Service

1. Create new **Web Service** on Render
2. Connect GitHub repository
3. Configure:
   - **Environment**: Docker
   - **Dockerfile Path**: `Dockerfile`
   - **Docker Build Context**: `.`

4. Add environment variables:
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.onrender.com
   DATABASE_URL=postgresql://...
   CORS_ALLOWED_ORIGINS=https://your-app.onrender.com
   ```

### 2. Deploy FastAPI WebSocket Service

1. Create another **Web Service** on Render
2. Connect same GitHub repository
3. Configure:
   - **Environment**: Docker
   - **Dockerfile Path**: `Dockerfile.fastapi`
   - **Docker Build Context**: `.`

4. Add environment variables:
   ```
   SECRET_KEY=your-production-secret-key
   DATABASE_URL=postgresql://...
   ```

### 3. Update Frontend URLs

In `templates/index.html`, update lines 864-870:

```javascript
const API_URL = 'https://your-django-app.onrender.com/api';
const WS_URL = 'wss://your-fastapi-app.onrender.com/ws';
```

---

## 📁 Project Structure

```
chat_app/
├── app/                        # FastAPI WebSocket application
│   ├── __init__.py
│   ├── main.py                # WebSocket server
│   └── models.py              # Shared models
├── chat_app/                   # Django project
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI config
├── templates/                  # HTML templates
│   └── index.html             # Main chat interface
├── static/                     # Static files (CSS, JS, images)
├── .dockerignore              # Docker ignore rules
├── .env                       # Environment variables (not in git)
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Django Docker config
├── Dockerfile.fastapi         # FastAPI Docker config
├── docker-compose.yml         # Docker Compose config
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version
└── README.md                  # This file
```

---

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-xyz...` |
| `DEBUG` | Debug mode | `True` or `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1,*.onrender.com` |
| `DATABASE_URL` | PostgreSQL connection | `postgresql://user:pass@host:5432/db` |
| `CORS_ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:8001` |

---

## 🛠️ API Endpoints

### Authentication
```
POST   /api/register/          - Register new user
POST   /api/login/             - Login user
POST   /api/token/refresh/     - Refresh JWT token
```

### Chat Rooms
```
GET    /api/chatrooms/         - List all chat rooms
POST   /api/chatrooms/         - Create new chat room
GET    /api/chatrooms/{id}/    - Get chat room details
DELETE /api/chatrooms/{id}/    - Delete chat room
```

### Messages
```
GET    /api/messages/          - List messages (filtered by room)
POST   /api/messages/          - Send message (also via WebSocket)
DELETE /api/messages/{id}/     - Delete message
```

### WebSocket
```
WS     /ws?token={jwt}         - Authenticated WebSocket connection
WS     /ws?anonymous=true      - Anonymous WebSocket connection
```

---

## 🔌 WebSocket Protocol

### Client → Server

**Send Message:**
```json
{
  "type": "send_message",
  "chat_room_id": 1,
  "content": "Hello!",
  "anonymous_name": "Guest123"
}
```

**Join Room:**
```json
{
  "type": "join_room",
  "chat_room_id": 1
}
```

**Typing Indicator:**
```json
{
  "type": "typing",
  "chat_room_id": 1,
  "is_typing": true
}
```

### Server → Client

**New Message:**
```json
{
  "type": "new_message",
  "message_id": 123,
  "chat_room_id": 1,
  "content": "Hello!",
  "sender_name": "John",
  "is_anonymous": false,
  "timestamp": "2025-10-31T12:00:00Z"
}
```

**User Typing:**
```json
{
  "type": "user_typing",
  "chat_room_id": 1,
  "user_name": "John",
  "is_typing": true
}
```

**Error:**
```json
{
  "type": "error",
  "message": "Invalid chat room"
}
```

---

## 🧪 Testing

### Run Django Tests
```bash
python manage.py test
```

### Test WebSocket Connection
```javascript
const ws = new WebSocket('ws://localhost:8000/ws?token=YOUR_JWT_TOKEN');
ws.onopen = () => console.log('Connected!');
ws.onmessage = (e) => console.log('Received:', e.data);
```

---

## 🐛 Troubleshooting

### WebSocket Not Connecting
- Check FastAPI service is running on port 8000
- Verify CORS settings in `app/main.py`
- Check browser console for errors

### Messages Not Appearing
- Open browser DevTools (F12) → Console
- Check for WebSocket connection status
- Verify `addMessageToUI()` function is called

### Database Connection Error
- Verify `DATABASE_URL` in `.env`
- Check PostgreSQL is running
- Run migrations: `python manage.py migrate`

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` in settings

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Samriddha**
- GitHub: [@Samriddha9619](https://github.com/Samriddha9619)
- Repository: [chat_app](https://github.com/Samriddha9619/chat_app)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

- Django & Django REST Framework teams
- FastAPI community
- Render for hosting
- Supabase for database

---

## 📸 Screenshots

### Login Screen
![Login](screenshots/login.png)

### Chat Interface
![Chat](screenshots/chat.png)

### Group Chat
![Group](screenshots/group.png)

---

## 🔮 Future Enhancements

- [ ] Voice/Video calls
- [ ] File sharing improvements
- [ ] Message reactions (👍, ❤️, etc.)
- [ ] Message encryption (E2E)
- [ ] Mobile apps (React Native)
- [ ] Message translation
- [ ] Advanced search
- [ ] Chatbots integration
- [ ] Screen sharing

---

## 📚 Documentation

For detailed documentation, visit:
- [Django Docs](https://docs.djangoproject.com/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---

**⭐ If you found this project helpful, please give it a star!**

**🐛 Found a bug? [Open an issue](https://github.com/Samriddha9619/chat_app/issues)**

**💡 Have a feature idea? [Start a discussion](https://github.com/Samriddha9619/chat_app/discussions)**