# Nexacore Softwares MVP Website

A modern, responsive, and conversion-focused MVP website for Nexacore Softwares Pvt Ltd, built with Flask, Bootstrap, and custom CSS.

## 🎯 Features

✅ **Hero Section** - Eye-catching landing section with call-to-action  
✅ **About Section** - Company information and key highlights  
✅ **Services Section** - 5 core service offerings with icons  
✅ **Statistics Section** - Showcase impressive work metrics  
✅ **Call-to-Action** - Strategic engagement prompt  
✅ **Contact Form** - Lead capture with email validation  
✅ **Responsive Design** - Mobile-first, works on all devices  
✅ **Lead Management** - Automatic lead storage and email notifications  

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Flask (Python)
- **Email**: Flask-Mail (optional)
- **Storage**: JSON (leads are saved locally)
- **Hosting**: Ready for Vercel, Netlify, or any Python-capable host

## 📋 Project Structure

```
Nexacore/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment configuration template
├── README.md             # This file
├── templates/
│   └── index.html        # Main website page
├── static/
│   ├── css/
│   │   └── style.css     # Custom styling
│   └── js/
│       └── script.js     # JavaScript functionality
└── leads.json           # Lead storage (auto-generated)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Clone/Navigate to Project
```bash
cd /home/abhishek-sharma/Nexacore
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Email (Optional)
Copy `.env.example` to `.env` and add your email credentials:
```bash
cp .env.example .env
```

Edit `.env` with your mail settings:
```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

> **Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833).

### 5. Run the Application
```bash
python app.py
```

The website will be available at: **http://localhost:5000**

## 📝 Configuration

### Email Setup (Optional)
By default, the app works without email. To enable email notifications:

1. Set up Gmail App Password:
   - Enable 2-factor authentication on your Google account
   - Generate an [App Password](https://support.google.com/accounts/answer/185833)

2. Update `.env` file with your credentials

3. Restart the app

### Viewing Leads
Leads are automatically saved to `leads.json`. To view all leads programmatically:
```bash
curl http://localhost:5000/leads
```

## 🎨 Customization

### Change Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #0066cc;
    --secondary-color: #6b42c2;
    --accent-color: #ff6b6b;
}
```

### Update Content
Edit `templates/index.html` to change:
- Company name and tagline
- Service descriptions
- Contact information
- Social links

### Add More Services
In `templates/index.html`, duplicate a service card block and update the content:
```html
<div class="col-md-6 col-lg-4">
    <div class="service-card">
        <div class="service-icon">
            <i class="fas fa-icon-name"></i>
        </div>
        <h4>Service Name</h4>
        <p>Service description goes here.</p>
    </div>
</div>
```

Find more icons at: https://fontawesome.com/icons

## 📊 Lead Management

Leads are stored in `leads.json` with:
- Name, Email, Phone, Message
- Timestamp
- Unique ID
- Status (new, contacted, etc.)

You can:
- **View leads**: `curl http://localhost:5000/leads`
- **Export leads**: Open `leads.json` and copy to CSV/Excel
- **Integrate with CRM**: Connect the `/leads` endpoint to your CRM system

## 🌐 Deployment

### Deploy to Vercel
```bash
npm i -g vercel
vercel
```

### Deploy to Heroku
```bash
heroku create nexacore-site
git push heroku main
```

### Deploy to PythonAnywhere
1. Create account at pythonywhere.com
2. Upload files
3. Configure web app to use Flask
4. Set up domain

## 🔒 Security Notes

- **Before production**, add authentication to `/leads` endpoint
- Use environment variables for sensitive data
- Implement CSRF protection
- Add rate limiting to form submissions
- Use HTTPS in production

## 📱 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## ⚡ Performance Tips

1. **Image Optimization**: Replace placeholder images with optimized versions
2. **Caching**: Enable browser caching headers
3. **CDN**: Serve Bootstrap and FontAwesome from CDN (already done)
4. **Minification**: Minify CSS/JS for production
5. **Database**: Migrate from JSON to PostgreSQL for scale

## 🐛 Troubleshooting

**Port 5000 already in use?**
```bash
python app.py --port 5001
```

**Email not sending?**
- Check `.env` file exists
- Verify credentials are correct
- Check Gmail App Password is set up
- Check firewall/antivirus isn't blocking SMTP

**Static files not loading?**
- Clear browser cache
- Restart Flask app
- Check `static/` folder exists

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [FontAwesome Icons](https://fontawesome.com/icons)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)

## 📄 License

Copyright © 2026 Nexacore Softwares Pvt Ltd. All rights reserved.

## 👥 Support

For issues or questions, contact: support@nexacore.com

---

**Built with ❤️ for Modern Businesses**
