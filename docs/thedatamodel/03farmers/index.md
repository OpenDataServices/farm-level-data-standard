The farmer
=========
**Definition**
The farmer is the person that manages one or more farms, possibly helped by farm workers. The farmer takes the major management decisions even when the decision is to do contract farming where the farm practice is often prescribed in detail by an external actor. In this model the farmer is not necessarily the owner of the farm. A farmer can manage someone else’s farm. Nor does he or she need to be the owner of the assets composing the farm, e.g a sharecropper is seen as a farmer in this model. For a more detailed explanation on how ownership plays a role in modelling different farm types, see also the conceptual model in '*the approac*' section.

**Data attributes**

groupInternalIDs is an array of database specific identification linking a farmer to 0, 1 or more groups.

As explained in section '*Uniquely identifying data elements*' {GroupRecordGlobalID, GroupInternalID, GroupGeoID} provides the means to: 1 globally uniquely identify all the records of farmer groups, 2 to to provide each farmer group with a unique interal ID which allows to link to link other data entities to this farmer group and; 3 to have a clue to uniquely identify this farmer group in the field or to clean the dataset when combined with datasets from other sources.

**Datastructure**
Required data attributes are indicated by grey shaded fields in the table below.
* By clicking on the blue table title -> all data attributes become visable, 
* By clicking on the data entity buttons -> all data ttributes become visable of that data entity and.
* By clicking on the {} symbols -> the JSON becomes visable 
<script src="../../_static/docson/widget.js" data-schema="../../../schema/components/Farmer.JSON"></script>
