Uniquely identifying data elements
=========================

### Key message
**In the reference framework a data structure is proposed to uniquely identify objects and model the relationships between these objects. The system allows the exchange and merging of data that is structured in a similar way.**  3 Identifiers are used build a structure of data entities interlinked with keys and to maintain this structure. These Identifiers are called: 1 the InternalID, 2 the GeoID and 3 the GlobalRecordID.

1. **The InternalID** provides a means internally structure the data set uniquely identifying the  objects in the dataset and relations between them. 

2. **The GeoID** provides an imperfect means to uniquely identify the object in the field and to clean the dataset when it is combined with datasets from other sources.

3. **The GlobalRecordID** is a globally unique identifier for First Mile Farm data record.

The GeoID and the GlobalRecordID can be used to maintain the InternalID structure while exchanging data between organisations.

### Introduction
In an ideal world every farmer, farm, plot or farmers group would be globally uniquely identified by some formal or informal system and these identification numbers would be generally known and used by different organisations. Organisations could make data recordings about farmer, farm, plot or farmer groups and could easily combine these recordings with other recordings trusting these globally unique IDs to sort the data and make analyses using all records combined. However currently this is an utopia, because there is no perfect system uniquely identifying all farmer, farm, plot or farmers groups globally (see also the sections below). 

Instead the reference framework uses 3 identifiers to build and internal structure and maintain a local data set of first mile farm data: 1 the internal ID, 2 the GloballyUniqueRecordID and the GeoID. 

### The InternalID
The InternalID is the ID used to uniquely identify Data Entities in a data set in a local data base and to structure the data using these internalIDs as Keys to link the farmers to farmer groups, farms to farmers, plots to farms and plot observations to plots. 

When the data set is merged with another First Mile Farm data set the internal ID needs to be updated to represent the new structure of the data sets. In principles there are **3 problems that need to be solved**.

1. *If 2 datasets are merged and they may contain information about the same farmers these farmers should get the same InternalIDs and all related Keys inside the combined dataset need to be updated.* 

2. *If 2 different farmers have the same InternalID before the merge, 1 of the 2 farmers need to get a new and unique ID during the merger and all Keys need to be updated accordingly.*

3. *If dataset a is shared with organisation b and with organisation c and next these organisations merge their datasets the newly derived data set will contain all records of dataset a twice. These doubles need to be removed from the database.*

### The GeoID
**To clean the datasets from problem 1 and 2 the GeoID is introduced.** The GeoID is the location of an object in WGS84 coordinates and a description of where the geolocation is measured. When the WGS84 TRF (*see also the section on spatial data acquistion and standards*)  is viewed as an register using 2 ID numbers, WGS84 can be considered as the only registration system that is consistently used globally to uniquely “identify” objects over the past 20 year. However the location of an object may have different interpretations between different data collectors, therefor a description of where the geolocation is measured is made part of the GeoID to ease the cleaning process. One can imagine that the cleaning based on geolocation will be made with much more confidence when all GeoIDs are taken at the doorstep of a farm and not at the location where the interview is taken. However sometimes the GeoID can not be taken at the doorstep, therefor different options are provided with decreasing accuracy:

1. Location of main entrance of the object or the front door of the main office from where operations take place; 

2. Centerpoint of the object or centerpoint of area of operation of the object; 

3. Location on the object or in the area of operation; 

4. Location near the object or near the area of operation of the object; 

5. Location where the interview has taken place

It is assumed that even the location of an interview is relative in the proximity of the place where a farmer has is activities. It may be the only information available and is still informative on the area where the farm is located. Therefore it is recommended to add additional identifying information if available to facilitate the cleaning process, like:

*the legal or official name

*the legal registration number (and what kind)

*the Address

*etc. (*see also the section below on alternative ways of identification for more suggestions*)

### GloballyUniqueRecordID 
**To solve problem 3 the GloballyUniqueRecordID is used.** The GloballyUniqueRecordID is considered an indivisible part of the data record and attached to it at the time of recording. The GloballyUniqueRecordID consists of:

*The original internal ID used by the data collection organisation to identify that farmer, farm, plot, farmers group etc; When objects are uniquely identified only at project level, the project ID needs to be added to the object ID for example (Internal Project ID + Internal Object ID). 

*The latitude and longitude coordinates of the main entrance of the headquarters of the organisation that collected the data;

*Time-Date stamp of the recording.

The GloballyUniqueRecordID always needs to stay attached to the data record and should not be changed when exporting, merging or updating datasets. The GloballyUniqueRecordID also provides a means to go back to the source of the data.

In principle the reference framework is building a pool of globally uniquely identified data records. If the data model and the 3 identifiers are used consistently by it’s user group, the combined dataset of uniquely identified records can be considered as the global pool of first mile farm data allowing for global data exchange and data analysis.

### Alternative ways of identification 

All of this data could be added to the records to facilitate the identification in the field and the cleaning of datasets.

* **Using a national register** The most straightforward to uniquely identify a farmer, a farm or a piece of land would be to use an official national registration number such as, the tax number, a social security number of a civil service number, a company register number or a land registration number.  However in many countries such systems do not exist or are only partially complete and is therefore no solution that can be applied globally. Many of these data sources are also privicy sensitive. http://org-id.guide/ is resource help you to find registers of organisations in different countries.

* **Using Cooperative register** Many farmers work for a cooperative. In order to function well the cooperative needs to register all its members to administrate things like: the farmers input need, the amount of produce delivered to the farmer, debit and credits, etc. The reliability of the data in the administration of a cooperatives varies to a great extent. Moreover not all farmers are connected to a cooperative making it impossible to create a globally unique identifier.

* **Using the Blue Number** The Blue Number Initiative, led by International Trade Center (ITC), the UN and GS1, aims to make food and agriculture supply chains and systems more sustainable, contributing to the United Nations Global Goals for Sustainable Development. The Blue Number acts as a unique identifier for use by anyone involved in the food chain from farmers, producers, distributors and vendors to consumers. Currently there are about 2000 people registered mainly in Singapore.

* **Building an enumeration of real world characteristics.** Uniquely identifying a farmer by his or her name works pretty well in small groups. However when the database expands many doubles will occur. As strategy to stratification with real world characteristics can be created in the database to maintain the small groups with mostly unique names. An examples of such a stratification is to add the names of the lowest and second lowest administrative zones to the name the farmer.

* **Universally unique identifier** Many technology companies use a universally unique identifier (UUID) to identify farmers and other objects in their databases. A UUID is a 128-bit number which is generated to identify information in computer systems. When generated according to the standard methods, UUIDs are for practical purposes unique, without depending for their uniqueness on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes. While the probability that a UUID will be duplicated is not zero, it is so close to zero as to be negligible. However these UUID are generally applied within the context of one organisation or even one project. This means that the same farmer will have two different identifiers between 2 organisations or even 2 projects. This means that when data sources from different origin are being combined for re-use, one farmer can appear in 2 or more records with different ID numbers.
