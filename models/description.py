from jsonmodels import models, fields, errors, validators

class Date(models.Base):
    expression = fields.StringField(required=True)
    begin = fields.StringField(required=True)
    end = fields.StringField()
    date_type = fields.StringField()

class Extent(models.Base):
    number = fields.StringField(required=True)
    unit = fields.StringField(required=True)

class Container(models.Base):
    top_container = fields.StringField()
    top_container_indicator = fields.StringField()
    sub_container = fields.StringField()
    sub_container_indicator = fields.StringField()
    sub_sub_container = fields.StringField()
    sub_sub_container_indicator = fields.StringField()

class DigitalObject(models.Base):
    URI = fields.StringField()


class Component(models.Base):
    id = fields.StringField(required=True)
    collection_id = fields.StringField(required=True)
    title = fields.StringField(required=True)
    title_filing_si = fields.StringField()
    repository = fields.StringField(required=True)
    level = fields.StringField(required=True)
    collection_name = fields.StringField(required=True)
    dates = fields.ListField(Date)
    extents = fields.ListField(Extent)
    languages = fields.ListField(str)
    creators = fields.ListField(str)
    names = fields.ListField(str)
    subjects = fields.ListField(str)
    places = fields.ListField(str)
    abstract = fields.ListField(str)
    accessrestrict = fields.ListField(str)
    scopecontent = fields.ListField(str)
    accruals = fields.ListField(str)
    altformavail = fields.ListField(str)
    appraisal = fields.ListField(str)
    arrangement = fields.ListField(str)
    bibliography = fields.ListField(str)
    bioghist = fields.ListField(str)
    custodhist = fields.ListField(str)
    fileplan = fields.ListField(str)
    note = fields.ListField(str)
    odd = fields.ListField(str)
    originalsloc = fields.ListField(str)
    otherfindaid = fields.ListField(str)
    phystech = fields.ListField(str)
    prefercite = fields.ListField(str)
    processinfo = fields.ListField(str)
    relatedmaterial = fields.ListField(str)
    separatedmaterial = fields.ListField(str)
    userestrict = fields.ListField(str)
    materialspec = fields.ListField(str)
    physloc = fields.ListField(str)

    containers = fields.ListField(Container)
    has_digital_object = fields.StringField()
    digital_objects = fields.ListField(DigitalObject)
    components = fields.ListField()