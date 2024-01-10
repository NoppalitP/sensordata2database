# Getting sensor data and insert to database

## Intro

ESP32 microcontroller gathers data from a sensor and a web service, processes it, and stores it in a database. 

## The process

### 1.Sensor Data Acquisition:

- The ESP32 then communicates with the BME680 sensor through the I2C protocol.
- The BME680 sensor measures environmental parameters like temperature, humidity, and pressure.
- This sensor data is sent back to the ESP32

### 2.Making a request

-The ESP32 microcontroller starts by making an HTTP GET request to the Google Sheet.

-This request retrieves data from the sheet, potentially containing instructions or configuration settings for the project.


## Flowchart

![line](https://github.com/NoppalitP/sensordata2database/assets/155846151/7ebcc553-f0e7-4574-9819-d8af8070f6a7)

![sensor](https://store.fut-electronics.com/cdn/shop/files/BME680-enviromental-sensor_500x500.jpg)


![esp32](https://store.fut-electronics.com/cdn/shop/files/esp32-development-kit-30pin_500x500.jpg)


![s_sensor](https://github.com/NoppalitP/sensordata2database/assets/155846151/d7d6f30e-4995-4fa8-b7dc-85d16e51bf68)

![s_esp32](https://github.com/NoppalitP/sensordata2database/assets/155846151/0fb5ac61-da83-4615-8bb1-235f2bb84630)



![python](https://github.com/NoppalitP/sensordata2database/assets/155846151/eb208313-48ba-4062-bae4-35dd886f8352)
![google sheet](https://github.com/NoppalitP/sensordata2database/assets/155846151/27e53ded-ebc9-413c-82ec-b8c166d78b1f)

![data](https://github.com/NoppalitP/sensordata2database/assets/155846151/1b1995b5-bacf-437e-a7be-5f16c1b9503f)
![app script](https://github.com/NoppalitP/sensordata2database/assets/155846151/77a940b2-9e1b-48b4-b901-b808621b00f7)

![MySQL-Database](https://github.com/NoppalitP/sensordata2database/assets/155846151/0320cbee-65c3-4218-a745-3ab477303f8a)
