## Currency Converter using Python and Flask

A simple web application that allows users to convert between different currencies using real-time exchange rates.

### Table of Content
- [Overview](#overview)
- [Motivation](#motivation)
- [Learning Objective](#learning-objective)
- [Technical Aspect](#technical-aspect)
- [Technologies Used](#technologies-used)


---

### Overview

This project implements a **Currency Converter** web application using Python's Flask framework. It fetches real-time exchange rates from an API to convert between two currencies. The user inputs the amount, selects the source currency, and the target currency, and the application displays the converted amount. The data is fetched from the [ExchangeRate-API](https://www.exchangerate-api.com/).

### Motivation

The motivation behind this project is to explore end-to-end development of a web application, integrating backend logic (Python/Flask) with frontend design (HTML/CSS) and external API integration for real-time data. Currency exchange is a common problem, and building a converter teaches the basics of web apps and API usage.

### Learning Objective

The main goal of this project is to provide hands-on experience with:
- Flask web framework in Python.
- API integration to fetch real-time data.
- Frontend development with HTML, CSS.
- End-to-end full-stack development, covering backend logic, frontend interface, and real-time API usage.

### Technical Aspect

- **Backend:** Developed using the Flask framework in Python.
- **Frontend:** Built with HTML for user input, displaying the results of currency conversion.
- **API:** The app uses the [ExchangeRate-API](https://www.exchangerate-api.com/) to get the latest exchange rates for conversions.
- **Features:**
  - The user inputs base and target currencies, along with the amount.
  - Real-time conversion is calculated using fetched exchange rates.

### Technologies Used

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)  
[<img target="_blank" src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" width="150">](https://github.com/pallets/flask)
[<img target="_blank" src="https://raw.githubusercontent.com/exchangerate-api/exchangerate-api/master/docs/assets/exchange-rate-logo.png" width="150">](https://www.exchangerate-api.com/)


