Spatial data aquisition and standards
=====================================

### Key messages
The recommended Terrestrial Reference Framework to locate a point on the earth’s surface  is GWS84 using decimal degrees Latitude and Longitude coordinates with at least four decimal places (d.ddddd), for example Latitude: 52.05256, Longitude 5.26671. In this way locations are indicated with an accuracy of 1m.

**Using a Navigational Satellite System (NSS)**
Modern smartphones have enough accuracy to map geolocations in the field using the internal receiver for NSS signals. Depending on the conditions accuracies between 2 and 9m can be reached.

The NAVSTAR GPS system is the standard system currently in use on most mobile devices, however some devices are capable of combining different systems, providing a higher accuracy and shorter search time for satellites connections.

Make sure that the accuracy while measuring is < 10m. Automated averaging of multiple measurements of the same location is a practical solution to reduce error towards 1m.

To measure the boundary of an area (a polygon) only the corners should be measured manually to minimize the error in the service area. Measuring multiple points along the edge of an area or using an automated tracking function in your GPS reduces the accuracy.

**Using screen digitization**
Locations and areas can also be mapped from a screen. Screen digitization is always in relation to another data source (aerial photograph, satellite image or GIS file). There are a number of aspect that need attention:
* The TRF of the reference source and the TRF that is used for the digitization. The recommended TRF in the reference framework is GWS84 using decimal degrees Latitude and Longitude coordinates. Local datasets are possibly to based on a different RTF. More advanced desktop GIS, like QGIS or ARCGIS are capable of making data transformations from one TRF to another TRF but need to be operated by a specialist.
* The accuracy of the reference data set is determining the accuracy of the results. Field boundaries or boundaries between farms may not be clear on an aerial photograph for small holder farms. Boundaries maybe not visible or appear fuzzy. A third party data set needs to be checked overlaying it with actual field measurements to be sure of the accuracy.

Different approaches to digitize data from screen are described.

### Introduction
The collection of spatial information of objects, like the geolocation or shape of objects, is of growing importance for first mile data collection. Spatial information helps to: 
1. identify objects (see the section on [Uniquely identifying data elements]{http://farm-level-data-standard.readthedocs.io/en/latest/05%20identification/}, 
2. to combine different sources of information, e.g. to identify all farms with a particular soil type using a soil map,
3. to determine spatial relations, e.g. to select all farms with a market nearby of less than 10 km and to determine spatial characteristics of an object e.g. the area of a field. 

**The geolocation** is description of the location of an object at the earth's surface in coordinates relative to a mathematically defined **Terrestrial Reference Frame (TRF)**. The standard TRF recommended in this document is GWS84 using decimal degrees Latitude and Longitude coordinates with at least four decimal places (d.ddddd), for example Latitude: 52.05256, Longitude 5.26671. Four decimal places indicate an accuracy of about 1 meters and five decimal degrees indicate an accuracy of about 1 meter. Points in the Southern hemisphere have negative latitudes; points in the western hemisphere (the Americas) have negative longitudes. If the sign is positive (northern hemisphere latitudes and eastern hemisphere longitudes), it is not necessary to include a “+” sign. The [WGS84 TRF]{http://earth-info.nga.mil/GandG/wgs84/index.html} is the first globally applicable TRF and is currently the default for world standards and for most applications and devices including the [GeoJSON]{ https://tools.ietf.org/html/rfc7946} and the NAVSTAR Global Positioning System or [GPS]{http://www.gps.gov/}. When using spatial data, especially when using third party georeferenced data, it is essential to be aware of the coordinate system used to describe the geolocations. Combining 2 spatial datasets based on a different TRF will result in errors if not carried out properly. More background on fundamentals from geodesy and cartography needed for georeferencing can be found in [the last section]{}.

Nowadays spatial information is often collected and stored digitally using [an object model of points, lines and polygon or collections of these]{https://www.e-education.psu.edu/geog486/l1_p8.html}. A Point type object is described by a single coordinate pair. A line string is a one-dimensional object represented by a sequence of points and the line segments connecting them. A Polygon is a two-dimensional surface stored as a sequence of points defining an exterior bounding ring of at least 3 points and zero or more interior rings to represent holes in the polygon if needed. Spatial information about objects can be collected digitally in the field using a Navigational Satellite System or behind a computer using a Geographical Information System. Both approaches are explained in more detail in [the section on Navigational Satellite System (NSS) to collect spatial data]{} and [4.2.2.]{}.

### Using a Navigational Satellite System (NSS) to collect spatial data in the field.
A [Navigational Satellite System]{https://en.wikipedia.org/wiki/Satellite_navigation} is a constellation satellites with accurately known positions or orbits that transmits coded radio signals. These coded radio signals are used by specialized electronic devices to calculate the location on the earth’s surface relative to the satellite constellation. Currently the American [NAVSTAR Global Positioning System or GPS]{http://www.gps.gov/} is the most used system. However alternative systems exist, or become operational soon in the future (see also the below table on NSS). Nowadays some receivers can already use the data from these alternative systems, or combine the signals of several systems. Combining the data from 2 or more NSS increases the accuracy of the measurement and decreases the search time for satellites data connections. 

System | Coverage | Public horizontal Accuracy | Current Status | TRF
--- | --- | --- | --- | ---
GPS | Global | 2-9m | Operational | WGS84
GLONASS | Global | 4-7m | Operational | PZ-90
BeiDou-2 | South East Asia and Australia | 10m | Regionally Operational, Global in 2020 | BTRF
Galileio | Global | 4m | Accessible,fully Operational in 2019 | GTFR
NAVIC | 1.500 km beyond the Indian subcontinent | 10m | Operational | ITRF









### Using a Geographical Information System (GIS) to to collect spatial data in the field. 

### Some more background on the complexity behind geodata







