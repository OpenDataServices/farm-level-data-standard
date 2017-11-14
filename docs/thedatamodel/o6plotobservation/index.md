The plot observation
=========
**Definition**
Data obtained from an assessment in a plot, generally done at a specific location, in a transect or in an area. This data entity is not meant to describe the plot as a whole. Based on observations estimates are made for the characteristics of the plot as a whole. The observations are records of the ‘plot observation’ data entity, where as the estimation for the plot as a whole based on the observations should be added as a data attribute of the plot data entity. For example in a grass plot the biomass is measured at 3 points. This can be added to the data set as 3 plot observation records, the average biomass calculated for the plot can be added to the plot data entity.

**Data attributes**
Typical observations in a plot are: 
- three height, 
- number of branches, 
- good capture light and aeration, 
- height of Jorquette, 
- percentage of trees show old wilted, 
- number of dead or mummified pods, 
- number of dead branches, 
- number of damaged or diseased pods, 
- number of epiphytes 
- number of ant nests/tunnels nests,
- etc. 

As explained in section '*Uniquely identifying data elements*' {GroupRecordGlobalID, GroupInternalID, GroupGeoID} provides the means to: 1 globally uniquely identify all the records of farmer groups, 2 to to provide each farmer group with a unique interal ID which allows to link to link other data entities to this farmer group and; 3 to have a clue to uniquely identify this farmer group in the field or to clean the dataset when combined with datasets from other sources.

**Additional standardization resources**
- [ISRIC - WoSIS exchange requirements](http://www.isric.org/sites/default/files/isric_report_2015_03.pdf)

**Datastructure**
Required data attributes are indicated by grey shaded fields in the table below.
* By clicking on the blue table title -> all data attributes become visable, 
* By clicking on the data entity buttons -> all data ttributes become visable of that data entity and.
* By clicking on the {} symbols -> the JSON becomes visable 
<script src="../../_static/docson/widget.js" data-schema="../../../schema/components/Plotobservation.JSON"></script>
