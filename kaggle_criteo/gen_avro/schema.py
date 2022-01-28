SCHEMA = """
{
  "type" : "record",
  "name" : "Kaggle-Criteo",
  "fields" : [ {
    "name" : "entityId",
    "type" : [ "string", "null" ]
  }, {
    "name" : "response",
    "type" : [ "int", "null" ]
  }, {
    "name" : "perEntity",
    "type" : [ "null", {
      "type" : "array",
      "items" : {
        "type" : "record",
        "name" : "Feature",
        "fields" : [ {
          "name" : "name",
          "type" : "string"
        }, {
          "name" : "term",
          "type" : "string"
        }, {
          "name" : "value",
          "type" : "float"
        } ]
      }
    } ]
  }, {
    "name" : "uid",
    "type" : "long",
    "doc" : "unique id for the sample"
  } ]
}
"""
