The plot
=========
**Definition**
A plot is an area of land, enclosed or otherwise, used for agricultural purposes such as cultivating crops or for livestock.

**Data attributes**
The data entity plot describes the main and general characteristics of a plot: including location and geometry, but also agronomically. Examples are this plots: 
- seed variety (name/vendor/date/quantity in kg/ha)
- yields (kg/ha)
- pesticide use (product/trade name/vendor/date/ quantity in kg/ha)
- fertilizer use (product/trade name/vendor/date/quantity in kg/ha) and application method
- measured or calculated water use  (date/quantity in kg of harvested paddy/litre water input)
- timing of the different farm activities

As explained in section '*Uniquely identifying data elements*' {GroupRecordGlobalID, GroupInternalID, GroupGeoID} provides the means to: 1 globally uniquely identify all the records of farmer groups, 2 to to provide each farmer group with a unique interal ID which allows to link to link other data entities to this farmer group and; 3 to have a clue to uniquely identify this farmer group in the field or to clean the dataset when combined with datasets from other sources.

The model can be expanded by creating rotation specific, crop specific data entities or data entities describing the agronomic conditions like soil type.

**Additional standardization resources**
- [World reference base for soil resources 2014](http://www.fao.org/3/a-i3794e.pdf)

**Datastructure**
Required data attributes are indicated by grey shaded fields in the table below.
* By clicking on the blue table title -> all data attributes become visable, 
* By clicking on the data entity buttons -> all data ttributes become visable of that data entity and.
* By clicking on the {} symbols -> the JSON becomes visable 
<script src="../../_static/docson/widget.js" data-schema="../../../schema/components/Plot.JSON"></script>
