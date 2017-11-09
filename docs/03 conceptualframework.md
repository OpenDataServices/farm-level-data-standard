A neutral first mile farm data model  
================

## Approach
In the three schema approach a conceptual data model is proposed as an effective way to integrate between different databases and organisations. In the conceptual model the data entities are defined in the way that the end-users think and talk about concepts in the real world. It is therefore assumed that multiple organisations can easily develop a mapping from their own internal data structures onto such conceptual model because of the internal logic of the community. The conceptual model can therefore function as a neutral and organisation independent interface for the data from 1 database to another database. If all organisations would develop such a mapping (or adapt their own internal data structures), effortless and automated data exchange and data integration can take place. The reference framework for first mile farm data aims to put the foundation for such a neutral model.

In ‘first mile’ projects many different aspects of farms are being collected. Examples are the agricultural and economic performance of a farms, farming activities performed at a farm, social and environmental conditions, compliance to standard measures etc. It is beyond the scope of this document to address all of these aspects in detail, including the recommended field data collection methodologies and associated data formats. This document presents a generic structure by representing the core components of a farm as data entities. It will only discuss data attributes that are essential for the internal structure and which are needed to be able understand and combine the data, such as farmers ID or the shape of the fields or are commonly collected such as the address or expected yield. It will also present the logic how the model can be expanded with additional data attributes or data entities providing the option to customise the model and to provide the opportunity to expand the generic model into a more all comprehensive model at a later stage.

The reference framework is designed in such away that new data attributes and even new data entities for different purposes can be added easily. This is illustrated under the the heading extensions, for Cocoa action program and MARS Adoption Observations. The data formats are available as together with protocols how to collect the data in the field. 

By adding more and more extensions to the reference framework, a repositry emerges of 'proven' data formats and data collection protocols. Organsations can benefit from this repositry harvesting the formats and data collection protocols they need for their own data management. Having different data formats and datacollection methodologies in 1 repositry will also facilitate further standardization discussions. To add to the reference framework please contact andre.jellema@data-impact.com.

## Defining the conceptual data model

![Conceptual model for first mile farm data collection](reference-framework/docs/_static/Neutraldatamodelgif.gif)

To define the conceptual data model, the concept of a farm is taken as the starting point. A farm in this reference framework is defined as a collection assets managed as 1 entity with the primarily objective to raise living organisms for food or raw materials. At the farm crops are cultivated on one or more plots of land and farm animals are being kept. The farm is a run by a farmer often supported by farm workers. Different buildings may be present at the farm to support the work. The farm may consist of multiple plots, herds or buildings. Workers are not bound to 1 farm but may work at different farms. A farmer may manage several farms. A farmer may be member of one or more farmers groups. A farmer group can be a cooperative or a group of farmers loosely organised around a government or corporate program.

Many organisations are making observations in a plot during their field work. The data entity ‘plot observation’ is introduced to map the data elements directly linked to concrete  observations in the field.

The conceptual model is flexible to include a number of different farmer and farm types depending on the ownership of the farm and ownership of farm assets. Traditionally one may think of the farmer being the owner of both the farm and the farm assets, however this is not always the case. In many cases a farmer will hire or lease part of the production assets. ‘Sharecroppers’ or ‘Tenant farmers’ make use of agricultural assets which they do not own and have to pay a percentage of the profit, part of the produce or both. In ‘systems with communal land rights’ members of the community are getting fields assigned to use for farming, but do not own the land. Land use rights may change through time. The land of a farm is therefore a not static asset but may change through time.

In some cases the farmer is more like ‘the manager’ and not ‘the owner’ of the farm benefitting directly from the produce of the farm. When the rights are shared with a group of individuals, the farm can be called a ‘Communal farm’. When ownership rights are with a company the farm can be called a ‘Corporate farm’. By managing the concept of ownership well for the different data entities all of these different type of farms and farmers can be included in the model, even while ownership changes over time.

The summary report data entity is meant to add contextual information about each data release.

The logic of the model is to map the first mile data elements collected in the field work at the right level data entity. Eg.
The certified stock of a cooperative should be a data element of the data entity group
The total certified produce of a farm should be a data element of the data entity farm
The expected harvest of a field should be a data element of the data entity group

The dark blue elements indicated in the model will be detailed out more in the sections below. The lighter blue elements to visualize the logic in the model and to indicate possible extensions in the future or customization options. In case of customisation the added data elements can be described in the summary report to provide extra context and data integrity validation options.


[neutralmodel]: https://github.com/firstmile/reference-framework/blob/master/docs/_static/Neutraldatamodelgif.gif "Neutral model for first mile farm data"
