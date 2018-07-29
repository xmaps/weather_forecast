from django.db import models


class City(models.Model):
    """
    Represents the different cities with weather forecast
    """
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)

    def __str__(self):
        return '{}, {}'.format(self.name, self.country_code)


class Forecast(models.Model):
    """
    Represents the weather forecast associated to the cities
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # temperatures saved with Unit as Kelvin
    temperature = models.FloatField(null=True)
    max_temperature = models.FloatField(null=True)
    min_temperature = models.FloatField(null=True)
    # pressures saved with unit as Atmospheric pressure (hPa)
    pressure = models.FloatField(null=True)
    pressure_at_sea = models.FloatField(null=True)
    pressure_at_ground = models.FloatField(null=True)
    # humidity and cloudiness as percentage
    humidity = models.FloatField(null=True)
    cloudiness = models.FloatField(null=True)
    weather_description = models.CharField(max_length=250, null=True)
    # wind speed as meter/sec
    wind_speed = models.FloatField(null=True)
    wind_degrees = models.FloatField(null=True)

    def __str__(self):
        return 'Forecast for {} on {} at {}'.format(self.city.name,
                                                    str(self.date),
                                                    str(self.time))
