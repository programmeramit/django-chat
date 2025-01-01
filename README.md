

# **Real-Time Group Chat Application**

This is a **real-time group chat application** built with **Django Channels** and **Redis**. The app allows users to join chat groups, send and receive messages instantly, and includes features like unique usernames and easy group name copying.

---

## **Features**

### 🔥 Real-Time Chat
- Users can send and receive messages instantly without refreshing the page.
- Messages are delivered in real-time using **WebSockets**.

### 👥 Group Chat
- Users can join existing groups or create new ones.
- Each group is identified by a unique group name.

### 🧑‍💻 Unique Usernames
- Every user is required to enter a unique username when joining the app.
- This ensures clear identification during group interactions.

### 📋 Copy Group Name
- Users can copy the group name with a single click for easy sharing with others.



## **Technologies Used**

### Backend:
- **Django**: Core backend framework.
- **Django Channels**: Handles WebSocket connections for real-time communication.
- **Redis**: Acts as the channel layer for message brokering.

### Frontend:
- **HTML/CSS**: Basic UI for chat interface.
- **JavaScript**: Handles WebSocket connections and dynamic updates.

---

## **Installation**

### Prerequisites
- Python (>= 3.8)
- Redis Server
- Django (>= 4.0)

### Steps
1. **Clone the repository**:
   ```bash
    https://github.com/programmeramit/django-chat
   cd django-chat
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Redis server**:
   Make sure Redis is running. Use the following command to start Redis:
   ```bash
   redis-server
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open the app in your browser**:
   Visit `http://127.0.0.1:8000` to use the chat app.

---

## **Usage**

1. **Join or Create a Group**:
   - Enter your username.
   - Enter the group name you want to join or create.
   - Click "Join".

2. **Send Messages**:
   - Type your message in the input box and press Enter.

3. **Copy Group Name**:
   - Click on the "Copy Group Name" button to copy the name to your clipboard.

---

## **Configuration**

### Redis Configuration
By default, the app assumes Redis is running locally on port `6379`. If you need to configure a different Redis server, update the `CHANNEL_LAYERS` in `settings.py`:

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
```

---

## **Screenshots**

### **Login Page**
- Users can enter their username and group name.

### **Chat Interface**
- Real-time messages appear as soon as they're sent.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

- [Django Channels Documentation](https://channels.readthedocs.io/en/stable/)
- [Redis](https://redis.io/)
- All contributors and the open-source community!

---

Feel free to replace placeholders like `yourusername` and adjust sections as needed for your project. Let me know if you want further customization!
