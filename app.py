# app.py

import streamlit as st
from PIL import Image

# Fraud detection functions

def detect_fraud_in_website(url: str) -> bool:
    """
    Detect if a website URL is potentially fraudulent.
    
    Parameters:
    - url (str): The URL of the website to check.
    
    Returns:
    - bool: True if the website is likely fraudulent, False otherwise.
    """
    # List of suspicious keywords often found in fraudulent URLs
    suspicious_keywords = [
        'free', 'winner', 'prize', 'secure', 'verify', 
        'login', 'account', 'update', 'confirm', 'bank'
    ]
    
    # Check for presence of suspicious keywords in the URL
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True
    
    # Additional logic can be added here for more robust detection
    
    return False

def detect_spam_email(content: str) -> bool:
    """
    Detect if an email content is likely spam.
    
    Parameters:
    - content (str): The text content of the email.
    
    Returns:
    - bool: True if the email is likely spam, False otherwise.
    """
    # List of common spam keywords
    spam_keywords = [
        'congratulations', 'winner', 'claim', 'urgent', 
        'money', 'prize', 'free', 'click', 'offer', 
        'lottery', 'investment', 'inheritance', 'deal'
    ]
    
    # Check for presence of spam keywords in the email content
    for keyword in spam_keywords:
        if keyword in content.lower():
            return True
    
    return False

def detect_spam_texts(messages: list) -> list:
    """
    Detect if a list of text messages are likely spam.
    
    Parameters:
    - messages (list): A list of text messages to check.
    
    Returns:
    - list: A list of booleans indicating whether each message is spam.
    """
    spam_keywords = [
        'free', 'win', 'click', 'buy', 'promo', 
        'offer', 'deal', 'credit', 'loan', 'urgent'
    ]
    
    results = []
    for message in messages:
        is_spam = any(keyword in message.lower() for keyword in spam_keywords)
        results.append(is_spam)
    
    return results

def detect_phishing_text(content: str) -> bool:
    """
    Detect if a text content is likely a phishing attempt.
    
    Parameters:
    - content (str): The text content to check.
    
    Returns:
    - bool: True if the text is likely phishing, False otherwise.
    """
    phishing_keywords = [
        'verify your account', 'login', 'password', 'bank', 'confirm',
        'update', 'secure', 'alert', 'suspend', 'security'
    ]
    
    for keyword in phishing_keywords:
        if keyword in content.lower():
            return True
    
    return False

# Streamlit app
def main():
   

    # App title and logo
    st.set_page_config(page_title="Fraud Shield", page_icon=":shield:"
    st.title("Fraud Shield")
    st.write("A simple app to detect fraud in websites, emails, and text messages.")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = ["Home", "Website Fraud Detection", "Email Spam Detection", "Text Message Spam Detection", "Phishing Detection"]
    choice = st.sidebar.radio("Go to", options)
    
    # Home
    if choice == "Home":
        st.subheader("Welcome to Fraud Shield")
        st.write("Select a feature from the sidebar to start detecting fraud.")
    
    # Website Fraud Detection
    elif choice == "Website Fraud Detection":
        st.subheader("Website Fraud Detection")
        url = st.text_input("Enter the website URL:")
        if st.button("Check"):
            if detect_fraud_in_website(url):
                st.warning("The website is potentially fraudulent!")
            else:
                st.success("The website appears to be safe.")
    
    # Email Spam Detection
    elif choice == "Email Spam Detection":
        st.subheader("Email Spam Detection")
        email_content = st.text_area("Enter the email content:")
        if st.button("Analyze"):
            if detect_spam_email(email_content):
                st.warning("The email is likely spam!")
            else:
                st.success("The email appears to be safe.")
    
    # Text Message Spam Detection
    elif choice == "Text Message Spam Detection":
        st.subheader("Text Message Spam Detection")
        messages = st.text_area("Enter text messages (one per line):")
        if st.button("Check Messages"):
            messages_list = messages.split("\n")
            results = detect_spam_texts(messages_list)
            for i, result in enumerate(results):
                if result:
                    st.warning(f"Message {i+1} is likely spam!")
                else:
                    st.success(f"Message {i+1} appears to be safe.")
    
    # Phishing Detection
    elif choice == "Phishing Detection":
        st.subheader("Phishing Detection")
        text_content = st.text_area("Enter the content to analyze:")
        if st.button("Check for Phishing"):
            if detect_phishing_text(text_content):
                st.warning("The content is likely a phishing attempt!")
            else:
                st.success("The content appears to be safe.")

if __name__ == "__main__":
    main()


