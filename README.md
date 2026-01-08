# SimCar
A simple webpage for car owners (simulated car only available). 

View information about the car's battery, such as the battery level and whether it is currently charging or not.
Provides the ability to start / stop charging the battery using REST APIs. 

Tools
Uses Azure IoT Hub to connect to your simulated car - car simulated by a small console program using C# IoT Device SDK.
The console program simulates the battery percentage and charging state.
Uses Azure Functions to process messages from IoT Hub
Vanilla JS used for front end.
