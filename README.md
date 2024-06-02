# Banking System

This is a simple banking system implemented in Python using the Tkinter module. It provides a user-friendly interface for registering, logging in, depositing, and making payments. This project serves as a foundational requirement for future projects that involve payment options, such as restaurant management systems, parking management systems, etc.

## Prerequisites

Ensure you have the following installed:

- `pip`
- `qrcode`
- `opencv-python` (for QR code scanning)
- `Pillow` (PIL fork for image processing)

You can install these dependencies using pip:

bash
  
      pip install qrcode opencv-python Pillow



Database Setup
Execute the following SQL commands to create the necessary database tables:

      CREATE DATABASE bankingsystem;
      
      CREATE TABLE users (
          uid VARCHAR(255) NOT NULL,
          name VARCHAR(255),
          age INT,
          gender VARCHAR(10),
          passs VARCHAR(255),
          email VARCHAR(255),
          contact VARCHAR(20),
          PRIMARY KEY (uid)
      );
      
      CREATE TABLE account (
          casid VARCHAR(255) NOT NULL,
          amount DECIMAL(10, 2),
          passs VARCHAR(255),
          interest DECIMAL(5, 2),
          PRIMARY KEY (casid)
      );



