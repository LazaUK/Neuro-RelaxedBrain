# Neuro Hack - Analysing brain waves of relaxed brain.

This is my attempt to read and visualise brain wave telemetry, retrieved from the Muse meditation device.
> **Note:** This solution has been built and tested in Python 3.8.

## Pre-requisites
For this tutorial, you would need the following hardware and software components:
- Muse meditation device. See the [Muse Web site](https://choosemuse.com/) for available models that support *EEG streaming*;
- Computer with pre-installed Python 3.x;

## Step 0 - Client Setup
1. Download content of this repo;
2. Install python libraries, missing on your computer. E.g, to deploy muselsl for EEG streaming, use:
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

## Step 3 - Visualise content in PowerBI dashboard

Finally, you can visualise your Energy Metering data in PowerBI. Below is an example of a PowerBI dashboard with the real-time telemetry and historical stats.
![Step4](/images/Step4.png)

