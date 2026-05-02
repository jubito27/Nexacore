from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@nexacore.com')

mail = Mail(app)

# Store leads locally (in production, use a database)
LEADS_FILE = 'leads.json'

def load_leads():
    """Load leads from JSON file"""
    if os.path.exists(LEADS_FILE):
        with open(LEADS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_leads(leads):
    """Save leads to JSON file"""
    with open(LEADS_FILE, 'w') as f:
        json.dump(leads, f, indent=2)

@app.route('/')
def index():
    """Render homepage"""
    return render_template('index.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        # Get form data
        data = request.get_json() if request.is_json else request.form.to_dict()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        message = data.get('message', '').strip()

        # Validate required fields
        if not name or not email or not message:
            return jsonify({'error': 'Please fill in all required fields'}), 400

        # Create lead record
        lead = {
            'id': len(load_leads()) + 1,
            'name': name,
            'email': email,
            'phone': phone if phone else 'N/A',
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'status': 'new'
        }

        # Save lead
        leads = load_leads()
        leads.append(lead)
        save_leads(leads)

        # Send email notification (if configured)
        if app.config['MAIL_USERNAME']:
            try:
                msg = Message(
                    subject=f'New Lead from {name}',
                    recipients=[app.config['MAIL_DEFAULT_SENDER']],
                    body=f"""
New Contact Form Submission:

Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Message: {message}

Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    """
                )
                mail.send(msg)
            except Exception as e:
                print(f"Error sending email: {e}")
                # Continue anyway - lead is saved locally

        return jsonify({'success': True, 'message': 'Thank you! We will contact you soon.'}), 200

    except Exception as e:
        print(f"Error processing contact: {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

@app.route('/leads', methods=['GET'])
def get_leads():
    """Get all leads (for admin purposes)"""
    # In production, add authentication before exposing this endpoint
    leads = load_leads()
    return jsonify(leads), 200

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('index.html'), 200

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create leads file if it doesn't exist
    if not os.path.exists(LEADS_FILE):
        save_leads([])
    
    # Run development server
    app.run(debug=True, host='0.0.0.0', port=5000)
