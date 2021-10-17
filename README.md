# Neuro Hack - Analysing brain waves of relaxed brain

This is my attempt to read and visualise brain wave telemetry, retrieved from the Muse meditation device.
> **Note:** This solution has been built and tested in Python 3.8.

## Pre-requisites
For this tutorial, you would need the following hardware and software components:
- Muse meditation device. See the [Muse Web site](https://choosemuse.com/) for available models that support *EEG streaming*;
- Computer with pre-installed Python 3.x.

## Step 0 - Client Setup
1. Download content of this repo;
2. Install python libraries, missing on your computer. E.g, to deploy muselsl for EEG streaming, use:
```
pip install muselsl
```

## Step 1 - Stream EEG telemetry

1. Execute Python script Laziz_step1.py. It uses [muselsl](https://pypi.org/project/muselsl/1.0.4/) Python module, published on PyPI by Alexandre Barachant, to stream EEG data out of the Muse meditation device;
2. You should see the following output in your command line, confirming successful connectivity to the Muse device and activation of EEG stream:

![Step1a](/images/Step1a.png)


## Step 2 - Process brain wave details

1. Execute Python script Laziz_step2.py. This second script will spin up Dash Web service, process EEG telemetry and send the data to Dash charts;
2. You should see the following output in your command line, with the values for Alpha, Beta and Theta waves:

![Step2a](/images/Step2a.png)


## Step 3 - Visualise content in PowerBI dashboard

Finally, you can visualise your Energy Metering data in PowerBI. Below is an example of a PowerBI dashboard with the real-time telemetry and historical stats.
![Step4](/images/Step4.png)

