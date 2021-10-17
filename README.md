# Neuro Hack - Analysing brain waves of relaxed brain.

This is my attempt to read and visualise brain wave telemetry, retrieved from the Muse meditation device.
> **Note:** This solution has been built and tested in Python 3.8.

## Pre-requisites
For this tutorial, you would need the following hardware and software components:
- Muse meditation device. See the [Muse Web site](https://choosemuse.com/) for available models that support *EEG streaming*;
- Computer with pre-installed Python 3.x;

## Step 0 - Client Setup
1. Download content of this repo;
2. Install python library, missing on your computer. E.g, to deploy muselsl for EEG streaming, use:
```
pip install muselsl
```

## Step 1 - Azure IoT Hub configuration

1. Deploy Azure IoT Hub resource in your Azure subscription;
2. In Azure IoT Hub, add new IoT device corresponding to your SmartPlug using "Add Device" under Explorers -> IoT devices:
![Step1a](/images/Step1a.png)
3. Open newly created IoT device record and copy one of its connection strings (either primary or secondary:
![Step1b](/images/Step1b.png)
4. Open downloaded DemoKasa.py file and update the value of the CONNECTION_STRING variable with the copied connection string from the previous action above:
![Step1c](/images/Step1c.png)


## Step 2 - Azure SQL configuration

1. Deploy Azure SQL database in your Azure subscription;
2. Create a table in the newly-deployed Azure SQL database, using the following SQL script, so that you can store there your Smart Plug's daily and monthly stats:
```
CREATE TABLE [dbo].[energydata](
    [id] [int] IDENTITY(1, 1) NOT NULL,
    [teledate] [varchar](10) NULL,
    [monthly_stats] [nvarchar](max) NULL,
    [yearly_stats] [nvarchar](max) NULL
)
```

## Step 3 - Azure Stream Analytics configuration

1. Deploy Azure Stream Analytics job resource in your Azure subscription;
2. Add Azure IoT Hub from Step 1 above as a stream input for your Azure Stream Analytics job:
![Step3a](/images/Step3a.png)
3. Add PowerBI as a real-time telemetry output from your Azure Stream Analytics job:
![Step3b](/images/Step3b.png)
4. Add Azure SQL as a historical data output from your Azure Stream Analytics job:
![Step3c](/images/Step3c.png)
5. Create a new query in Stream Analytics that can analyse input from IoT Hub and redirect specific values to PowerBI and Azure SQL DB based on the values of telemetryContent custom property:
```
WITH data AS
(
    SELECT
        *,
        GetMetadataPropertyValue(MyIotHub, '[User].[telemetryContent]') AS telemetryContent
    FROM MyIoTHub 
)

SELECT 
    current_ma, voltage_mv, power_mw, total_wh, EventProcessedUtcTime as time
INTO 
    MyBIRT
FROM data
WHERE
    telemetryContent = 'RealTime_Telemetry'

SELECT 
    teledate, monthly_stats, yearly_stats
INTO 
    MySQLDB
FROM data
WHERE
    telemetryContent = 'Monthly_Stats'
```
6. Activate your Azure Stream Analytics job.

## Step 4 - Visualise content in PowerBI dashboard

Finally, you can visualise your Energy Metering data in PowerBI. Below is an example of a PowerBI dashboard with the real-time telemetry and historical stats.
![Step4](/images/Step4.png)

