Spatial data acquisition and standards
=====================================

## Key messages
Spatial data collection is always in reference to some theoretical model of the earth. The recommended '*model earth*' or Terrestrial Reference Framework (TRF) to locate a point on the earth’s surface  is GWS84 using decimal degrees Latitude and Longitude coordinates with at least four decimal places (d.dddd), for example Latitude: 52.0525, Longitude 5.2667. In this way locations are indicated with an accuracy of 10m.

**Using a Navigational Satellite System (NSS)**
Modern smartphones have enough accuracy to map geolocations in the field using the internal receiver for NSS signals. Depending on the conditions accuracies between 2 and 9m can be reached.

The NAVSTAR GPS system is the standard system currently in use on most mobile devices, however some devices are capable of combining GPS with other navigation systems, providing a higher accuracy and shorter search time for satellites connections.

Make sure that the accuracy while measuring is < 10m. Automated averaging of multiple measurements of the same location is a practical solution to reduce error towards 1m.

To measure the boundary of an area (a polygon) only the corners should be measured manually minimizing the error of the area measured. On the contrary a strategy of measuring multiple points along the edge of an area or using an automated tracking function in your device reduces the accuracy.

**Using screen digitization**
Locations and areas can also be mapped from a screen. Screen digitization is always in relation to another data source (aerial photograph, satellite image or GIS file). There are a number of points to take into account:
* The TRF of the reference source and the TRF that is used for the digitization. Local datasets used are possibly to based on a different RTF. The combination of data sources with different TRF's or other data handling using the wrong TRF leads to errors in the results. More advanced desktop GIS, like QGIS or ARCGIS are capable of making data transformations from one TRF to another TRF but need to be operated by a specialist.
* The accuracy of the reference data set is determining the accuracy of the end result. Field boundaries or boundaries between farms may not be clear on an aerial photograph for small holder farms. Boundaries maybe not visible or appear fuzzy. It is best to check the quality of a third party data set by overlaying it with actual field measurements or other data with known accuracy.

Different approaches to digitize data from screen are described in this section.

## Introduction
The collection of spatial information of objects, like the geolocation or the shape of objects, is of growing importance for first mile data collection. Spatial information helps to: 
1. identify objects (see the section on '*[Uniquely identifying data elements](http://farm-level-data-standard.readthedocs.io/en/latest/05%20identification/)*', 
2. to combine different sources of information, e.g. to identify all farms with a particular soil type using a soil map,
3. to determine spatial relations, e.g. to select all farms with a market nearby of less than 10 km and to determine spatial characteristics of an object e.g. the area of a field. 

**The geolocation** is description of the location of an object at the earth's surface in coordinates relative to a mathematically defined **Terrestrial Reference Frame (TRF)**. The standard TRF recommended in this document is GWS84 using decimal degrees Latitude and Longitude coordinates with at least four decimal places (d.dddd), for example Latitude: 52.0525, Longitude 5.2667. Four decimal places indicate an accuracy of about 10 meters and five decimal degrees indicate an accuracy of about 1 meter. Points in the Southern hemisphere have negative latitudes; points in the western hemisphere (the Americas) have negative longitudes. If the sign is positive (northern hemisphere latitudes and eastern hemisphere longitudes), it is not necessary to include a “+” sign. The [WGS84 TRF](http://earth-info.nga.mil/GandG/update/index.php?dir=wgs84&action=wgs84) is the first globally applicable TRF and is currently the default for world standards and for most applications and devices including the [GeoJSON](https://tools.ietf.org/html/rfc7946) and the NAVSTAR Global Positioning System or [GPS](http://www.gps.gov/). When using spatial data, especially when using third party georeferenced data, it is essential to be aware of the coordinate system used to describe the geolocations. Combining 2 spatial datasets based on a different TRF will result in errors if not carried out properly. More background on fundamentals from geodesy and cartography needed for georeferencing can be found in [the last section](http://farm-level-data-standard.readthedocs.io/en/latest/06%20spatialdata/#some-more-background-on-the-complexity-behind-geodata).

Nowadays spatial information is often collected and stored digitally using [an object model of points, lines and polygon or collections of these](https://www.e-education.psu.edu/geog486/l1_p8.html). A Point type object is described by a single coordinate pair. A line string is a one-dimensional object represented by a sequence of points and the line segments connecting them. A Polygon is a two-dimensional surface stored as a sequence of points defining an exterior bounding ring of at least 3 points and zero or more interior rings to represent holes in the polygon if needed. Spatial information about objects can be collected digitally in the field using a Navigational Satellite System  ([More info in this section](http://farm-level-data-standard.readthedocs.io/en/latest/06%20spatialdata/#using-a-navigational-satellite-system-nss-to-collect-spatial-data-in-the-field)) ([ More info in this section](http://farm-level-data-standard.readthedocs.io/en/latest/06%20spatialdata/#using-a-geographical-information-system-gis-to-to-collect-spatial-data-in-the-field)).

## Using a Navigational Satellite System (NSS) to collect spatial data in the field.
A [Navigational Satellite System](https://en.wikipedia.org/wiki/Satellite_navigation) is a constellation satellites with accurately known positions or orbits that transmits coded radio signals. These coded radio signals are used by specialized electronic devices to calculate the location on the earth’s surface relative to the satellite constellation. Currently the American [NAVSTAR Global Positioning System or GPS](http://www.gps.gov/) is the most used system. However alternative systems exist, or become operational soon in the future (see also the below table below). Nowadays some receivers can already use the data from these alternative systems, or combine the signals of several systems. Combining the data from 2 or more NSS increases the accuracy of the measurement and decreases the search time for satellites data connections. Measurement with a NSS has an error. This error is depending on the system used, the openness of the sky above the location device (no buildings or trees), the number of satellites above the horizon at the moment of the measurement and actual position of these satellites in the sky. Under optimal conditions the error varies between 2 and 10 meters.  

System | Coverage | Public horizontal Accuracy | Current Status | [TRF]( http://www.navipedia.net/index.php/Reference_Frames_in_GNSS)
--- | --- | --- | --- | ---
[GPS](http://www.gps.gov/) | Global | 2-9m | Operational | WGS84
[GLONASS](https://www.glonass-iac.ru/en/) | Global | 4-7m | Operational | PZ-90
[BeiDou-2](http://en.beidou.gov.cn/) | South East Asia and Australia | 10m | Regionally Operational, Global in 2020 | BTRF
[Galileio](http://www.esa.int/Our_Activities/Navigation/Galileo_and_EGNOS) | Global | 4m | Accessible,fully Operational in 2019 | GTFR
[NAVIC](http://www.isro.gov.in/irnss-programme) | 1.500 km beyond the Indian subcontinent | 10m | Operational | ITRF

### Collecting a point location

*The following procedure is derived from the SAN guidelines for certificate mapping produced by the Rainforest Alliance.*

There are many mobile apps that turn an Android or iOS smartphone into a mapping tool; the following are just two examples that are free, easy to use, and work offline. These programs should be configured in the settings to report in decimal degrees. It is best to report location points by saving “waypoints” and downloading these onto your computer; this avoids the possibility of transcription errors. It is also possible to read the latitude and longitude coordinates directly off the app display and record this information in a notebook or data form. To increase the accuracy of your measurement towards 1m multiple measurements can be taken at the same location and then averaged. Some GPS systems have an automated option for this. 

Using [GPS Essentials](http://www.gpsessentials.com)
This app provides a suite of location tools, including a tool for collecting points (waypoints). To collect a location point with GPS Essentials, click on the waypoints icon and the orange “plus” button in the bottom right corner (see screenshots below). Next, wait for a moment for your phone to pick up satellites and improve accuracy. The accuracy of your GPS should be 10m or less. Now, enter the name and description of the waypoint and click “create”; you can now read the latitude and longitude location of your point. If you like, you can save your point and export it to your computer. To do this, open the “Waypoints” button, click the three dots in the upper right corner for the pull-down menu and select “Export” to email the data to yourself as a .kml file. 

![GPSessentials screenshots](https://github.com/firstmile/reference-framework/blob/master/docs/_static/GPSessentials.gif "GPSessentials screenshots")

**Using My Maps**
Google My Maps is a mobile app and also a web-based application that runs on your desktop. The My Maps mobile app is similar to the Google Maps app that comes with many phones; however, it has additional functionality and must be downloaded and installed as a separate application. Once you have installed the app on your device and logged in with your Google account, you can create your own maps and add points. When you return from the field and connect with the Internet, these mobile maps synchronize with your desktop web-based My Maps program, where the data can be exported as a .kml file.

When in the field, launch the Google My Maps mobile app. To add a waypoint, click the blue “+” sign in the lower right corner (see figure x), click on “Add a new point”, select the location, select the layer, and give the point a name and description. You also may be able to add points by holding down at a point in the screen for a few seconds; then you will be prompted to name and save this point. You can now read the latitude and longitude location of your point. If you like, you can also now view the point in Google Maps – My Maps, since the point will automatically sync through your Google account. 

![Google My Maps screenshots](https://github.com/firstmile/reference-framework/blob/master/docs/_static/googlemymaps.gif)

### Collecting a polygon in the field. 
A polygon is a 2 dimensional feature defining the border of a surface area with a series of points. In the polygon data model the points are interconnected by line segments in the same order as they are recorded. A polygon can readily be used to map a field or a waterbody. The best way to map a field or a waterbody is to walk around the object in the field and to only measure the corners of the fields manually as a waypoint. It is not recommended to use an automated trace function to measure the boundary or to take multiple points along the boundary of a field, this decreases the accuracy or the measurement: 
* First of all when a trace function is used any deviation from the boundary, caused for example because part of the boundary is not walkable will be recorded. This will result in an oddly shaped boundary and higher inaccuracies for area calculations.
* Secondly when measuring distances and areas the relative error in the measurement decreases with the distance between the measurements. For example if 2 points are located 20m apart and the GPS has an accuracy of ±5m, the relative error in the measurement is ±50%. However if the distance between 2 points is 200m with the same accuracy, the relative error decreases to ±5% only. The same mechanism applies to area calculations. In conclusion to increase the accuracy of distance and area calculations the distance between the point measurements need to be maximized. This happens when only the corner points op polygons are being measured and not the inbetween points along the edges.

## Using a Geographical Information System (GIS) to collect spatial data. 
Another approach is to digitize areas and locations from a screen using a geografical information system or GIS. A IS can be desktop or webbased. The 2 main desktop applications are [QGIS](http://www.qgis.org/nl/site/) and [ArcGIS](http://www.esri.com/arcgis/about-arcgis). Both application has similar functionalities whereas ArcGIS is proprietary software and QGIS open source software and need a specialist to operate the system. The community [Geo for All](http://www.geoforall.org/) has mission to make geoanalysis accessible for all providing freely accessible training programs on the use of QGIS. Beside desktop GIS systems, webbased GIS systems are available. Most of these web apps provide visualization and digitization functionalities. Examples are [Google Earth]( https://www.google.nl/intl/nl/earth/) and [Google My Maps](https://www.google.com/maps/about/mymaps/) and are available free of charge.

Screen digitization is always in relation to another data source (aerial photograph, satellite image or GIS file). There are a number of points to take into account:
* The TRF of the reference source and the TRF that is used for the digitization. Local datasets used are possibly to based on a different RTF. The combination of data sources with different TRF's or other data handling using the wrong TRF leads to errors in the results. More advanced desktop GIS, like QGIS or ARCGIS are capable of making data transformations from one TRF to another TRF but need to be operated by a specialist.
* The accuracy of the reference data set is determining the accuracy of the end result. Field boundaries or boundaries between farms may not be clear on an aerial photograph for small holder farms. Boundaries maybe not visible or appear fuzzy. It is best to check the quality of a third party data set by overlaying it with actual field measurements or other data with known accuracy.

*The following procedure is derived from the SAN guidelines for certificate mapping produced by the Rainforest Alliance.*

### Point locations
If the location of interest can be identified in a web-map or via satellite view, then it may be easy to obtain the GPS coordinates from the screen. In Google Earth, just place the cursor at the desired location and read off the coordinate values from the “Status bar” at the bottom of the screen. In Google Maps, simply create a point or marker at the desired location and then click on that marker to display the properties, which will show the GPS coordinates (usually at the bottom left of the pop-up). When reporting these points, make sure that they are in Decimal Degrees. 

### The digitization of polygons 

**Using Google Earth**
Google Earth Pro is a program that you can download for free and install on your computer ([download here](https://www.google.com/earth/download/gep/agree.html). After installing the program, select from the main menu Tools à Options and configure: show Lat/Long in Decimal Degrees (3D View tab).

The Google Earth screen is divided into 3 panels on the left-hand side of the screen and one larger panel with the “Map Viewing Area” in the center (see screenshot below). For the purpose of mapping farm polygons, you will mainly utilize the “Map Viewing Area” and the “Places panel”, which is where your data can be referenced and organized. The content layers under the folder “My Places” are automatically copied to your hard drive when you exit the program and re-loaded the next time it is launched. 

![Google Earth screenshots](https://github.com/firstmile/reference-framework/blob/master/docs/_static/Googleearth.gif "Google Earth screenshots")

If you have reference points collected in the field in .kml or .kmz format can simply be loaded into Google Earth by double-clicking on the .kml or .kmz file. Alternatively, you can also open kml/kmz, gpx and many other types of spatial data by clicking on File à Open. Data imported into Google Earth are stored in the “Temporary Places” folder of the “Places panel.” You must remember to move the files up to one of your folders so that they are not lost when you exit the program.

When time-stamped GPS data are imported and displayed in Google Earth, the “Time slider” is automatically displayed at the top of the screen (figure 5). This slider has “Range Makers” that control the time and date range of the tracks and points that are displayed. This is important because sometimes you might think your data has disappeared, when it is only out of the range specified in the time slider. To view all the data, move the range markers to the far right and left sides to define a wider date range.

![Google Earth Time slider](https://github.com/firstmile/reference-framework/blob/master/docs/_static/Googletimeslider.gif"Google Earth Time slider")

To draw a polygon, follow these steps (figure 6):
1.      Select the <Add polygon> tool.
2.      Click on the map at the location of the polygon corners (vertices), going around the entire edge of the polygon to define its shape.
3.      When done, give the polygon a name in the “Name” field and add any additional details in the “Description field.”
4.      Click on the “Style, Color” tab to define how the polygon is displayed.
5.      Click on <OK> to save the polygon.

![Polygon digitizing steps in Google Earth](https://github.com/firstmile/reference-framework/blob/master/docs/_static/Googletimeslider.gif "Polygon digitizing steps in Google Earth")

Polygon digitizing steps in Google Earth.

Once you have created your polygon you should see it in the left Places panel. You can edit both the vertices and the properties by right-clicking on the item in the Places panel and selecting properties. To save the polygon(s) as a kml/kmz file, in the Place panel move all the polygons you want to save into one folder, right-click on the folder, select “Save Place As” and enter the name and location of the output file (figure 7).

Figure 7. Example of how to save polygons as a kmz file.
 
**Using polygons with Google My Maps**
Google My Maps is an extension of Google Maps. It can be used as part of Google Maps on any internet browser (after you sign in using your Google account); on a smartphone it must be downloaded as a separate app. All maps and data created in either form can be displayed and edited in the other. Since maps are web-based, they can be shared and edited by multiple users. To use [Google Maps](https://www.google.com/maps/d/?hl=en_US&app=mp), open the website and sign-in with your Google credentials. This will take you to the My Maps home screen, where you can create a new map (figure 8). For a tutorial on how to create a Google My Maps, [Clickhere](https://www.youtube.com/watch?v=TftFnot5uXw).  


Figure 8. Google My Maps home screenshot.

Click on the “Create a New Map” button in the upper left corner to initiate your new map. Now you are ready to start using your map. Give the map a name, zoom-in to your area of interest and select the basemap from the various options (map, terrain, satellite, atlas and more).

**Upload data into Google My Maps**
As Google My Maps is entirely web-based, whatever data you collect in the field on the My Maps app (waypoints, lines) will automatically sync into the desktop map. It is also possible to import spatial data stored .kml, .kmz, .cvs or .gpx files. To do this, first click on <Add layer> and then click on the <Import> button that appears under the new layer. A window is displayed for you to upload or drag / drop files to be imported (figure 9).

Figure 9. Google My Maps import window.

**Create and edit polygons in Google My Maps**
Use the tools in the upper center of the map to create points, lines and polygons. To create a polygon, use the line tool and go around the perimeter of the desired polygon area clicking to create a vertex at every corner and then click on the first point to complete the polygon. If you have collected reference points from the field and imported them to Google My Maps, these can help indicate where to draw the polygon vertices. When you are finished, enter the polygon name and description, and save (figure 10).

Figure 10. Example of a farm polygons drawn in Google My Maps.
All features created can be symbolized by selecting the line thickness, icon type, and color. Note that when you create a point, the latitude / longitude coordinates are displayed at the bottom of the point’s information window. Maps are automatically saved as you work.

To export the map, click on the three dots in the top right of the map box, select “export to kml” and select whether you want to export all the map data, or just the data in a specific layer. Note that Google My Maps has limited ability to move and organize features into layers, so for complex sites, it might be necessary to export the map into a more full-featured program, such as Google Earth, to organization the multiple polygons.


## Some more background on the complexity behind geodata
When working with spatial data it is important to be aware of the complexity behind it. Locations in space are generally described in mathematics, as points in a rectangular coordinate system consisting of three axis (x,y,z). However when we are thinking and talking about the world around us in daily live, we are actually mentally flattening the curved surface of the earth in the 2 dimensions (x,y)  of a flat plane and define height (z) as the elevation of the surface above sea level. This section explains some fundamentals from geodesy and cartography to get an understanding of this complexity and to avoid mistakes during spatial data handling because of misinterpretations.

The description of the earth surface in coordinates is based on mathematical models called [Terrestrial Reference Frames (TRF)](https://www.iers.org/IERS/EN/Home/home_node.html).  A modern TRF is defined by *a Datum* and *a Geoid model* of the earth.

"source=http://www.dauntless-soft.com" 
"source=http://www.asu.cas.cz)" 

Figure x: Visualization of a Datum and a Geoid. A Datum is a mathematical description of the earth surface, which is used to pinpoint a location on earth’s surface in latitude and longitude coordinates.   A Geoid is a mathematical model of the mean sea level across the globe based on the earth’s gravitational field as reference to measure height. In the figure the color scheme is expressing the difference in meters between the geoid model surface and the ellipsoid model surface in meters (see text below for further explanations).

[A Datum](https://en.wikipedia.org/wiki/Geodetic_datum) is a numerical description of the earth surface as an ellipsoid. This ellipsoid is the used to pinpoint locations on the earth’s surface in latitude and longitude coordinates. [Latitude](https://en.wikipedia.org/wiki/Latitude) is a geographic coordinate that specifies the north–south position of a point on the Earth's surface. Latitude is an angle which ranges from 0° at the Equator to + 90° at the North Pole and -90° at the South pole. Lines of constant latitude are called parallels and run east–west as circles parallel to the equator. [Longitude]( https://en.wikipedia.org/wiki/Longitude) is a geographic coordinate that specifies the east-west position of a point on the Earth's surface. Lines of constant longitude are lines running from the North Pole to the South Pole called meridians. The longitude of a location is measured as the angle east or west from a reference Meridian, ranging from 0° at the reference to +180° eastward and −180° westward. Different Datums are being used to describe different parts of the world, resulting into different locations for the same location when using the same coordinates in different reference frames. The distance between 2 points with the same coordinates using different datums may go up to several kilometers. 
Height in daily live is measured as the elevation of a point above sea level. This measurement is challenging when it needs to take place in landlocked country in the middle of a continent. As a starting point in a modern TRF uses an Earth Gravitational Model (EGM)  to model the mean sea level for all water surfaces, but also across land surfaces (see figure x). This model of the mean sea level across the globe is called a [Geoid]( https://en.wikipedia.org/wiki/Geoid). The Geoid’s of modern TRFs match each other [within the centimeter meter accuracy](http://www.navipedia.net/index.php/Reference_Frames_in_GNSS),  taking [EGM]( http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.html) as a starting point for the model.

Globally the [WGS84 TRF](http://earth-info.nga.mil/GandG/update/index.php?dir=wgs84&action=wgs84) developed by the US Department of Defense is the most widely used TRF for many years now as a result of the rise of the usage of [Global Positioning Systems (GPS)](http://www.gps.gov/) for field work, mapping and navigation. This drastically simplified the exchange of spatial information and logically the WGS84 is also the standard recommended in this document. However there are still 2 points to be aware off: 
* The WGS84 reference system has been updated several times in the past and will be updated in the future. For the mapping purposes as discussed in this document [the WGS84 can be considered stable since 1996](http://earth-info.nga.mil/GandG/publications/tr8350.2/wgs84fin.pdf). Before this date the WGS84 TRF was using an ellipsoid rather than a geoid as a reference to express the height above the earth’s system. The difference in height between the WGS84 TRF and the height value based on the modern WGS84 is between −105 m and +85 m. [The GeoidEval utility](https://geographiclib.sourceforge.io/cgi-bin/GeoidEval) can be used to calculate the height difference between the old model and the new model at every location on earth.
In addition paper maps or digital data coming from external sources may be using different datums. There is a whole history in mapping and geodesy finding the most accurate representation of the earth in different regions. http://epsg.io/ provides overview of all TRFs in use and the transformations between.

In practice when we are working with spatial data, for example measuring distances, working on a paper map, a computer screen and even using the GPS map display, we are working with spatial data presented on a flat surface not on a globe model. The mathematical transformation from a ellipsoid representation of x,y coordinates on a flat surface is called a map projection. To illustrate how different concepts work common projections are visualized in figure X. Every type of projection is an imperfect representation of you data and will be distorted in some way. Some methodologies are specifically capable of preserving area relations, shapes objects or the distance between points, but none will preserve all. [There are endless ways to make map projections](https://en.wikipedia.org/wiki/Map_projection) depending on the region and the purpose of the map and this is important to realize when using external data sources. The [Universal Transverse Mercator projection](http://earth-info.nga.mil/GandG/coordsys/grids/utm.html) is popular world wide applicable map projection system. http://epsg.io/ also provides a comprehensive database and access to all coordinate systems worldwide, including the map projection and the TRF and mathematical transformations between them. The data based can be easily be searched for your region by clicking on a map. 

Popular applications, like google maps, bing maps, openstreet maps etc. are using [the webmecator projection](https://en.wikipedia.org/wiki/Web_Mercator). Despite the popularity of these applications it has taken a long time before the webmecator projection was accepted by the Geodetic community as an appropriate map projection system. The key problem of this system is that the ellipsoid model of the earth to project lat long coordinates on a plane is replaced by a spherical model to speed up calculations and internet response times. [This results in systematic error up to 40 km’s]( http://earth-info.nga.mil/GandG/wgs84/web_mercator/(U)%20NGA_SIG_0011_1.0.0_WEBMERC.pdf) when compared a spheroid projection based on WGS84. In addition the ‘primitive’ [mercator projection](https://en.wikipedia.org/wiki/Mercator_projection#Mathematics_of_the_projection), dated from the middle ages, heavily distorts distances and areas at latitudes further from the equator, for example Greenland is projected with similar dimensions as latin America.The key advantage of the mercator is that it allows for effortless zooming in a squared world and angles between points on the map are preserved.  In online applications as google maps, ArcGIS Online or bing maps the errors in distance and area calculations are generally fixed making calculations in an alternative TRF.  However the [National Geospatial-intelligence Agency still warns](http://earth-info.nga.mil/GandG/wgs84/web_mercator/) for the incompatibly with and non-compliance of this type of applications to the WGS 84 TRF. [This ESRI website](http://servicesbeta.esri.com/demos/compareMeasurements.html) illustrates the differences that are produced by different map projections stressing the need to be aware of the TRF and map projection that is used while working spatial data, especially while calculating distance and surfaces.

"source=Dylan Prentiss, Department of Geography, University of California, Santa Barbara."

Figure x: Visualization of 3 types of map projections: the cylindrical, conical, and planar projection. If the globe is imagined as a wire-frame model with a light source in the center, the shadows created beyond the sphere can be "projected" onto a flat surface. 






