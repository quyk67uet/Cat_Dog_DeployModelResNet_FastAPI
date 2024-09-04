# Cat Dog Classification API

This project implements a FastAPI-based API for cat and dog image classification using a pre-trained deep learning model.

## Project Overview

This API allows users to upload an image and receive a prediction on whether the image contains a cat or a dog. The project uses a ResNet18 model trained on a cat-dog dataset and exposes the model's predictions through a RESTful API.

## Features

- Image upload endpoint for cat/dog classification
- Pre-trained ResNet18 model for accurate predictions
- FastAPI for efficient and easy-to-use API development
- CORS middleware for cross-origin resource sharing
- Logging middleware for request tracking
- Pydantic models for input/output validation

## Project Structure

root/
├── config/
│   ├── catdog_cfg.py
│   └── logging_cfg.py
├── logs/
├── middleware/
│   ├── init.py
│   ├── cors.py
│   └── http.py
├── models/
│   ├── weights/
│   │   └── catdog_weights.pt
│   ├── catdog_model.py
│   └── catdog_predictor.py
├── routes/
│   ├── base.py
│   └── catdog_route.py
├── schemas/
│   └── catdog_schema.py
├── utils/
│   └── logger.py
├── app.py
├── requirements.txt
├── server.py
└── README.md
