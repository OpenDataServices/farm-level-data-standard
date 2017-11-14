The farm
=========
**Definition**
A farm is described as a collection assets managed as 1 entity with the primarily objective to raise living organisms for food or raw materials. A farm often consists of fields, buildings and livestock and is run a farm manager and the farm owner has the rights on the produce. The farm owner and the farm owner are often united in 1 person: the farmer. A farm manager is often supported by farm workers to carry out the activities.

**Data attributes**

In the data model the farm modelled as a placeholder for foreign keys uniting all relevant data entities based on their keys together as 1 farm, including the farmer, the farm owner, the plots of the farm, the herds and the workers etc. 

Additional data entities describing the farm as a whole can be added to this data entity, like the farm boundary, farm area, or aggregated numbers like total amount of produce. Plot specific attributes should be added to the plot like the produce from a specific plot or a plot boundary.

As explained in section '*Uniquely identifying data elements*' {GroupRecordGlobalID, GroupInternalID, GroupGeoID} provides the means to: 1 globally uniquely identify all the records of farmer groups, 2 to to provide each farmer group with a unique interal ID which allows to link to link other data entities to this farmer group and; 3 to have a clue to uniquely identify this farmer group in the field or to clean the dataset when combined with datasets from other sources.

**Datastructure**
Required data attributes are indicated by grey shaded fields in the table below.
* By clicking on the blue table title -> all data attributes become visable, 
* By clicking on the data entity buttons -> all data ttributes become visable of that data entity and.
* By clicking on the {} symbols -> the JSON becomes visable 
<script src="../../_static/docson/widget.js" data-schema="../../../schema/components/Farm.JSON"></script>
