# Getting sensor data and insert to database

## Intro

ESP32 microcontroller gathers data from a sensor and a web service, processes it, and stores it in a database. 

## The process

### 1. Sensor Data Acquisition:

- The ESP32 then communicates with the BME680 sensor through the I2C protocol.
- The BME680 sensor measures environmental parameters like temperature, humidity, and pressure.
- This sensor data is sent back to the ESP32

### 2. ESP 32 Making a request

- The ESP32 microcontroller starts by making an HTTP GET request to the Google Sheet.
- This request retrieves data from the sheet, potentially containing instructions or configuration settings for the project.

### 3. Google App Script working process

- handle an HTTP GET request with parameters related to sensor
- integration with a Google Sheet
- Appending Data to the Google Sheet

### 4. Python Program that does

- Connects to a Google Sheets document
- Retrieves all records from the selected worksheet
- Inserts the transformed data into the "bme680_data" table in the MySQL database


## Flowchart

![line](https://github.com/NoppalitP/sensordata2database/assets/155846151/7ebcc553-f0e7-4574-9819-d8af8070f6a7)

## Hardwere

### Sensor BME680

- BME680
Gas sensor measuring relative humidity, barometric pressure, ambient temperature and gas (VOC).

![sensor](https://store.fut-electronics.com/cdn/shop/files/BME680-enviromental-sensor_500x500.jpg)

* [ฺBME680](https://shopee.co.th/Bme680-%E0%B9%80%E0%B8%8B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%8B%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%AD%E0%B8%B8%E0%B8%93%E0%B8%AB%E0%B8%A0%E0%B8%B9%E0%B8%A1%E0%B8%B4%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%8A%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%94%E0%B8%B4%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B8%AD%E0%B8%A5-Cjmcu-680-High-Altitude-Sensor-i.341476548.9802165029?sp_atk=91f17fd6-a9dd-4a54-99b6-3a068c1aee20&xptdk=91f17fd6-a9dd-4a54-99b6-3a068c1aee20) - BME680 Its price is 170 baht from china.

![s_sensor](https://github.com/NoppalitP/sensordata2database/assets/155846151/d7d6f30e-4995-4fa8-b7dc-85d16e51bf68)

### ESP32
- ESP32 is a series of low-cost, low-power system on a chip microcontrollers

![esp32](https://store.fut-electronics.com/cdn/shop/files/esp32-development-kit-30pin_500x500.jpg)

* [ESP32](https://shopee.co.th/ESP32-ESP32S-Node32-ESP-WROOM-32-NodeMCU-32-WiFi-Bluetooth-IoT-Development-Board-%E0%B8%9A%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1%E0%B8%A7%E0%B8%87%E0%B8%88%E0%B8%A3-i.270502312.5537452929?sp_atk=35d6e786-fda5-4f91-a134-181dbe0271a7&xptdk=35d6e786-fda5-4f91-a134-181dbe0271a7) - ESP32 Its price around 168 baht.

![s_esp32](https://github.com/NoppalitP/sensordata2database/assets/155846151/0fb5ac61-da83-4615-8bb1-235f2bb84630)

## Sensor data obtained from bme680 sensor Send to google sheet

### Temperature,Humidity,Pressure,Gas,Pressure altitude

![data](https://github.com/NoppalitP/sensordata2database/assets/155846151/1b1995b5-bacf-437e-a7be-5f16c1b9503f)

## Picture of circuit

### BME680

![BME680_r](https://github.com/NoppalitP/sensordata2database/assets/155846151/7609209e-18fc-4ef8-a6ea-80504a40cb9a)

### ESP32

![ESP32_r](https://github.com/NoppalitP/sensordata2database/assets/155846151/34e8dce5-8b79-4b11-a868-794bfc5745bb)

### 2.42 INCH OLED I2C Display Module

![Monitor](https://github.com/NoppalitP/sensordata2database/assets/155846151/92c0d473-31c1-4bac-bfcd-ff4c33cf5def)

### Whole circuit

![Whole](https://github.com/NoppalitP/sensordata2database/assets/155846151/04d66c0b-e711-4847-bfff-f1928712b743)


