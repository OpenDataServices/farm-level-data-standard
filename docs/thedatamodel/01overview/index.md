Overview of the JSON model
============================

The complete data structure is visualised in the table below:
* All required data attributes are indicated bold in, 
* By clicking on the blue table title -> all data attributes become visable, 
* By clicking on the data entity buttons -> all data ttributes become visable of that data entity and.
* By clicking on the {} symbols -> the JSON becomes visable 

<script src="../../_static/docson/widget.js" data-schema="../../_static/Firstmilefarmerdatab.JSON"></script>

### Description
In [JSON schema language]( http://json-schema.org/) the data entities making up the conceptual model (Group, Farmer, Farm, Plot, Plotobservation) as described in the conceptual model are stored as [arrays of JSON objects](https://specs.frictionlessdata.io/table-schema/).

Each time a data entity is recorded a new JSON object is created and added to the array. The recording of the same data entity at another point in time needs to be added as a new record to allow for continuous monitoring and to allow the composition of farms and ownership to change overtime. The recording of the data entities therefore are timestamped. 

In the reference framework a system of 3 identifiers is proposed to uniquely identify objects and model the relationships between these objects. These Identifiers are called: 1 the InternalID, 2 the GeoID and 3 the GlobalRecordID. The system allows the exchange and merging of data that is structured in a similar way.

* **The InternalID** provides a means internally structure the data set uniquely identifying the objects in the dataset and relations between them.

* **The GeoID** provides an imperfect means to uniquely identify the object in the field and to clean the dataset when it is combined with datasets from other sources.

* **The GlobalRecordID** is a globally unique identifier for First Mile Farm data record.

**The GeoID** and **the GlobalRecordID** can be used to maintain the InternalID structure while exchanging data between organisations. This mechanism will be explained in more detail in the section on '*the identification Uniquely Identifying Objects*'. 

It is not required use all data entities (Farmer grouo, Farmer, Farm, Plot, Plot Observation) in a data bases while using the data structure. For example some organisations only want to collect plot level data, so no details are needed/available on which farmer manages the plot or to who the plot belongs. The arrays for group, farmer, and farm can be left empty. 

However to maintain compatibility of different global data sources it is essential that all data attributes are recorded at the right data entity level to maintain the internal structure of the data format. For example it does not fit the logic of the reference framework to add an attribute ‘farm size’ to the data entity ‘farmer’, even if that farmer owns or manages that farm. The farm and it’s size are inextricable, even if this is the only attribute recorded about farms in the data set. As a result the farm size of a farmer's farm can only be found by first finding the farm instance of the farmer's farm using internals keys and next the size of that farm instance.  

### Extensions

The reference framework is designed in such away that new data attributes or even new data entities for different purposes can be added to the model easily. This is illustrated under the heading extensions, for Cocoa action program and MARS Adoption Observations. The data formats are available together with the official protocols on how to collect the data in the field. 

By adding more and more extensions to the reference framework, a repositry emerges of 'proven' data formats and data collection protocols. Organsations can benefit from this repositry harvesting the formats and data collection protocols they need for their own data management. Having different data formats and datacollection methodologies in 1 repositry will also facilitate further standardization and interoperability discussions. To add to the reference framework please contact andre.jellema@data-impact.com.

In the following sections the core data entities of the generic data structure for farm data collection, storag and exchange will be further elaborated.

### Flattened table in Excel format*

A flattened table in excel format is avialable [here](https://docs.google.com/spreadsheets/d/1lmKCK8K4ZXjjW23dOeA7WtUf3QbyhKg3HWF_7StsAsY/edit?usp=sharing) The flattened table can be used to make a mapping from an existing data structure to the generic data structure for farm data collection, storag and exchange.

