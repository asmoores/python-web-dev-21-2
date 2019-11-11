from django.db.models import (
    Model,
    CharField,
    SlugField,
    TextField,
    DateField,
    ManyToManyField,
)


from organizer.models import Startup, Tag


class BlogPost(Model):
    title = CharField(max_length=63)
    slug = SlugField(
        max_length=63,
        unique_for_month="pub_date",
    )
    text = TextField()
    pub_date = DateField()
    tags = ManyToManyField(Tag)
    startup = ManyToManyField(Startup)

    class Meta:
        get_latest_by = ["pub_date"]
        ordering = ["-pub_date", "title"]
        verbose_name = "Blog Post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
