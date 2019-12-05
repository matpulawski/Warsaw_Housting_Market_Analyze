# Warsaw_Housting_Analyze
The final project at the Data Science bootcamp (Kodołamacz - Sages)

## Project

The goal of the project is to acquire and analyze data, and then select and optimize the machine learning algorithm to predict the prices of houses in Warsaw Housting Market.

## Dataset

The data used for the analysis came from the [OTODOM](https://www.otodom.pl/) website and were posted there in 16.11.2019.
I collected ads using Web Scraping. Data scraping and saving to the database is carried out by the framework Scrapy.

Describe of the dataset columns:
* ```district``` - district in Warsaw where is the apartment,
* ```area``` - area of apartment in sqm,
* ```chamber``` - number of chambers in the apartment,
* ```market``` - origin of offer (primary or secondary market)
* ```building``` - type of building,
* ```floor``` - number of floors in the apartment,
* ```building_floors``` - number of floors in the whole building,
* ```construction_year``` - year, when building was build,
* ```standard``` - describe of the apartment standard,
* ```property``` - type of property,
* ```window``` - type of window in the apartment,
* ```heating``` - type of heating in the apartment,
* ```url``` -  url address of the add,
* ```rent``` - heigh of rent in PLN,
* ```price``` - price of the apartment in PLN,

## Prerequisites

This project requires Python and the following Python libraries installed:

* scrapy v 1.2.1
* sklearn v 0.21.3
* xgboost v 0.90
* pandas v.0.24.2
* numpy v 1.16.2
* matplotlib v 3.0.3
* scipy 1.2.1

You may also have Jupyter Notebook software installed on your computer.
