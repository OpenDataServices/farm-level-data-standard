Overview of the JSON model
============================

In the [JSON schema language]( http://json-schema.org/) the data entities making up the conceptual model (Group, Farmer, Farm, Plot, Plotobservation) as described in the conceptual model are stored as [arrays of JSON objects](https://specs.frictionlessdata.io/table-schema/).

Each time a data entity is recorded a new JSON object is created and added to the array. The recording of the same data entity at another point in time needs to be added as a new record to allow for continuous monitoring and to allow the composition of farms and ownership to change overtime. The recording of the data entities therefore are timestamped. 

The structure of the dataset and links between the objects in the real world are maintained using 3 Identifiers:
1. **The InternalID** provides a means internally structure the data set. It uniquely identifies the  objects in the dataset and relations between them. For example the InternalID can be used to links the farmer to his or her farm and the InternalID of farm can be used to link the plots to the farm. Possible the dataset contains multiple recordings of the plot at different moments in time. These two recordings will have the same InternalID.
2. **The GeoID**. When two datasets coming from different sources are merged, the InternalID's need to be updated. The GeoID provides a means to do this. To datasets addressing the same object in the field should get the same InternalID, possibly objects that have the same InternalID but are in reallity adressing to different objects should get 2 different InternalID's. The GeoID provides the database maneger to perform this cleaning process. 
3. **The GlobalRecordID** uniquely identifies a First Mile Farm data record globally. The ID can be used clean a dataset for dublicate records.

It has been chosen to use thys dynamic system of 3 ID because currently there is no global registration available that uniquely identifies farmer groups, farmers, farms or farm plots. Using these 3 IDs a global data pool of uniquely identified data records emerges, maintained in local databases allowing for the global exchange, cleaning data and analysis of First Mile Farm Data coming from different sources. This mechanism will be explained in more detail in the section on '*the identification Uniquely Identifying Objects*'. 

It is not required use all data entities in the data structure while setting up a database or data export file. for example some organisations only want to exchange plot level data, so no details on which farmer manages the plot or to which farmer it belongs to are needed. The arrays for group, farmer, and farm can be left empty. However incomplete the dataset can still be combined with a data set of farms and fields to analyze the crop distribution in a region. Even when part of the fields records occur in both datasets they would still stand out as doubles based on the timestamp, the geolocation of the data collecting organisation and the original database identifier.

However to maintain compatibility of different global data sources it is essential that all data attributes are recorded at the right data entity level to maintain the internal structure of the data format. For example it does not fit the logic of the reference framework to add a attribute ‘farm size’ to the data entity ‘farmer’. The farm and it’s size are inextricable, even if this is the only attribute recorded about farms in the data set. As a result the farm size of a farmer can only be found using InternalID connection. 

The reference framework is designed in such away that new data attributes or even new data entities for different purposes can be added to the model easily. This is illustrated under the heading extensions, for Cocoa action program and MARS Adoption Observations. The data formats are available together with the official protocols on how to collect the data in the field. 

By adding more and more extensions to the reference framework, a repositry emerges of 'proven' data formats and data collection protocols. Organsations can benefit from this repositry harvesting the formats and data collection protocols they need for their own data management. Having different data formats and datacollection methodologies in 1 repositry will also facilitate further standardization and interoperability discussions. To add to the reference framework please contact andre.jellema@data-impact.com.

<script src="../../_static/docson/widget.js" data-schema="../../_static/Firstmilefarmerdatab.JSON"></script>

*Flattened table in Excel format*

A flattened table in excel format is avialable [here](https://docs.google.com/spreadsheets/d/1lmKCK8K4ZXjjW23dOeA7WtUf3QbyhKg3HWF_7StsAsY/edit?usp=sharing) The flattened table can be used to make a mapping from an existing data structure to the generic data structure for farm data collection, storag and exchange.


In the following sections the core data entities of the generic data structure for farm data collection, storag and exchange will be further elaborated.
