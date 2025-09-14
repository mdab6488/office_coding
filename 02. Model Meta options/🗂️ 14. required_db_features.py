# Purpose: Lists database features that must be present for the model to be used.

class GISModel(models.Model):
    geometry = models.GeometryField()

    class Meta:
        required_db_features = ['gis_enabled']

