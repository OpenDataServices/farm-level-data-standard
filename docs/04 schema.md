# Data schema
![alt text][Main data structure]

The model consists of the main data entities Group, Farmer, Farm, Plot, Cropobservation and number of supporting data entities. New data attributes or data entities can be added to the model by submitting extensions to the model.  

<script src="../_static/docson/widget.js" data-schema="../../_static/first-mile-schema.json"></script>

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



https://github.com/firstmile/reference-framework/blob/master/_static/Neutraldatamodelgif.gif
