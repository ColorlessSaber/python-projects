from django.db import models

# Create your models here.
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    object = models.Manager()

    # Display the title and prof name when listed on the admin page
    def __str__(self):
        # returns the input value of the title and instructor name
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # overwrite Django's default name for the model when shown on the admin page
    class Meta:
        verbose_name_plural = 'University Classes'