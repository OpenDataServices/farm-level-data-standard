# Schema

<script src="../_static/docson/widget.js" data-schema="../../_static/first-mile-schema.json"></script>

## Summary 

To maximize traceability of the data, each recording of a data entity carries the geolocation of the organisation that collected the data together with the internal database ID. The combination of the geolocation, the timestamp and the ID of the data entity identify the data record globally unique. To support the process of identifying and potentially cleaning the data while reusing it is recommended to add additional identifying data elements to the record (see also the chapter on identifying and geolocating data)


```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: summary
    :collapse: 
```

## Key tables

### Farm

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: farm
    :collapse: 
```


### Farmer

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: farmer
    :collapse: 
```

### Plot level

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: plot
    :collapse: 
```
 
### Crop observation

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: cropObservation
    :collapse: 
```


### Group

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :include: group
    :collapse: 
```

## Definitions

### Address
```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/address
    :include:
    :collapse: 
```

### ContactPoint
```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/contactpoint
    :include:
    :collapse: 
```

### GlobalID

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/GlobalID
    :include:
    :collapse: 
```

### IDGeolocation

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/GeoID
    :include:
    :collapse: 
```

### DataAttributeStructure

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/dataattributestructure
    :include:
    :collapse: 
```

### DataEntityStructure

```eval_rst
.. jsonschema:: ../schema/first-mile-schema.json
    :pointer: /definitions/dataEntityStructure
    :include:
    :collapse: 
```


### Location

Auto-documentation of location is not currently working.