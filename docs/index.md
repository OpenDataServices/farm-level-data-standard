<style><!--

.wy-table-responsive table td {
  /* !important prevents the common CSS stylesheets from overriding
     this as on RTD they are loaded after this stylesheet */
  white-space: normal !important;
}

.wy-table-responsive {
  overflow: visible !important;
}


--></style>

Farm Level Data Standard (documentation demonstrator)
======================================================

```eval_rst
.. toctree::
   :maxdepth: 2
   :glob:

   *
   */*

```




This is a demonstration documentation site for work on a Farm Level Data Standard.

## Schema

### Summary 

To maximize traceability of the data, each recording of a data entity carries the geolocation of the organisation that collected the data together with the internal database ID. The combination of the geolocation, the timestamp and the ID of the data entity identify the data record globally unique. To support the process of identifying and potentially cleaning the data while reusing it is recommended to add additional identifying data elements to the record (see also the chapter on identifying and geolocating data)


```eval_rst
.. jsonschema:: ../schema/Summaryreport.JSON
    :include: 
    :collapse: 
```

### Farm



```eval_rst
.. jsonschema:: ../schema/Farm.JSON
    :include: 
    :collapse: dataCollectorsGeolocation, dataCollectingOrganisationName, collectionTimeDateStamp, dataCollectorsID
```


### Farmer

```eval_rst
.. jsonschema:: ../schema/Farmer.JSON
    :include: 
    :collapse: 
```

 
### First Mile Farmer

```eval_rst
.. jsonschema:: ../schema/FirstMileFarmer.JSON
    :include: 
    :collapse: 
```


### Plot level

```eval_rst
.. jsonschema:: ../schema/Plot.JSON
    :include: 
    :collapse: 
```
 
### Crop observation

```eval_rst
.. jsonschema:: ../schema/Cropobservation.JSON
    :include: 
    :collapse: 
```


### Group

```eval_rst
.. jsonschema:: ../schema/Group.JSON
    :include: 
    :collapse: 
```



Indices and tables
==================

```eval_rst
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
